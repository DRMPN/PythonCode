import logging
# Import the command handler
import lightbulb
# Import slash commands submodule 
from lightbulb import slash_commands
import os


# Set the logging level
logging.basicConfig(level=logging.INFO)


# Create instance of a bot and set to debug for both lightbulb and hikari
# TODO: add more parameters
bot = lightbulb.Bot(token=os.environ.get("DISCORD_BOT_TOKEN"), prefix="DisBot", logs="DEBUG")


# Test slash command group
class Foo(slash_commands.SlashCommandGroup):
    description = "Test slash command group."


# Test subcommand #1
@Foo.subcommand()
class Bar(slash_commands.SlashSubCommand):
    description = "Test subcommand one."
    # Options
    baz: str = slash_commands.Option("Test subcommand option one.")

    async def callback(self, context):
        await context.respond(context.options.baz)


# Test subcommand #2
@Foo.subcommand()
class Baz(slash_commands.SlashSubCommand):
    description = "Test subcommand two."
    # Options
    bak: str = slash_commands.Option("Test subcommand option two.")

    async def callback(self, context):
        await context.respond(context.options.bak)


# Add the slash command group to the bot
bot.add_slash_command(Foo)


# Run the bot
bot.run()