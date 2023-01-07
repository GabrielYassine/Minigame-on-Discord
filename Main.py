
import discord
import info

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

#BILLEDE SKAL POSTES NÅR SPILLET STARTER, samt ændre en variable fra 0 til 1.
    if contents.startswith("!start"):
        rem = contents[1:]
        if rem == "start":
            global gamemode
            if gamemode == 1:
                reply = "You are already in a game"
                await message.channel.send(reply)
            if gamemode == 0:
                await info.start_game(message)
                gamemode = 1

    #liste af mulige commands.
    if contents.startswith("!help"):
        rem = contents[1:]
        if rem == "help":
            await info.help(message)
            
    #Man skal kunne bruge shop når som helst og opgrade sine stats med penge.
    if contents.startswith("!shop"):
        rem = contents[1:]
        reply = rem
        await message.channel.send(reply)
    
    #ADD 1-3 FORSKELLIGE COMMANDS TIL ALLE LANES, kan bruges når som helst.
    if contents.startswith("!gank"):
        if gamemode == 1:
            rem = contents[1:]
            reply = rem
            await message.channel.send(reply)

    #Nogle kriterier i forhold til stats skal opfyldes før man kan skrive denne command.
    if contents.startswith("!drake"):
        rem = contents[1:]
        if rem == "drake":
            if gamemode == 1:
                global kills
                if kills == 0:
                    if health >= 2 and strength >= 2 and armor_penetration >= 2:
                        reply = "you have succesfully killed the first dragon"
                        kills += 1
                if kills == 1:
                    if health >= 3 and strength >= 3 and armor_penetration >= 3:
                        reply = "you have succesfully killed the second dragon"
                        kills +=1
                if kills == 2:
                    if health >= 4 and strength >= 4 and armor_penetration >= 4:
                        reply = "you have succesfully killed the third dragon"
                        kills +=1
                if kills == 3:
                    if health >= 5 and strength >= 5 and armor_penetration >= 5:
                        reply = "you have succesfully killed the fourth dragon"
                        kills +=1
            if gamemode == 0:
                reply = "this command can only be used while a game is active."
                await message.channel.send(reply)


        await message.channel.send(reply)
    
    #ADD 1-4 FORSKELLIGE COMMANDS TIL JUNGLE, kan bruges når som helst.
    if contents.startswith("!jungle"):
        rem = contents[1:]
        if rem == "jungle":
            if gamemode == 1:
                global money
                money += 100
                reply = "you have cleared the jungle, new balance: {}".format(money)
                await message.channel.send(reply)
            if gamemode == 0:
                reply = "this command can only be used while a game is active."
                await message.channel.send(reply)
            
    
    #skal force end et spil og skal kun kunne anvendes når man er i et spil og ændrer gamemode fra 1 til 0.
    if contents.startswith("!surrender"):
        rem = contents[1:]
        if rem == "surrender":
            if gamemode == 0:
                reply = "You arent in a game yet"
                await message.channel.send(reply)
            if gamemode == 1:
                reply = "Imagine surrendering, Major L, uninstall life tbh skull emoji x7"
                await message.channel.send(reply)
                global time
                money = 0
                time = 0
                gamemode = 0
            
    #FIND UD AF OM LEADERBORD SKAL TILFØJES
    # if contents.startswith("!leaderboard"):
    #     rem = contents[1:]
    #     reply = rem
    #     await message.channel.send(reply)

    # else:
    #     reply = "Error, Unknown input, type !help to see the available commands"
    #     await message.channel.send(reply)

token = get_token()
client.run(token)
