"""Executes when bot package runs."""

# Standard Libraries.
import os
import logging


# Third Party Libraries.
import discord
import dotenv

# Project Modules.
from bot.bot import Bot
from bot.constants import InternalConstants
from bot.log import setup_logger, get_logger

# Get secrets
dotenv.load_dotenv(InternalConstants.DOTENV_PATH, override=True)
LOG_LEVEL = os.getenv(InternalConstants.LOG_LEVEL_NAME)
DISCORD_TOKEN = os.getenv(InternalConstants.DISCORD_TOKEN_NAME)

# Logging
setup_logger(LOG_LEVEL)
log = get_logger(__name__)

if DISCORD_TOKEN is not None:
    # Starts the bot.
    bot = Bot(command_prefix="!", intents=discord.Intents.none(), help_command=None)
    bot.run(DISCORD_TOKEN, log_handler=None, log_level=logging.CRITICAL)
else:
    log.error("Discord Token is none bot exiting")
