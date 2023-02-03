import discord
import info
import Class
import Jungle
import Dragon
import shop
import Gank

Player_dict = {}
player = Class.Player(0,1,1,1,0,0,0,0)

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
                await info.start_game(message)
                player = Class.Player(1,1,1,1,0,0,0,0)
                Player_dict[member_id] = player

        else:
            commands = ["!help", "!gank", "!shop", "!dragon", "!jungle", "!surrender"]
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

############################

            if contents.startswith("!help"):
                await info.help(message)

####################################

            if contents.startswith("!gank"):
                await Gank.gank_lane(client, message, player)
                
####################################
                  
            if contents.startswith("!shop"):
                if player.money > 300:
                    await shop.shop_open(client, message, player)
                else:
                    await message.channel.send("You don't have enough gold to upgrade.")

###########################

            if contents.startswith("!dragon"):
                await Dragon.dragon_clear(message, player)

##############################

            if contents.startswith("!jungle"):
                await Jungle.jungle_clear(message, player)

###########################

            if contents.startswith("!surrender"):
                reply = "Imagine surrendering, Major L, uninstall life tbh skull emoji x7"
                await message.channel.send(reply)
                player.gamemode = 0

###########################

token = get_token()
client.run(token)
