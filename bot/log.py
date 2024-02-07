"""File setup loggers."""

# Standard Library
import pathlib
import sys
import logging
from logging import handlers

# Third Party Libraries
import discord

# Project Modules
from bot.logging_config import LoggingConfig

# For other modules to import and use
get_logger = logging.getLogger


def setup_log_dir(path: pathlib.Path, reset: bool):
    """Create log dir if none exist and delete existing logs if reset flag is `True`."""
    path.parent.mkdir(exist_ok=True)
    if reset and path.is_file():
        path.unlink()


def setup_logger(log_level_name: str | None) -> None:
    """Setup loggers.

    Args:
    log_level
        Lowest severity log message logger will handle.
    """
    # Add default string without making mypy go crazy
    log_level_name = log_level_name or ""

    # Log file
    log_file = LoggingConfig.LOG_FILE_PATH
    setup_log_dir(log_file, LoggingConfig.CLEAR_EXISTING_LOGS)

    numeric_log_level = logging.getLevelNamesMapping().get(
        log_level_name, LoggingConfig.DEFAULT_LOG_LEVEL
    )

    # Logger
    logger = logging.getLogger()
    logger.setLevel(numeric_log_level)

    # Handler for logging to file with timed rotation
    rotation_handler = handlers.TimedRotatingFileHandler(
        log_file,
        LoggingConfig.TIMED_ROTATING_HANDLER.WHEN,
        LoggingConfig.TIMED_ROTATING_HANDLER.INTERVAL,
        LoggingConfig.TIMED_ROTATING_HANDLER.BACKUP_COUNT,
    )
    discord.utils.setup_logging(handler=rotation_handler)
    rotation_handler.setLevel(numeric_log_level)

    # Logs to stdout if log level is DEBUG
    if numeric_log_level <= +logging.DEBUG:
        stream_handler = logging.StreamHandler(sys.stdout)
        discord.utils.setup_logging(handler=stream_handler)
        logger.debug("Streaming logs to stdout.")

    logger.info("Logger started with log level %s.", log_level_name)
