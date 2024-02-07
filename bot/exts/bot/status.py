"""Status command"""

# Standard Libraries.
from time import time
from datetime import timedelta
from venv import logger

# Third Party Libraries.
import discord
from discord import app_commands
from discord.ext import commands
from psutil import cpu_percent, virtual_memory

# Project Modules.
from bot.bot import Bot
from bot.constants import EmbedColor, Emoji
from bot.log import get_logger

# Logging
logger = get_logger(__name__)


class Status(commands.Cog):
    """Subclass of Cog for status command

    Commands
    ---------
    status - returns latency, ram usage, cpu usage and uptime of the bot.
    """

    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot = bot

    @app_commands.command(name="status", description="Returns stats about bot.")  # type: ignore
    async def _command(self, interaction: discord.Interaction):
        # Gets stats
        latency = round(self.bot.latency * 1000)
        uptime = timedelta(seconds=round(time()) - self.bot.start_time)
        cpu_usage = cpu_percent()
        memory_usage = virtual_memory().percent

        # Creates embed with stats and reply with it
        embed = discord.Embed(
            description=f"**Bot's Ping** {Emoji.LATENCY}\n{latency}ms\n"
            + f"**Cpu  Usage** {Emoji.CPU}\n{cpu_usage}%\n"
            + f"**Ram  Usage** {Emoji.RAM}\n{memory_usage}%\n"
            + f"**Last Down** {Emoji.UPTIME}\n{uptime}",
            color=EmbedColor.DEFAULT_EMBED_COLOR,
        )
        await interaction.response.send_message(embed=embed)

        # Logs it for debug only
        logger.debug(
            "Status command invoked by %s, info %s",
            interaction.user.id,
            (latency, uptime, cpu_usage, memory_usage),
        )

        # Returns of test purpose
        return (latency, uptime, cpu_usage, memory_usage)


async def setup(bot: Bot):
    """Called by pycord to setup the cog."""
    await bot.add_cog(Status(bot))
