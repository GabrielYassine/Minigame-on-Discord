import discord
import info
import asyncio
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    contents = message.content

async def shop(message):
    if gamemode == 1:
        if contents.startswith("!shop"):
            rem = contents[1:]
            global money
            global strength
            global health
            global armor_penetration
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
    