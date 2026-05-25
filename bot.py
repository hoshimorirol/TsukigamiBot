import discord
from discord import app_commands
from discord.ext import commands
import sqlite3
import datetime
import io
import os

# ==================== CONFIGURACIÓN ====================
TOKEN = os.getenv("TOKEN", "")
GUILD_ID = int(os.getenv("GUILD_ID", "0"))
REVIEW_CHANNEL_ID = int(os.getenv("REVIEW_CHANNEL_ID", "0"))
TRANSCRIPT_CHANNEL_ID = int(os.getenv("TRANSCRIPT_CHANNEL_ID", "0"))
TICKET_CATEGORY_ID = int(os.getenv("TICKET_CATEGORY_ID", "0"))
ADMIN_ROLE_ID = int(os.getenv("ADMIN_ROLE_ID", "0"))
MODERATOR_ROLE_ID = int(os.getenv("MODERATOR_ROLE_ID", "0"))
MEMBER_ROLE_ID = int(os.getenv("MEMBER_ROLE_ID", "0"))
UNVERIFIED_ROLE_ID = int(os.getenv("UNVERIFIED_ROLE_ID", "0"))

# ==================== BASE DE DATOS ====================
def init_db():
    conn = sqlite3.connect('applications.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        username TEXT,
        status TEXT DEFAULT 'pending',
        answers TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        reviewed_by INTEGER,
        review_note TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS review_messages (
        message_id INTEGER PRIMARY KEY,
        channel_id INTEGER,
        app_id INTEGER,
        user_id INTEGER
    )''')
    conn.commit()
    conn.close()

init_db()

# ==================== FUNCIONES AUXILIARES ====================
def is_staff(member: discord.Member) -> bool:
    admin_role = member.guild.get_role(ADMIN_ROLE_ID)
    mod_role = member.guild.get_role(MODERATOR_ROLE_ID)
    return (admin_role in member.roles) or (mod_role in member.roles)

def has_member_role(member: discord.Member) -> bool:
    member_role = member.guild.get_role(MEMBER_ROLE_ID)
    return member_role in member.roles if member_role else False

async def generate_transcript(channel: discord.TextChannel):
    """Genera un archivo .txt con la transcripción del ticket."""
    lines = []
    lines.append(f"TRANSCRIPCIÓN DE TICKET: #{channel.name}")
    lines.append(f"Servidor: {channel.guild.name}")
    lines.append(f"Fecha de cierre: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("-" * 50)
    lines.append("")

    async for msg in channel.history(limit=None, oldest_first=True):
        timestamp = msg.created_at.strftime("%H:%M:%S")
        author = str(msg.author)
        content = msg.content or ""

        if msg.embeds:
            embed_titles = [e.title for e in msg.embeds if e.title]
            if embed_titles:
                content += f" [Embed: {', '.join(embed_titles)}]"

        if msg.attachments:
            att_urls = [a.url for a in msg.attachments]
            content += f" [Adjuntos: {', '.join(att_urls)}]"

        lines.append(f"[{timestamp}] {author}: {content}")

    transcript_text = "\n".join(lines)
    file = discord.File(
        io.BytesIO(transcript_text.encode('utf-8')),
        filename=f"transcript_{channel.name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )
    return file

# ==================== MODAL PARTE 1 ====================
class ApplicationModalPart1(discord.ui.Modal, title="Solicitud — Parte 1 de 2"):
    q1 = discord.ui.TextInput(
        label="1. ¿Cómo conociste Hoshizora?",
        style=discord.TextStyle.short,
        required=True,
        placeholder="Alianzas, Disboard, invitación, otro servidor...",
        max_length=200
    )
    q2 = discord.ui.TextInput(
        label="2. ¿Aceptas las normas del servidor?",
        style=discord.TextStyle.short,
        required=True,
        placeholder="Sí / No",
        max_length=50
    )
    q3 = discord.ui.TextInput(
        label="3. ¿Qué edad tienes?",
        style=discord.TextStyle.short,
        required=True,
        placeholder="Ej: 21",
        max_length=10
    )
    q4 = discord.ui.TextInput(
        label="4. ¿Experiencia en DnD/TTRPG?",
        style=discord.TextStyle.long,
        required=True,
        placeholder="Cuéntanos tu experiencia...",
        max_length=400
    )
    q5 = discord.ui.TextInput(
        label="5. ¿Dispositivo de juego?",
        style=discord.TextStyle.short,
        required=True,
        placeholder="PC / Teléfono / Tablet / Otro",
        max_length=100
    )

    async def on_submit(self, interaction: discord.Interaction):
        bot = interaction.client
        bot.pending_answers[interaction.user.id] = {
            "q1": self.q1.value,
            "q2": self.q2.value,
            "q3": self.q3.value,
            "q4": self.q4.value,
            "q5": self.q5.value,
        }

        btn = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="Continuar a Parte 2",
            emoji="➡️"
        )

        async def open_part2(btn_interaction: discord.Interaction):
            await btn_interaction.response.send_modal(ApplicationModalPart2())

        btn.callback = open_part2
        view = discord.ui.View(timeout=600)
        view.add_item(btn)

        await interaction.response.send_message(
            "✅ **Parte 1 guardada.**\nHaz clic en el botón de abajo para completar la Parte 2.",
            view=view,
            ephemeral=True
        )

# ==================== MODAL PARTE 2 ====================
class ApplicationModalPart2(discord.ui.Modal, title="Solicitud — Parte 2 de 2"):
    q6 = discord.ui.TextInput(
        label="6. ¿Tienes micrófono?",
        style=discord.TextStyle.short,
        required=True,
        placeholder="Sí / No",
        max_length=50
    )
    q7 = discord.ui.TextInput(
        label="7. ¿Expectativas del servidor?",
        style=discord.TextStyle.long,
        required=True,
        placeholder="Cuéntanos tus expectativas...",
        max_length=400
    )
    q8 = discord.ui.TextInput(
        label="8. ¿OK con reglas caseras?",
        style=discord.TextStyle.long,
        required=True,
        placeholder="Sí / No / Depende...",
        max_length=400
    )

    async def on_submit(self, interaction: discord.Interaction):
        bot = interaction.client
        user_id = interaction.user.id

        if has_member_role(interaction.user):
            return await interaction.response.send_message(
                "❌ Ya eres miembro del servidor. No necesitas enviar una solicitud.", ephemeral=True
            )

        part1 = bot.pending_answers.pop(user_id, None)
        if not part1:
            return await interaction.response.send_message(
                "❌ Se perdió la información de la Parte 1. Usa `/apply` de nuevo.", ephemeral=True
            )

        conn = sqlite3.connect('applications.db')
        c = conn.cursor()
        c.execute("SELECT id FROM applications WHERE user_id=? AND status='pending'", (user_id,))
        if c.fetchone():
            conn.close()
            return await interaction.response.send_message(
                "❌ Ya tienes una solicitud pendiente.", ephemeral=True
            )

        # PREGUNTAS EN FORMATO NEGRITA GRANDE (como en la imagen de ejemplo)
        answers_text = (
            f"**1. ¿Cómo te enteraste de Hoshizora? (A través de Alianzas, Disboard, alguien te invitó o lo viste publicado en otro servidor)**\n{part1['q1']}\n\n"
            f"**2. ¿Estás de acuerdo con las normas del Servidor y las Reglas comunitarias establecidas?**\n{part1['q2']}\n\n"
            f"**3. ¿Qué edad tienes?**\n{part1['q3']}\n\n"
            f"**4. ¿Tienes experiencia previa en DnD u otros TTRPG?**\n{part1['q4']}\n\n"
            f"**5. ¿Juegas en PC, teléfono u otro dispositivo?**\n{part1['q5']}\n\n"
            f"**6. ¿Tienes micrófono?**\n{self.q6.value}\n\n"
            f"**7. ¿Qué esperas de esta experiencia de juego en nuestro servidor?**\n{self.q7.value}\n\n"
            f"**8. ¿Te sientes cómodo siguiendo reglas caseras o modificaciones a las reglas estándar?**\n{self.q8.value}"
        )

        c.execute(
            "INSERT INTO applications (user_id, username, status, answers) VALUES (?, ?, ?, ?)",
            (user_id, str(interaction.user), 'pending', answers_text)
        )
        app_id = c.lastrowid
        conn.commit()
        conn.close()

        review_ch = bot.get_channel(REVIEW_CHANNEL_ID)
        if review_ch:
            embed = discord.Embed(
                title=f"📋 Solicitud #{app_id} — ⏳ PENDIENTE",
                description=f"**Solicitante:** {interaction.user.mention} (`{interaction.user.id}`)",
                color=discord.Color.blue(),
                timestamp=datetime.datetime.now()
            )
            embed.add_field(name="Respuestas", value=answers_text, inline=False)
            embed.set_thumbnail(url=interaction.user.display_avatar.url)
            embed.set_footer(text="Esperando revisión del staff")

            view = bot.build_review_view(app_id, interaction.user.id)
            msg = await review_ch.send(embed=embed, view=view)

            conn = sqlite3.connect('applications.db')
            c = conn.cursor()
            c.execute(
                "INSERT OR REPLACE INTO review_messages (message_id, channel_id, app_id, user_id) VALUES (?, ?, ?, ?)",
                (msg.id, msg.channel.id, app_id, interaction.user.id)
            )
            conn.commit()
            conn.close()

        await interaction.response.send_message(
            "✅ ¡Solicitud completa enviada! El staff la revisará pronto.", ephemeral=True
        )

# ==================== MODAL: COMENTARIO DE REVISIÓN ====================
class ReviewCommentModal(discord.ui.Modal):
    def __init__(self, app_id: int, user_id: int, action: str, original_message: discord.Message):
        super().__init__(title="Comentario de Revisión")
        self.app_id = app_id
        self.user_id = user_id
        self.action = action
        self.original_message = original_message

        self.note = discord.ui.TextInput(
            label="Comentario para registro",
            style=discord.TextStyle.long,
            required=True,
            placeholder="Ej: Cumples con los requisitos. Bienvenido! / No cumples edad mínima.",
            max_length=500
        )
        self.add_item(self.note)

    async def on_submit(self, interaction: discord.Interaction):
        if not is_staff(interaction.user):
            return await interaction.response.send_message("⛔ No tienes permiso.", ephemeral=True)

        member = interaction.guild.get_member(self.user_id)
        conn = sqlite3.connect('applications.db')
        c = conn.cursor()

        if self.action == "accepted":
            if member:
                member_role = interaction.guild.get_role(MEMBER_ROLE_ID)
                if member_role:
                    await member.add_roles(member_role, reason=f"Aceptado por {interaction.user}")
                if UNVERIFIED_ROLE_ID:
                    unv = interaction.guild.get_role(UNVERIFIED_ROLE_ID)
                    if unv and unv in member.roles:
                        await member.remove_roles(unv)

                try:
                    dm_embed = discord.Embed(
                        title=f"✅ Aceptado en {interaction.guild.name}",
                        description=f"**Comentario del staff:**\n{self.note.value}",
                        color=discord.Color.green()
                    )
                    await member.send(embed=dm_embed)
                except discord.Forbidden:
                    pass

            c.execute(
                "UPDATE applications SET status=?, reviewed_by=?, review_note=? WHERE id=?",
                ("accepted", interaction.user.id, self.note.value, self.app_id)
            )

            new_embed = discord.Embed(
                title=f"📋 Solicitud #{self.app_id} — ✅ ACEPTADA",
                description=f"**Solicitante:** {member.mention if member else 'Desconocido'} (`{self.user_id}`)",
                color=discord.Color.green(),
                timestamp=datetime.datetime.now()
            )
            c.execute("SELECT answers FROM applications WHERE id=?", (self.app_id,))
            row = c.fetchone()
            if row:
                new_embed.add_field(name="Respuestas", value=row[0], inline=False)
            new_embed.add_field(name="📝 Comentario del staff", value=self.note.value, inline=False)
            new_embed.set_footer(text=f"Revisado por {interaction.user.display_name}")
            await self.original_message.edit(embed=new_embed, view=None)

            await interaction.response.send_message(
                f"✅ Solicitud #{self.app_id} **aceptada**", ephemeral=True
            )

        elif self.action == "denied":
            if member:
                try:
                    dm_embed = discord.Embed(
                        title=f"❌ Solicitud denegada en {interaction.guild.name}",
                        description=f"**Motivo:**\n{self.note.value}",
                        color=discord.Color.red()
                    )
                    await member.send(embed=dm_embed)
                except discord.Forbidden:
                    pass

            c.execute(
                "UPDATE applications SET status=?, reviewed_by=?, review_note=? WHERE id=?",
                ("denied", interaction.user.id, self.note.value, self.app_id)
            )

            new_embed = discord.Embed(
                title=f"📋 Solicitud #{self.app_id} — ❌ DENEGADA",
                description=f"**Solicitante:** {member.mention if member else 'Desconocido'} (`{self.user_id}`)",
                color=discord.Color.red(),
                timestamp=datetime.datetime.now()
            )
            c.execute("SELECT answers FROM applications WHERE id=?", (self.app_id,))
            row = c.fetchone()
            if row:
                new_embed.add_field(name="Respuestas", value=row[0], inline=False)
            new_embed.add_field(name="📝 Comentario del staff", value=self.note.value, inline=False)
            new_embed.set_footer(text=f"Revisado por {interaction.user.display_name}")
            await self.original_message.edit(embed=new_embed, view=None)

            await interaction.response.send_message(
                f"❌ Solicitud #{self.app_id} **denegada**", ephemeral=True
            )

        conn.commit()
        conn.close()

# ==================== MODAL: COMENTARIO PARA BANEO ====================
class BanCommentModal(discord.ui.Modal):
    def __init__(self, app_id: int, user_id: int, original_message: discord.Message):
        super().__init__(title="Razón de Baneo")
        self.app_id = app_id
        self.user_id = user_id
        self.original_message = original_message

        self.note = discord.ui.TextInput(
            label="Razón del baneo (opcional)",
            style=discord.TextStyle.long,
            required=False,
            placeholder="Ej: Cuenta alterna, spam, etc.",
            max_length=500
        )
        self.add_item(self.note)

    async def on_submit(self, interaction: discord.Interaction):
        if not is_staff(interaction.user):
            return await interaction.response.send_message("⛔ No tienes permiso.", ephemeral=True)

        member = interaction.guild.get_member(self.user_id)
        reason_text = self.note.value or "Sin comentario"

        if member:
            await member.ban(reason=f"Baneado desde panel por {interaction.user}: {reason_text}")

        conn = sqlite3.connect('applications.db')
        c = conn.cursor()
        c.execute(
            "UPDATE applications SET status=?, reviewed_by=?, review_note=? WHERE id=?",
            ("banned", interaction.user.id, reason_text, self.app_id)
        )

        new_embed = discord.Embed(
            title=f"📋 Solicitud #{self.app_id} — 🔨 BANEADA",
            description=f"**Solicitante:** {member.mention if member else 'Desconocido'} (`{self.user_id}`)",
            color=discord.Color.dark_grey(),
            timestamp=datetime.datetime.now()
        )
        c.execute("SELECT answers FROM applications WHERE id=?", (self.app_id,))
        row = c.fetchone()
        if row:
            new_embed.add_field(name="Respuestas", value=row[0], inline=False)
        new_embed.add_field(name="📝 Razón del baneo", value=reason_text, inline=False)
        new_embed.set_footer(text=f"Baneado por {interaction.user.display_name}")
        await self.original_message.edit(embed=new_embed, view=None)

        conn.commit()
        conn.close()

        await interaction.response.send_message(
            f"🔨 Usuario baneado y solicitud #{self.app_id} cerrada.", ephemeral=True
        )

# ==================== BOT Y VIEWS ====================
class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        self.pending_answers = {}

    def build_review_view(self, app_id: int, user_id: int) -> discord.ui.View:
        view = discord.ui.View(timeout=None)

        btn_accept = discord.ui.Button(
            style=discord.ButtonStyle.green,
            label="Aceptar",
            emoji="✅",
            custom_id=f"appy_accept_{app_id}_{user_id}"
        )
        btn_accept.callback = self.make_callback("accept", app_id, user_id)

        btn_deny = discord.ui.Button(
            style=discord.ButtonStyle.red,
            label="Denegar",
            emoji="❌",
            custom_id=f"appy_deny_{app_id}_{user_id}"
        )
        btn_deny.callback = self.make_callback("deny", app_id, user_id)

        btn_ban = discord.ui.Button(
            style=discord.ButtonStyle.danger,
            label="Banear",
            emoji="🔨",
            custom_id=f"appy_ban_{app_id}_{user_id}"
        )
        btn_ban.callback = self.make_callback("ban", app_id, user_id)

        btn_ticket = discord.ui.Button(
            style=discord.ButtonStyle.blurple,
            label="Abrir Ticket",
            emoji="🎫",
            custom_id=f"appy_ticket_{app_id}_{user_id}"
        )
        btn_ticket.callback = self.make_callback("ticket", app_id, user_id)

        view.add_item(btn_accept)
        view.add_item(btn_deny)
        view.add_item(btn_ban)
        view.add_item(btn_ticket)

        return view

    def make_callback(self, action: str, app_id: int, user_id: int):
        async def callback(interaction: discord.Interaction):
            if not is_staff(interaction.user):
                return await interaction.response.send_message("⛔ Solo staff puede usar esto.", ephemeral=True)

            original_message = interaction.message

            if action == "accept":
                modal = ReviewCommentModal(app_id, user_id, "accepted", original_message)
                await interaction.response.send_modal(modal)

            elif action == "deny":
                modal = ReviewCommentModal(app_id, user_id, "denied", original_message)
                await interaction.response.send_modal(modal)

            elif action == "ban":
                modal = BanCommentModal(app_id, user_id, original_message)
                await interaction.response.send_modal(modal)

            elif action == "ticket":
                await self.open_ticket(interaction, app_id, user_id)

        return callback

    async def open_ticket(self, interaction: discord.Interaction, app_id: int, user_id: int):
        guild = interaction.guild
        member = guild.get_member(user_id)
        if not member:
            return await interaction.response.send_message("El usuario ya no está en el servidor.", ephemeral=True)

        category = guild.get_channel(TICKET_CATEGORY_ID)
        if not category or not isinstance(category, discord.CategoryChannel):
            return await interaction.response.send_message("Categoría de tickets inválida.", ephemeral=True)

        admin_role = guild.get_role(ADMIN_ROLE_ID)
        mod_role = guild.get_role(MODERATOR_ROLE_ID)

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            member: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True),
        }

        if admin_role:
            overwrites[admin_role] = discord.PermissionOverwrite(
                view_channel=True, send_messages=True, read_message_history=True, manage_channels=True
            )
        if mod_role:
            overwrites[mod_role] = discord.PermissionOverwrite(
                view_channel=True, send_messages=True, read_message_history=True, manage_channels=True
            )

        ticket_ch = await guild.create_text_channel(
            name=f"ticket-{member.name}",
            category=category,
            overwrites=overwrites,
            reason=f"Ticket creado por {interaction.user} para solicitud #{app_id}"
        )

        welcome_embed = discord.Embed(
            title="🎫 Ticket de Admisión Abierto",
            description=(
                f"**Bienvenido** {member.mention}\n\n"
                f"Este ticket fue abierto para consultar sobre tu solicitud `#{app_id}`.\n"
                f"Un **Shinobi** del Santuario te atenderá en breve.\n\n"
                f"🔒 El staff puede usar el botón **Close** para cerrar este ticket. "
                f"Se generará un transcript automático al cerrar."
            ),
            color=discord.Color.gold(),
            timestamp=datetime.datetime.now()
        )
        welcome_embed.set_footer(text="Sistema de Tickets — Hoshizora")

        # BOTÓN CLOSE CON CONFIRMACIÓN
        close_btn = discord.ui.Button(
            style=discord.ButtonStyle.red,
            label="Close",
            emoji="🔒",
            custom_id=f"close_{ticket_ch.id}"
        )

        async def close_callback(btn_interaction: discord.Interaction):
            # Solo staff puede cerrar
            if not is_staff(btn_interaction.user):
                return await btn_interaction.response.send_message("⛔ Solo staff puede cerrar tickets.", ephemeral=True)

            # Crear embed de confirmación
            confirm_embed = discord.Embed(
                title="🔒 ¿Cerrar Ticket?",
                description="¿Estás seguro de que deseas cerrar este ticket?\nSe generará una transcripción automática.",
                color=discord.Color.orange()
            )

            # Crear botones de confirmación
            yes_btn = discord.ui.Button(style=discord.ButtonStyle.green, label="Sí, cerrar", emoji="✅")
            no_btn = discord.ui.Button(style=discord.ButtonStyle.grey, label="No, cancelar", emoji="❌")

            # Variable de control para evitar múltiples clics
            clicked = False

            async def yes_callback(yes_interaction: discord.Interaction):
                nonlocal clicked
                if clicked:
                    return await yes_interaction.response.send_message("⏳ Ya se procesó esta acción.", ephemeral=True)
                clicked = True

                # Deshabilitar ambos botones
                yes_btn.disabled = True
                no_btn.disabled = True
                await yes_interaction.response.edit_message(embed=confirm_embed, view=confirm_view)

                # Generar transcript
                file = await generate_transcript(ticket_ch)

                # Enviar transcript al canal dedicado
                transcript_ch = self.get_channel(TRANSCRIPT_CHANNEL_ID)
                if transcript_ch:
                    transcript_embed = discord.Embed(
                        title=f"📄 Transcript — {ticket_ch.name}",
                        description=f"Ticket cerrado por {yes_interaction.user.mention}\nSolicitud relacionada: `#{app_id}`",
                        color=discord.Color.blue(),
                        timestamp=datetime.datetime.now()
                    )
                    await transcript_ch.send(embed=transcript_embed, file=file)

                # Borrar el canal del ticket
                await ticket_ch.delete(reason=f"Cerrado por {yes_interaction.user}")

            async def no_callback(no_interaction: discord.Interaction):
                nonlocal clicked
                if clicked:
                    return await no_interaction.response.send_message("⏳ Ya se procesó esta acción.", ephemeral=True)
                clicked = True

                # Deshabilitar ambos botones
                yes_btn.disabled = True
                no_btn.disabled = True
                await no_interaction.response.edit_message(embed=confirm_embed, view=confirm_view)

                # El ticket permanece abierto, solo informamos
                await no_interaction.followup.send("❌ Cierre cancelado. El ticket permanece abierto.", ephemeral=True)

            yes_btn.callback = yes_callback
            no_btn.callback = no_callback

            confirm_view = discord.ui.View(timeout=60)
            confirm_view.add_item(yes_btn)
            confirm_view.add_item(no_btn)

            # Responder con el mensaje de confirmación efímero
            await btn_interaction.response.send_message(embed=confirm_embed, view=confirm_view, ephemeral=True)

        close_btn.callback = close_callback

        view = discord.ui.View(timeout=None)
        view.add_item(close_btn)

        mentions = f"{member.mention}"
        if admin_role:
            mentions += f" | {admin_role.mention}"
        if mod_role:
            mentions += f" | {mod_role.mention}"

        await ticket_ch.send(content=mentions, embed=welcome_embed, view=view)
        await interaction.response.send_message(f"🎫 Ticket creado: {ticket_ch.mention}", ephemeral=True)

    async def setup_hook(self):
        conn = sqlite3.connect('applications.db')
        c = conn.cursor()
        c.execute("""
            SELECT rm.message_id, rm.channel_id, rm.app_id, rm.user_id 
            FROM review_messages rm
            JOIN applications a ON rm.app_id = a.id
            WHERE a.status = 'pending'
        """)
        rows = c.fetchall()
        conn.close()

        for msg_id, ch_id, app_id, user_id in rows:
            channel = self.get_channel(ch_id)
            if channel:
                try:
                    msg = await channel.fetch_message(msg_id)
                    view = self.build_review_view(app_id, user_id)
                    await msg.edit(view=view)
                except Exception as e:
                    print(f"No se pudo reconstruir mensaje {msg_id}: {e}")

        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

    async def on_ready(self):
        print(f"✅ Bot conectado como {self.user} ({self.user.id})")

bot = Bot()

# ==================== COMANDOS ====================
@bot.tree.command(name="apply", description="Enviar solicitud de ingreso", guild=discord.Object(id=GUILD_ID))
async def apply(interaction: discord.Interaction):
    if has_member_role(interaction.user):
        return await interaction.response.send_message(
            "❌ Ya eres miembro del servidor. No necesitas enviar una solicitud.", ephemeral=True
        )

    conn = sqlite3.connect('applications.db')
    c = conn.cursor()
    c.execute("SELECT id FROM applications WHERE user_id=? AND status='pending'", (interaction.user.id,))
    if c.fetchone():
        conn.close()
        return await interaction.response.send_message("❌ Ya tienes una solicitud pendiente.", ephemeral=True)
    conn.close()

    btn = discord.ui.Button(
        style=discord.ButtonStyle.green,
        label="📝 Comenzar Solicitud",
        emoji="📋"
    )

    async def start(btn_interaction: discord.Interaction):
        if has_member_role(btn_interaction.user):
            return await btn_interaction.response.send_message(
                "❌ Ya eres miembro del servidor.", ephemeral=True
            )
        await btn_interaction.response.send_modal(ApplicationModalPart1())

    btn.callback = start
    view = discord.ui.View(timeout=300)
    view.add_item(btn)

    await interaction.response.send_message(
        "Haz clic para iniciar tu solicitud de ingreso a **Hoshizora**.",
        view=view,
        ephemeral=True
    )

@bot.tree.command(name="setup", description="Publicar panel de solicitudes (Admin)", guild=discord.Object(id=GUILD_ID))
@app_commands.checks.has_permissions(administrator=True)
async def setup_panel(interaction: discord.Interaction):
    embed = discord.Embed(
        title="⛩️ Ritual del Torii — Solicitud de Ingreso",
        description=(
            "Aquí comienza tu camino como **Cazador de Leyendas**.\n\n"
            "Ten en consideración que tendrás que responder un formulario que será analizado "
            "por nuestros **Shinobis** para dar tu acceso a nuestro **Santuario de Hoshizora**.\n\n"
            'Dale click al botón de **"Enviar Solicitud"** para empezar tu formulario.'
        ),
        color=discord.Color.purple()
    )
    embed.set_thumbnail(url=interaction.guild.icon.url if interaction.guild.icon else None)
    embed.set_footer(text="Sistema de Admisiones — Hoshizora")

    # BOTÓN SIN EMOJI 📨
    button = discord.ui.Button(
        style=discord.ButtonStyle.green,
        label="Enviar Solicitud",
        emoji="⛩️",
        custom_id="appy_start_apply"
    )

    async def start_callback(btn_interaction: discord.Interaction):
        if has_member_role(btn_interaction.user):
            return await btn_interaction.response.send_message(
                "❌ Ya eres miembro del servidor. No necesitas enviar una solicitud.", ephemeral=True
            )

        conn = sqlite3.connect('applications.db')
        c = conn.cursor()
        c.execute("SELECT id FROM applications WHERE user_id=? AND status='pending'", (btn_interaction.user.id,))
        if c.fetchone():
            conn.close()
            return await btn_interaction.response.send_message("❌ Ya tienes una solicitud pendiente.", ephemeral=True)
        conn.close()

        btn = discord.ui.Button(
            style=discord.ButtonStyle.green,
            label="📝 Comenzar Solicitud",
            emoji="📋"
        )

        async def start_part1(btn2_interaction: discord.Interaction):
            if has_member_role(btn2_interaction.user):
                return await btn2_interaction.response.send_message(
                    "❌ Ya eres miembro del servidor.", ephemeral=True
                )
            await btn2_interaction.response.send_modal(ApplicationModalPart1())

        btn.callback = start_part1
        view = discord.ui.View(timeout=300)
        view.add_item(btn)

        await btn_interaction.response.send_message(
            "Haz clic para comenzar tu solicitud a **Hoshizora**.",
            view=view,
            ephemeral=True
        )

    button.callback = start_callback
    view = discord.ui.View(timeout=None)
    view.add_item(button)

    await interaction.channel.send(embed=embed, view=view)
    await interaction.response.send_message("✅ Panel publicado.", ephemeral=True)

@bot.tree.command(name="stats", description="Ver estadísticas (Staff)", guild=discord.Object(id=GUILD_ID))
@app_commands.checks.has_permissions(manage_messages=True)
async def stats(interaction: discord.Interaction):
    conn = sqlite3.connect('applications.db')
    c = conn.cursor()
    c.execute("SELECT status, COUNT(*) FROM applications GROUP BY status")
    rows = c.fetchall()
    conn.close()

    embed = discord.Embed(title="📊 Estadísticas", color=discord.Color.purple())
    for status, count in rows:
        emoji = {"pending": "⏳", "accepted": "✅", "denied": "❌", "banned": "🔨"}.get(status, "•")
        embed.add_field(name=f"{emoji} {status.upper()}", value=str(count), inline=True)

    await interaction.response.send_message(embed=embed, ephemeral=True)

# ==================== INICIAR ====================
if __name__ == "__main__":
    bot.run(TOKEN)