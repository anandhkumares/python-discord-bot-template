"""Configs for logging and handlers."""

# Standard Libraries
import dataclasses
import logging
import pathlib


@dataclasses.dataclass
class TimeDuration:
    """Enumeration representing time units for TimedRotationHandler.

    Attributes:
    SECONDS
        Unit representing "s" in handler.
    MINUTES
        Unit representing "m" in handler.
    HOURS
        Unit representing "h" in handler.
    DAYS
        Unit reprenting "d" in handler.
    """

    SECONDS = "s"
    MINUTES = "m"
    HOURS = "h"
    DAYS = "d"


@dataclasses.dataclass
class TimedRotatingFileHandlerConfig:
    """Config for TimedRotatingFileHandler."""

    WHEN = TimeDuration.DAYS
    INTERVAL = 1
    BACKUP_COUNT = 90


@dataclasses.dataclass
class LoggingConfig:
    """Config for logging and all handlers."""

    TIMED_ROTATING_HANDLER = TimedRotatingFileHandlerConfig
    LOG_FILE_PATH = pathlib.Path("logs", "bot.log")
    DEFAULT_LOG_LEVEL = logging.DEBUG
    CLEAR_EXISTING_LOGS = True
