import logging
from typing import Any


class CustomFormatter(logging.Formatter):
    required_fmt = "%(asctime)s %(levelname)s %(filename)s"
    error_rmt = required_fmt + "[%(lineno)d] %(funcName)s(): %(message)s"
    debug_fmt = required_fmt + ": %(message)s"

    def __init__(self) -> None:
        super().__init__(fmt="%(filename)s", datefmt="%Y-%m-%d %I:%M:%S", style="%")

    def format(self, record: Any) -> Any:
        format_orig = self._style._fmt
        if record.levelno <= logging.DEBUG:
            self._style._fmt = CustomFormatter.debug_fmt
        else:
            self._style._fmt = CustomFormatter.error_rmt
        result = logging.Formatter.format(self, record)
        self._style._fmt = format_orig
        return result


def get_logger(log_file: str) -> logging.Logger:
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler(log_file, mode="w")
    file_handler.setFormatter(CustomFormatter())
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger
