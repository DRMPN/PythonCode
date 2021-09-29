import logging
# Import the command handler
import lightbulb
# Import slash commands submodule 
from lightbulb import slash_commands
import os


# Create instance of a bot and set to debug for both lightbulb and hikari
# TODO: add more parameters
bot = lightbulb.Bot(token=os.environ.get("DISCORD_BOT_TOKEN"), prefix="DisBot", logs="DEBUG")


class Foo(slash_commands.SlashCommandGroup):
    description = "Test slash command group."


@Foo.subcommand()
class Bar(slash_commands.SlashSubCommand):
    description = "Test subcommand."
    # Options
    baz: str = slash_commands.Option("Test subcommand option.")

    async def callback(self, context):
        await context.respond(context.options.baz)

@Foo.subcommand()
class Baz(slash_commands.SlashSubCommand):
    description = "Test subcommand 2."
    # Options
    bak: str = slash_commands.Option("Test subcommand option 2.")

    async def callback(self, context):
        await context.respond(context.options.bak)


# Add the slash command to the bot
bot.add_slash_command(Foo)


# Run the bot
bot.run()