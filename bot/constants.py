"""Defines constants used all over the project."""

# Standard Libraries.
import dataclasses

# pylint: disable=invalid-name


@dataclasses.dataclass
class InternalConstants:
    """Constants used for bot, not used by commands or other stuffs."""

    DOTENV_PATH: str = ".env"
    DISCORD_TOKEN_NAME: str = "DISCORD_TOKEN"
    LOG_LEVEL_NAME: str = "LOG_LEVEL"
    EXTENSIONS_PATH: str = "bot/exts/"
