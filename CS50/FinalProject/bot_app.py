import logging
# Import the command handler
import lightbulb
import os


# Create instance of a bot and set to debug for both lightbulb and hikari
# TODO: change placeholder to os usage
bot = lightbulb.Bot(token="<placeholder>", prefix="<placeholder>", logs="DEBUG")


# Silly bot command definition 
# TODO: redo this with slash commands
@bot.command()
async def ping(ctx):
    # Send a message to the channel the command was used in
    await ctx.respond("Pong!")


# Run the bot
bot.run()