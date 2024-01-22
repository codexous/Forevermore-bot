import discord
from discord import app_commands

client = discord.Client(intents=discord.Intents.default())


@client.tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong")


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


client.run("TOKEN")