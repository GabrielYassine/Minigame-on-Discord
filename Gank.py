import discord
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    contents = message.content

@client.event
async def gank_lane(message, player):
    reply = "What lane do you want to have a go at?"
    gank_message = await message.channel.send(reply)
    await gank_message.add_reaction('⤴️')
    await gank_message.add_reaction('⬆️')
    await gank_message.add_reaction('⤵️')

    def check(reaction, user):
        return user == message.author and str(reaction.emoji) in ['⤴️', '⬆️', '⤵️']
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
        
    except asyncio.TimeoutError:
        try:
            await gank_message.delete()
        except discord.errors.NotFound:
            pass

    else:
        if str(reaction.emoji) == '⤴️':
            chance = 40 + player.strength * 4 *  + player.health * 2 + player.armor_penetration * 8
            reply = "you have chosen toplane, your chances of success are {}, are you sure you want to continue?".format(chance)
            confirm_message = await message.channel.send(reply)
            await confirm_message.add_reaction('✅')
            await confirm_message.add_reaction('🚫')
            
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ['✅', '🚫']
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
        
            except asyncio.TimeoutError:
                try:
                    await gank_message.delete()
                except discord.errors.NotFound:
                    pass

            if str(reaction.emoji) == '✅':
                player.time += 30
                random_number = random.randint(0, 100)
                if chance <= random_number:
                    random_number = random.randint(300, 400)
                    player.money += random_number
                    reply = "you have succesfully ganked toplane, new balance: {}".format(player.money)
                    await message.channel.send(reply)
                if random_number >= random_number:
                    reply = "you have unsuccesfully ganked botlane"
                await gank_message.delete()
            
            elif str(reaction.emoji) == '🚫':
                await confirm_message.delete()

        elif str(reaction.emoji) == '⬆️':
            chance = 40 + player.strength * 4 + player.health * 8 + player.armor_penetration * 2
            reply = "you have chosen midlane, your chances of success are {}, are you sure you want to continue?".format(chance)
            confirm_message = await message.channel.send(reply)
            await confirm_message.add_reaction('✅')
            await confirm_message.add_reaction('🚫')
            
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ['✅', '🚫']
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
        
            except asyncio.TimeoutError:
                try:
                    await gank_message.delete()
                except discord.errors.NotFound:
                    pass
                
            if str(reaction.emoji) == '✅':
                player.time += 30
                random_number = random.randint(0, 100)
                if chance <= random_number:
                    random_number = random.randint(300, 400)
                    player.money += random_number
                    reply = "you have succesfully ganked midlane, new balance: {}".format(player.money)
                    await message.channel.send(reply)
                if random_number >= random_number:
                    reply = "you have unsuccesfully ganked midlane"
                await gank_message.delete()

            elif str(reaction.emoji) == '🚫':
                await confirm_message.delete()

        elif str(reaction.emoji) == '⤵️':
            chance = 40 + player.strength * 2 + player.health * 2+ player.armor_penetration * 4
            reply = "you have chosen botlane, your chances of success are {}, are you sure you want to continue?".format(chance)
            confirm_message = await message.channel.send(reply)
            await confirm_message.add_reaction('✅')
            await confirm_message.add_reaction('🚫')
            
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ['✅', '🚫']
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
        
            except asyncio.TimeoutError:
                try:
                    await gank_message.delete()
                except discord.errors.NotFound:
                    pass
                
            if str(reaction.emoji) == '✅':
                player.time += 30
                random_number = random.randint(0, 100)
                if chance <= random_number:
                    random_number = random.randint(300, 400)
                    player.money += random_number
                    reply = "you have succesfully ganked botlane, new balance: {}".format(player.money)
                    await message.channel.send(reply)
                if random_number >= random_number:
                    reply = "you have unsuccesfully ganked botlane,"
                await gank_message.delete()

            elif str(reaction.emoji) == '🚫':
                await confirm_message.delete()