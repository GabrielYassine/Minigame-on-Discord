import discord
import Info
import asyncio
import random
import Class
import Jungle
import Drake
import Shop
import Gank

Player_dict = {}
player = Class.Player(0,1,1,1,0,0,0)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

@client.event
async def on_ready():
    print("Connected!")

@client.event
async def on_member_join(member):
    global player
    player = Class.Player()
    Player_dict[member.id] = player

@client.event
async def on_message(message):
    global player
    contents = message.content
    member_id = message.author.id
    if contents.startswith("!test"):
        if member_id not in Player_dict:
            player = Class.Player()
            Player_dict[member_id] = player
            reply = "you are registered"
            await message.channel.send(reply)

###################################

    if player.gamemode == 0:

###########################

        if contents.startswith("!play"):
            if message.author.id in Player_dict:
                await Info.start_game(message)
                player.gamemode = 1
        else:
            commands = ["!help", "!gank", "!shop", "!drake", "!jungle", "!surrender"]
            if contents.startswith(tuple(commands)):
                reply = "You are currently not in an active game"
                await message.channel.send(reply)

###########################

    if player.gamemode == 1:
        if message.author.id in Player_dict:
            player = Player_dict[message.author.id]
    
###########################

            if contents.startswith("!admin"):
                player.strength = 5
                player.health = 5
                player.armor_penetration = 5
                player.money = 5000
                reply = "admin mode activated"
                await message.channel.send(reply)
            
            if contents.startswith("!help"):
                await Info.help(message)

####################################

            if contents.startswith("!gank"):
                await Gank.gank_lane(message, player)
                # reply = "What lane do you want to have a go at?"
                # gank_message = await message.channel.send(reply)
                # await gank_message.add_reaction('⤴️')
                # await gank_message.add_reaction('⬆️')
                # await gank_message.add_reaction('⤵️')

                # def check(reaction, user):
                #     return user == message.author and str(reaction.emoji) in ['⤴️', '⬆️', '⤵️']
                # try:
                #     reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
                    
                # except asyncio.TimeoutError:
                #     try:
                #         await gank_message.delete()
                #     except discord.errors.NotFound:
                #         pass

                # else:
                #     if str(reaction.emoji) == '⤴️':
                #         chance = 40 + player.strength * 4 *  + player.health * 2 + player.armor_penetration * 8
                #         reply = "you have chosen toplane, your chances of success are {}, are you sure you want to continue?".format(chance)
                #         confirm_message = await message.channel.send(reply)
                #         await confirm_message.add_reaction('✅')
                #         await confirm_message.add_reaction('🚫')
                        
                #         def check(reaction, user):
                #             return user == message.author and str(reaction.emoji) in ['✅', '🚫']
                #         try:
                #             reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
                    
                #         except asyncio.TimeoutError:
                #             try:
                #                 await gank_message.delete()
                #             except discord.errors.NotFound:
                #                 pass

                #         if str(reaction.emoji) == '✅':
                #             player.time += 30
                #             random_number = random.randint(0, 100)
                #             if chance <= random_number:
                #                 random_number = random.randint(300, 400)
                #                 player.money += random_number
                #                 reply = "you have succesfully ganked toplane, new balance: {}".format(player.money)
                #                 await message.channel.send(reply)
                #             if random_number >= random_number:
                #                 reply = "you have unsuccesfully ganked botlane"
                #             await gank_message.delete()
                        
                #         elif str(reaction.emoji) == '🚫':
                #             await confirm_message.delete()

                #     elif str(reaction.emoji) == '⬆️':
                #         chance = 40 + player.strength * 4 + player.health * 8 + player.armor_penetration * 2
                #         reply = "you have chosen midlane, your chances of success are {}, are you sure you want to continue?".format(chance)
                #         confirm_message = await message.channel.send(reply)
                #         await confirm_message.add_reaction('✅')
                #         await confirm_message.add_reaction('🚫')
                        
                #         def check(reaction, user):
                #             return user == message.author and str(reaction.emoji) in ['✅', '🚫']
                #         try:
                #             reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
                    
                #         except asyncio.TimeoutError:
                #             try:
                #                 await gank_message.delete()
                #             except discord.errors.NotFound:
                #                 pass
                            
                #         if str(reaction.emoji) == '✅':
                #             player.time += 30
                #             random_number = random.randint(0, 100)
                #             if chance <= random_number:
                #                 random_number = random.randint(300, 400)
                #                 player.money += random_number
                #                 reply = "you have succesfully ganked midlane, new balance: {}".format(player.money)
                #                 await message.channel.send(reply)
                #             if random_number >= random_number:
                #                 reply = "you have unsuccesfully ganked midlane"
                #             await gank_message.delete()
            
                #         elif str(reaction.emoji) == '🚫':
                #             await confirm_message.delete()

                #     elif str(reaction.emoji) == '⤵️':
                #         chance = 40 + player.strength * 2 + player.health * 2+ player.armor_penetration * 4
                #         reply = "you have chosen botlane, your chances of success are {}, are you sure you want to continue?".format(chance)
                #         confirm_message = await message.channel.send(reply)
                #         await confirm_message.add_reaction('✅')
                #         await confirm_message.add_reaction('🚫')
                        
                #         def check(reaction, user):
                #             return user == message.author and str(reaction.emoji) in ['✅', '🚫']
                #         try:
                #             reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
                    
                #         except asyncio.TimeoutError:
                #             try:
                #                 await gank_message.delete()
                #             except discord.errors.NotFound:
                #                 pass
                            
                #         if str(reaction.emoji) == '✅':
                #             player.time += 30
                #             random_number = random.randint(0, 100)
                #             if chance <= random_number:
                #                 random_number = random.randint(300, 400)
                #                 player.money += random_number
                #                 reply = "you have succesfully ganked botlane, new balance: {}".format(player.money)
                #                 await message.channel.send(reply)
                #             if random_number >= random_number:
                #                 reply = "you have unsuccesfully ganked botlane,"
                #             await gank_message.delete()

                #         elif str(reaction.emoji) == '🚫':
                #             await confirm_message.delete()

####################################
                  
            if contents.startswith("!shop"):
                await Shop.shop_open(message, player)
                # reply = "Hello Summoner, you can choose to upgrade your Strength, Health or Armor penetration, you currently have {} money".format(player.money)
                # shop_message = await message.channel.send(reply)
                # await shop_message.add_reaction('⚔️')
                # await shop_message.add_reaction('❤️')
                # await shop_message.add_reaction('🛡')

                # def check(reaction, user):
                #     return user == message.author and str(reaction.emoji) in ['⚔️', '❤️', '🛡']
                
                # try:
                #     reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
                    
                # except asyncio.TimeoutError:
                #     try:
                #         await shop_message.delete()
                #     except discord.errors.NotFound:
                #         pass

                # if player.money < 300:
                #     await message.channel.send("You don't have enough money to upgrade.")
                #     try:
                #         await shop_message.delete()
                #     except discord.errors.NotFound:
                #         pass

                # elif str(reaction.emoji) == '⚔️':
                #     player.strength += 1
                #     reply = "your strength is now lvl {}".format(player.strength)
                #     await message.channel.send(reply)
                #     player.money -= 300
                #     try:

                #         await shop_message.delete()
                #         if player.money > 300:
                #             await message.channel.send("!shop")

                #     except discord.errors.NotFound:
                #         pass

                # elif str(reaction.emoji) == '❤️':
                #     player.health += 1
                #     reply = "your health is now lvl {}".format(player.health)
                #     await message.channel.send(reply)
                #     player.money -= 300
                #     try:
                #         await shop_message.delete()
                #     except discord.errors.NotFound:
                #         pass

                # elif str(reaction.emoji) == '🛡':
                #     player.armor_penetration += 1
                #     reply = "your armor penetration is now lvl {}".format(player.armor_penetration)
                #     await message.channel.send(reply)
                #     player.money -= 300
                #     try:
                #         await shop_message.delete()
                #     except discord.errors.NotFound:
                #         pass

###########################

            if contents.startswith("!drake"):
                await Drake.drake_clear(message, player)

##############################

            if contents.startswith("!jungle"):
                await Jungle.jungle_clear(message, player)

###########################

            if contents.startswith("!surrender"):
                reply = "Imagine surrendering, Major L, uninstall life tbh skull emoji x7"
                await message.channel.send(reply)

###########################

token = get_token()
client.run(token)
