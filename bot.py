import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Needed for reading messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="killall", description="Deletes all messages in the current channel")
async def killall(interaction: discord.Interaction):
    if not interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
        return

    await interaction.response.defer()
    deleted = await interaction.channel.purge()
    await interaction.followup.send(f"Deleted {len(deleted)} messages.", ephemeral=True)

bot.run(TOKEN)
