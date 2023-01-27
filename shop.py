import discord
import asyncio
import Class

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    contents = message.content

@client.event
async def shop_open(message, player):
    reply = "Hello Summoner, you can choose to upgrade your Strength, Health or Armor penetration, you currently have {} money".format(player.money)
    shop_message = await message.channel.send(reply)
    await shop_message.add_reaction('⚔️')
    await shop_message.add_reaction('❤️')
    await shop_message.add_reaction('🛡')

    def check(reaction, user):
        return user == message.author and str(reaction.emoji) in ['⚔️', '❤️', '🛡']
    
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
        
    except asyncio.TimeoutError:
        try:
            await shop_message.delete()
        except discord.errors.NotFound:
            pass

    if player.money < 300:
        await message.channel.send("You don't have enough money to upgrade.")
        try:
            await shop_message.delete()
        except discord.errors.NotFound:
            pass

    elif str(reaction.emoji) == '⚔️':
        player.strength += 1
        reply = "your strength is now lvl {}".format(player.strength)
        await message.channel.send(reply)
        player.money -= 300
        try:
            await shop_message.delete()
        except discord.errors.NotFound:
            pass

    elif str(reaction.emoji) == '❤️':
        player.health += 1
        reply = "your health is now lvl {}".format(player.health)
        await message.channel.send(reply)
        player.money -= 300
        try:
            await shop_message.delete()
        except discord.errors.NotFound:
            pass

    elif str(reaction.emoji) == '🛡':
        player.armor_penetration += 1
        reply = "your armor penetration is now lvl {}".format(player.armor_penetration)
        await message.channel.send(reply)
        player.money -= 300
        try:
            await shop_message.delete()
        except discord.errors.NotFound:
            pass