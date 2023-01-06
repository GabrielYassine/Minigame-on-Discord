
import discord
import funktioner

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
            await funktioner.start_game(message)

    #FIND UD AF OM LEADERBORD SKAL TILFØJES
    if contents.startswith("!leaderboard"):
        rem = contents[1:]
        reply = rem
        await message.channel.send(reply)
    
    #Man skal kunne bruge shop når som helst og opgrade sine stats med penge.
    if contents.startswith("!shop"):
        rem = contents[1:]
        reply = rem
        await message.channel.send(reply)
    
    #ADD 1-3 FORSKELLIGE COMMANDS TIL ALLE LANES, kan bruges når som helst.
    if contents.startswith("!gank"):
        rem = contents[1:]
        reply = rem
        await message.channel.send(reply)

    #Nogle kriterier i forhold til stats skal opfyldes før man kan skrive denne command.
    if contents.startswith("!drake"):
        rem = contents[1:]
        reply = rem
        await message.channel.send(reply)
    
    #ADD 1-4 FORSKELLIGE COMMANDS TIL JUNGLE, kan bruges når som helst.
    if contents.startswith("!jungle"):
        rem = contents[1:]
        reply = rem
        await message.channel.send(reply)

token = get_token()
client.run(token)
