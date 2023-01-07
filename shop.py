import discord

client = discord.Client()

@client.event
async def on_reaction_add(reaction, user):
    # Check if the user is the bot itself
    if user == client.user:
        return

    # Check if the reaction is one of the three options
    if str(reaction.emoji) == "⚔️":
        # Upgrade damage
        pass
    elif str(reaction.emoji) == "🛡":
        # Upgrade defense
        pass
    elif str(reaction.emoji) == "💪":
        # Upgrade strength
        pass

client.run('your-bot-token-goes-here')
