import random
import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    contents = message.content

@bot.command()
async def maybe_do_something(ctx):
    # Generate a random float between 0 and 1
    probability = random.random()

    # If the probability is less than 0.6, perform the action
    if probability < 0.6:
        await ctx.send("Performing the action!")
    else:
        await ctx.send("Not performing the action.")
