"""Executes when bot package runs."""
from os import getenv
from discord import Intents
from dotenv import load_dotenv

from bot.bot import Bot
from bot.log import setup_logger

load_dotenv()

# Setups logger
LOG_LEVEL = getenv("LOG_LEVEL")
setup_logger(LOG_LEVEL)


# Starts the bot
TOKEN = getenv("TOKEN")
bot = Bot(
    command_prefix="!",
    intents=Intents.none(),
    help_command=None,
)
bot.run(TOKEN)
