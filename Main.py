import discord
import info
import asyncio
import random
import Class

Player_dict = {}

gamemode = 0
time = 0
money = 0
kills = 0
strength = 1
armor_penetration = 1
health = 1

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
async def on_message(message):
    contents = message.content
    global gamemode
    if gamemode == 0:

#BILLEDE SKAL POSTES NÅR SPILLET STARTER, samt ændre en variable fra 0 til 1.
        if contents.startswith("!play"):
            async def on_member_join(member):
                player = player(1,1,1,0,0,0)
                Player_dict[member.id] = player
                global gamemode
                await info.start_game(message)
                gamemode = 1

    if gamemode == 1:
        if message.author.id in Player_dict:
            player = Player_dict[message.author.id]

        #liste af mulige commands.
            if contents.startswith("!help"):
                rem = contents[1:]
                if rem == "help":
                    await info.help(message)

            #Shop funktionen        
            if contents.startswith("!shop"):
                global money
                global strength
                global health
                global armor_penetration
                rem = contents[1:]
                if rem == "shop":
                    reply = "Hello Summoner, you can choose to upgrade your Strength, Health or Armor penetration, you currently have {} money".format(money)
                    shop_message = await message.channel.send(reply)
                    await shop_message.add_reaction('⚔️')  # Emoji for strength
                    await shop_message.add_reaction('❤️')  # Emoji for health
                    await shop_message.add_reaction('🛡')  # Emoji for armor penetration

                    def check(reaction, user):
                        return user == message.author and str(reaction.emoji) in ['⚔️', '❤️', '🛡']
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
                        
                    except asyncio.TimeoutError:
                        try:
                            await shop_message.delete()  # Delete the shop message
                        except discord.errors.NotFound:
                            pass  # Do nothing if the message has already been deleted

                    else:
                        if money < 300:  # Check if the user has enough money
                            await message.channel.send("You don't have enough money to upgrade.")
                            try:
                                await shop_message.delete()  # Delete the shop message
                            except discord.errors.NotFound:
                                pass  # Do nothing if the message has already been deleted

                        elif str(reaction.emoji) == '⚔️':
                            # Upgrade strength
                            strength += 1
                            reply = "your strength is now lvl {}".format(strength)
                            await message.channel.send(reply)
                            money -= 300  # Deduct the cost from the user's money
                            try:

                                await shop_message.delete()  # Delete the shop message
                                if money > 300:
                                    await message.channel.send("!shop")

                            except discord.errors.NotFound:
                                pass  # Do nothing if the message has already been deleted

                        elif str(reaction.emoji) == '❤️':
                            health += 1
                            reply = "your health is now lvl {}".format(health)
                            await message.channel.send(reply)
                            money -= 300  # Deduct the cost from the user's money
                            try:
                                await shop_message.delete()  # Delete the shop message
                            except discord.errors.NotFound:
                                pass  # Do nothing if the message has already been deleted

                        elif str(reaction.emoji) == '🛡':
                            # Upgrade armor penetration
                            armor_penetration += 1
                            reply = "your armor penetration is now lvl {}".format(armor_penetration)
                            await message.channel.send(reply)
                            money -= 300  # Deduct the cost from the user's money
                            try:
                                await shop_message.delete()  # Delete the shop message
                            except discord.errors.NotFound:
                                pass  # Do nothing if the message has already been deleted


            #ADD 1-3 FORSKELLIGE COMMANDS TIL ALLE LANES, kan bruges når som helst.
            if contents.startswith("!gank"):
                if gamemode == 1:
                    rem = contents[1:]
                    if rem == "gank":
                        reply = "you have ganked"
                        
                    await message.channel.send(reply)

        #Nogle kriterier i forhold til stats skal opfyldes før man kan skrive denne command.
            if contents.startswith("!drake"):
                rem = contents[1:]
                if rem == "drake":
                    if gamemode == 1:
                        global kills
                        if kills == 0:
                            if health >= 2+kills and strength >= 2+kills and armor_penetration >= 2+kills:
                                reply = "you have succesfully killed the third dragon"
                                await message.channel.send(reply)
                                kills += 1
                        if kills == 1:
                            if health >= 3 and strength >= 3 and armor_penetration >= 3:
                                reply = "you have succesfully killed the second dragon"
                                await message.channel.send(reply)
                                kills +=1
                        if kills == 2:
                            if health >= 4 and strength >= 4 and armor_penetration >= 4:
                                reply = "you have succesfully killed the third dragon"
                                await message.channel.send(reply)
                                kills +=1
                        if kills == 3:
                            if health >= 5 and strength >= 5 and armor_penetration >= 5:
                                reply = "you have succesfully killed the fourth dragon"
                                await message.channel.send(reply)
                                kills +=1
                                # add at man vinder, game ender, og time bliver gemt til user id. Du skal nok bruge en dictionary.
                    if gamemode == 0:
                        reply = "this command can only be used while a game is active."
                        await message.channel.send(reply)

        #ADD 1-4 FORSKELLIGE COMMANDS TIL JUNGLE, kan bruges når som helst.
            if contents.startswith("!jungle"):
                rem = contents[1:]
                if rem == "jungle":
                    random_number = random.randint(100, 200)
                    money += random_number
                    reply = "you have cleared the jungle, new balance: {}".format(money)
                    await message.channel.send(reply)
                    
                
        #skal force end et spil og skal kun kunne anvendes når man er i et spil og ændrer gamemode fra 1 til 0.
            if contents.startswith("!surrender"):
                rem = contents[1:]
                if rem == "surrender":
                    reply = "Imagine surrendering, Major L, uninstall life tbh skull emoji x7"
                    await message.channel.send(reply)
                    global time
                    money = 0
                    time = 0
                    gamemode = 0

token = get_token()
client.run(token)
