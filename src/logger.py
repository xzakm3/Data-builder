import logging
from typing_extensions import Final

LOGGER_NAME: Final = "default_logger"


class CustomFormatter(logging.Formatter):

    blue = "\x1b[34m;"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    _format = "%(asctime)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.INFO: blue + _format + reset,
        logging.WARNING: yellow + _format + reset,
        logging.ERROR: red + _format + reset,
    }

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def init_logger() -> None:
    logger = get_logger()
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(CustomFormatter())

    logger.addHandler(ch)


def get_logger() -> logging.Logger:
    return logging.getLogger(LOGGER_NAME)
