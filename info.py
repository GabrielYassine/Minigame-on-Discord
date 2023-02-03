import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def start_game(message):
    reply = "Welcome To League of Speed!\n"
    reply += "This game is about defeating a total of 4 dragons in the shortest possible time.\n"
    reply += "The first dragon requirement is level 2 of strength, health and armor penetration. \n"
    reply += "Each time you defeat a dragon, you recieve some gold and the requirements rise by 1 level on each stat. \n"
    reply += "You can choose between ganking the different lanes or defeating the monsters in the jungle to obtain gold.\n"
    reply += "You can spend gold in the shop to upgrade your stats, to higher your ganking sucessrate, clear speed, and to defeat the drakes.\n"
    reply += "Strength, health and armor penetration upgrades cost 300 while movement speed costs 1000 \n"
    reply += "You can at any point in the game type !help, to see the different commands that are available. Now Enjoy!"
    await message.channel.send(reply, file=discord.File('map.jpg'))

async def help(message):
    reply = "While playing League of Speed, you can perform various action by using different commands:\n"
    reply += "!start is used to start up a game, and can only be performed if a game isnt active.\n"
    reply += "!surrender is used to force end a game.\n"
    reply += "!shop is used to upgrade your stats, and can be accessed at anytime.\n"
    reply += "!gank is an action you can perform to gain gold, ganking is always a gamble, and will have a higher success rate the better your stats are. To gank a lane, you need to follow up !gank with the specific lane you wnat to gank.\n"
    reply += "!jungle is an an action you can perform to gain gold, its a safe way to obtain gold but deffinetly not as much as successfull ganks.\n"
    reply += "!dragon is an action you need to perform 4 times in order to win. The command can be called successfully whenever your stats fit the requirements.\n"
    await message.channel.send(reply)
