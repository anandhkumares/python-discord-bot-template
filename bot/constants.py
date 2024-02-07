"""Defines constants used all over the project."""

# Standard Libraries.
import dataclasses

# External Libraries.
from discord import Color

# pylint: disable=invalid-name


@dataclasses.dataclass
class InternalConstants:
    """Constants used for bot, not used by commands or other stuffs."""

    DOTENV_PATH: str = ".env"
    DISCORD_TOKEN_NAME: str = "DISCORD_TOKEN"
    LOG_LEVEL_NAME: str = "LOG_LEVEL"
    EXTENSIONS_PATH: str = "bot/exts/"


@dataclasses.dataclass()
class EmbedColor:
    """Color values for emebed depending on circumstances."""

    DEFAULT_EMBED_COLOR = Color.from_rgb(43, 45, 39)


@dataclasses.dataclass()
class Emoji:
    """All emoji used by bots."""

    LATENCY = "<:latencygreen:1160516336003326002>"
    RAM = "<:ramgreen:1160529241188872202>"
    CPU = "<:cpu:1049656690787762196>"
    UPTIME = "<:uptime:1049655141877432362>"
