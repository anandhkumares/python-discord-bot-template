"""Defines constants used all over the project."""
# Standard Libraries.
from dataclasses import dataclass

# pylint: disable=invalid-name


@dataclass
class InternalConstants:
    """Constants used for bot, not used by commands or other stuffs."""

    DOTENV_PATH: str = "../ .env"
    DISCORD_TOKEN_NAME: str = "DISCORD_TOKEN"
    EXTENSIONS_PATH: str = "bot/exts/"
