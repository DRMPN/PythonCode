import logging
# Import the command handler
import lightbulb
# Import slash commands submodule 
from lightbulb import slash_commands
import os


# Create instance of a bot and set to debug for both lightbulb and hikari
# TODO: add more parameters
bot = lightbulb.Bot(token=os.environ.get("DISCORD_BOT_TOKEN"), prefix="DisBot", logs="DEBUG")


# Silly bot command definition 
class Echo(slash_commands.SlashCommand):
    description = "Repeats your input."
    # Options
    text: str = slash_commands.Option("Text to repeat")

    async def callback(self, context):
        await context.respond(context.options.text)


# Add the slash command to the bot
bot.add_slash_command(Echo)


# Run the bot
bot.run()