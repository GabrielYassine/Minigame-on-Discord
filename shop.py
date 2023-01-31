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
async def shop_open(client, message, player):
    reply = "Hello Summoner, you can choose to upgrade your Strength (300), Health (300), Armor penetration (300), or Movement speed (1000) (Movementspeed halves time use on each action). You currently have {} money.".format(player.money)
    shop_message = await message.channel.send(reply)
    await shop_message.add_reaction('⚔️')
    await shop_message.add_reaction('❤️')
    await shop_message.add_reaction('🛡')
    await shop_message.add_reaction('🏃')
    
    def check(reaction, user):
        return user == message.author and str(reaction.emoji) in ['⚔️', '❤️', '🛡', '🏃']
    
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        try:
            await shop_message.delete()
        except discord.errors.NotFound:
            pass
        
    if str(reaction.emoji) == '⚔️':
        if player.strength >= 5:
            reply = "Strength can only be upgraded to level 5."
            await message.channel.send(reply)
        else:
            player.strength += 1
            player.money -= 300
            reply = "your strength is now lvl {}, your new balance is {}".format(player.strength, player.money)
            await message.channel.send(reply)
    elif str(reaction.emoji) == '❤️':
        if player.health >= 5:
            reply = "Health can only be upgraded to level 5."
            await message.channel.send(reply)
        else:
            player.health += 1
            player.money -= 300
            reply = "your health is now lvl {}, your new balance is {}".format(player.health, player.money)
            await message.channel.send(reply)
    elif str(reaction.emoji) == '🛡':
        if player.armor_penetration >= 5:
            reply = "Armor penetration can only be upgraded to level 5."
            await message.channel.send(reply)
        else:
            player.armor_penetration += 1
            player.money -= 300
            reply = "your armor penetration is now lvl {}, your new balance is {}".format(player.armor_penetration, player.money)
            await message.channel.send(reply)
    elif str(reaction.emoji) == '🏃':
        if player.movement_speed >= 1:
            reply = "Movement speed can only be upgraded once."
            await message.channel.send(reply)
        else:
            player.movement_speed += 1
            player.money -= 1000
            reply = "your movement speed is now lvl {}, your new balance is {}".format(player.movement_speed, player.money)
            await message.channel.send(reply)
    try:
        await shop_message.delete()
    except discord.errors.NotFound:
        pass