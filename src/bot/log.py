"""File setup loggers"""
import logging
from logging.handlers import TimedRotatingFileHandler
import sys


def setup_logger(log_level: str = "DEBUG") -> None:
    """Setup loggers.

    Parameters
    -----------
    `log_level (str = "DEBUG")`:
    Lowest severity log message logger will handle.
    """

    # Some configs?
    log_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    log_file_path = "../logs/logs.log"

    # Check if it is valid
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")
    logger = logging.getLogger(__package__)
    logger.setLevel(numeric_level)

    # Handler for logging to file with timed rotation
    rotation_handler = TimedRotatingFileHandler(
        log_file_path,
        "d",
        1,
        90,
    )
    rotation_handler.setFormatter(log_formatter)
    logger.addHandler(rotation_handler)

    logger.info("Logger started with log level %s.", log_level)

    # Logs to stdout if log level is DEBUG
    if numeric_level == logging.DEBUG:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(log_formatter)
        logger.addHandler(stream_handler)
        logger.debug("Streaming logs to stdout.")
