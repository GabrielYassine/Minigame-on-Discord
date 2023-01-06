import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    contents = message.content
    
async def start_game(message):
    gamemode = 1
    reply = "Welcome To Summernes Rift"
    await message.channel.send(reply, file=discord.File('map.jpg'))