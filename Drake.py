import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    contents = message.content

@client.event
async def drake_clear(message, player):
    if player.health >= player.kills + 2 and player.strength >= player.kills + 2 and player.armor_penetration >= player.kills + 2:
        player.kills += 1
        if player.kills == 4:
            reply = f"Congratulations, you have defeated all the dragons and won the game! Time: {player.time} seconds"
            player.gamemode = 0
        else:
            reply = f"You have successfully killed the {player.kills} dragon"
        await message.channel.send(reply)
