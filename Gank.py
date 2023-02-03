import discord
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def gank_lane(client, message, player):
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

#######################

    else:
        if str(reaction.emoji) == '⤴️':
            chance = 40 + player.strength * 2 + player.health * 1 + player.armor_penetration * 4
            reply = f"you have chosen toplane, your chances of success are {chance}, are you sure you want to continue?"
            confirm_message = await message.channel.send(reply)
            await confirm_message.add_reaction('✅')
            await confirm_message.add_reaction('🚫')
            try:
                await gank_message.delete()
            except discord.errors.NotFound:
                pass
            
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ['✅', '🚫']
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
        
            except asyncio.TimeoutError:
                try:
                    await confirm_message.delete()
                except discord.errors.NotFound:
                    pass

            if str(reaction.emoji) == '✅':
                if player.movement_speed == 1:
                    player.time += 15
                else:
                    player.time += 30
                random_number = random.randint(0, 100)
                if random_number <= chance:
                    random_number = random.randint(300, 400)
                    player.money += random_number
                    reply = f"you have succesfully ganked toplane, new balance: {player.money} gold."
                    await message.channel.send(reply)
                else:
                    reply = "you have unsuccesfully ganked botlane."
                    await message.channel.send(reply)
                try:
                    await confirm_message.delete()
                except discord.errors.NotFound:
                    pass

        elif str(reaction.emoji) == '🚫':
            try:
                await confirm_message.delete()
            except discord.errors.NotFound:
                pass

#######################

        elif str(reaction.emoji) == '⬆️':
            chance = 40 + player.strength * 2 + player.health * 4 + player.armor_penetration * 1
            reply = f"you have chosen midlane, your chances of success are {player.chance}, are you sure you want to continue?"
            confirm_message = await message.channel.send(reply)
            await confirm_message.add_reaction('✅')
            await confirm_message.add_reaction('🚫')
            try:
                await gank_message.delete()
            except discord.errors.NotFound:
                pass
            
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ['✅', '🚫']
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
        
            except asyncio.TimeoutError:
                try:
                    await confirm_message.delete()
                except discord.errors.NotFound:
                    pass
                
            if str(reaction.emoji) == '✅':
                if player.movement_speed == 1:
                    player.time += 15
                else:
                    player.time += 30
                random_number = random.randint(0, 100)
                if random_number <= chance:
                    random_number = random.randint(300, 400)
                    player.money += random_number
                    reply = f"you have succesfully ganked toplane, new balance: {player.money} gold."
                    await message.channel.send(reply)
                else:
                    reply = "you have unsuccesfully ganked botlane."
                    await message.channel.send(reply)
                try:
                    await confirm_message.delete()
                except discord.errors.NotFound:
                    pass

            elif str(reaction.emoji) == '🚫':
                try:
                    await confirm_message.delete()
                except discord.errors.NotFound:
                    pass

#######################

        elif str(reaction.emoji) == '⤵️':
            chance = 40 + player.strength * 4 + player.health * 1 + player.armor_penetration * 2
            reply = f"you have chosen botlane, your chances of success are {player.chance}, are you sure you want to continue?"
            confirm_message = await message.channel.send(reply)
            await confirm_message.add_reaction('✅')
            await confirm_message.add_reaction('🚫')
            try:
                await gank_message.delete()
            except discord.errors.NotFound:
                pass
            
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ['✅', '🚫']
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
        
            except asyncio.TimeoutError:
                try:
                    await confirm_message.delete()
                except discord.errors.NotFound:
                    pass
                
            if str(reaction.emoji) == '✅':
                if player.movement_speed == 1:
                    player.time += 15
                else:
                    player.time += 30
                random_number = random.randint(0, 100)
                if random_number <= chance:
                    random_number = random.randint(300, 400)
                    player.money += random_number
                    reply = f"you have succesfully ganked toplane, new balance: {player.money} gold."
                    await message.channel.send(reply)
                else:
                    reply = "you have unsuccesfully ganked botlane."
                    await message.channel.send(reply)
                try:
                    await confirm_message.delete()
                except discord.errors.NotFound:
                    pass

        elif str(reaction.emoji) == '🚫':
            try:
                await confirm_message.delete()
            except discord.errors.NotFound:
                pass