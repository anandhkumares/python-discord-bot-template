"""Executes when bot package runs."""
# Standard Libraries.
import os

# Third Party Libraries.
import discord
import dotenv

# Project Modules.
from bot.bot import Bot
from bot.constants import InternalConstants

# Get secrets.
dotenv.load_dotenv(InternalConstants.DOTENV_PATH)
DISCORD_TOKEN = os.getenv(InternalConstants.DISCORD_TOKEN_NAME)

if DISCORD_TOKEN is not None:
    # Starts the bot.
    bot = Bot(command_prefix="!", intents=discord.Intents.none(), help_command=None)
    bot.run(DISCORD_TOKEN)
else:
    print("Discord Token is none bot exiting")
