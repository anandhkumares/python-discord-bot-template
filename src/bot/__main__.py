"""Executes when bot package runs."""
from os import getenv
from discord import Intents
from dotenv import load_dotenv

from bot.bot import Bot

load_dotenv()
TOKEN = getenv("TOKEN")

bot = Bot(
    command_prefix="!",
    intents=Intents.none(),
    help_command=None,
)
bot.run(TOKEN)
