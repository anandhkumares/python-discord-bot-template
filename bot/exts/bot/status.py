"""Status command"""
from time import time
from datetime import timedelta
from discord.ext import commands
from discord import ApplicationContext, Embed
from psutil import cpu_percent, virtual_memory
from bot.bot import Bot
from bot.constants import EmbedColor, Emoji


class Status(commands.Cog):
    """Subclass of Cog for status command

    Commands
    ---------
    status - returns latency, ram usage, cpu usage and uptime of the bot.
    """

    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.slash_command(
        name="status",
        description="Returns stats about bot.",
    )
    async def _command(self, ctx: ApplicationContext):
        # Gets stats
        latency = round(self.bot.latency * 1000)
        uptime = timedelta(seconds=round(time()) - self.bot.start_time)
        cpu_usage = cpu_percent()
        memory_usage = virtual_memory().percent

        # Creates embed with stats and reply with it
        embed = Embed(
            description=f"**Bot's Ping** {Emoji.LATENCY}\n{latency}ms\n"
            + f"**Cpu  Usage** {Emoji.CPU}\n{cpu_usage}%\n"
            + f"**Ram  Usage** {Emoji.RAM}\n{memory_usage}%\n"
            + f"**Last Down** {Emoji.UPTIME}\n{uptime}",
            color=EmbedColor.DEFAULT_EMBED_COLOR,
        )
        await ctx.respond(embed=embed)

        # Logs it for debug only
        self.bot.logger.debug(
            "Status command invoked by %s, info %s",
            ctx.author.name,
            (latency, uptime, cpu_usage, memory_usage),
        )

        # Returns of test purpose
        return (latency, uptime, cpu_usage, memory_usage)


def setup(bot: Bot):
    """Called by pycord to setup the cog."""
    bot.add_cog(Status(bot))
