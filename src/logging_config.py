import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logging(name):
    """
    Configures logging for use in the main package
    and the FastAPI application
    """
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    logs_dir = os.path.join(root_dir, "logs")
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    log_filepath = os.path.join(logs_dir, "app.log")

    file_handler = RotatingFileHandler(
        log_filepath, maxBytes=10 * 1024 * 1024, backupCount=5, encoding="utf-8"
    )
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "{asctime} - {levelname} - {filename}:{lineno} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.debug("Logging system init OK")


def get_logger(name):
    return logging.getLogger(name)
