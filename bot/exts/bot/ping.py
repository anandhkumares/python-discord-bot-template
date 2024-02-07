"""A basic ping command"""

# Third Party Libraries.
import discord
from discord.ext import commands
from discord import app_commands
from bot.bot import Bot

# Project Modules.
from bot.constants import EmbedColor, Emoji
from bot.log import get_logger

# Logging
logger = get_logger(__name__)


class Ping(commands.Cog):
    """Subclass of Cog for ping command

    Commands
    ---------
    ping - returns latency of bot.
    """

    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot = bot

    @app_commands.command(name="ping", description="Check bot response time.")  # type: ignore
    async def _command(self, interaction: discord.Interaction):
        # Creates embed with latency and responds
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            description=f"**Pong!** {latency}ms {Emoji.LATENCY}",
            color=EmbedColor.DEFAULT_EMBED_COLOR,
        )

        await interaction.response.send_message(embed=embed)

        logger.debug(
            "Ping command invoked by %s, current latency is %sms",
            interaction.user.id,
            latency,
        )

        # returns for test purposes
        return latency


async def setup(bot: Bot):
    """Called by discord.py to setup the cog."""
    await bot.add_cog(Ping(bot))
