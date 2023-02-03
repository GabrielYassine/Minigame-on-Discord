import discord
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def jungle_clear(message, player):
    if player.movement_speed == 1:
        player.time += 15
    else:
        player.time += 30
    random_number = random.randint(100, 200)
    player.money += random_number
    reply = f"you have cleared the jungle, new balance: {player.money} gold"
    await message.channel.send(reply)