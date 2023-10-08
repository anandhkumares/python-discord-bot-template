"""Contains constant such as embed colors, emojies"""
from dataclasses import dataclass
from discord import Color


@dataclass()
class EmbedColor:
    """Color values for emebed depending on circumstances."""

    DEFAULT_EMBED_COLOR = Color.from_rgb(43, 45, 39)


@dataclass()
class Emoji:
    """All emoji used by bots."""

    LATENCY = "<:latencygreen:1160516336003326002>"
    RAM = "<:ramgreen:1160529241188872202>"
    CPU = "<:cpu:1049656690787762196>"
    UPTIME = "<:uptime:1049655141877432362>"
