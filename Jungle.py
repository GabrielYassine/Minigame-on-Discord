import discord
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    contents = message.content

@client.event
async def jungle_clear(message, player):
    player.time += 30
    random_number = random.randint(100, 200)
    player.money += random_number
    reply = "you have cleared the jungle, new balance: {}".format(player.money)
    await message.channel.send(reply)