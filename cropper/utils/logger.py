import logging
from typing import Optional


_LOG_FORMAT = "[%(asctime)s] " "[%(levelname)s] " "%(name)s: %(message)s"


def setup_logging(level: int = logging.INFO, log_file: Optional[str] = None) -> None:
    handlers: list[logging.Handler] = [logging.StreamHandler()]

    if log_file:
        handlers.append(logging.FileHandler(log_file))

    logging.basicConfig(
        level=level,
        format=_LOG_FORMAT,
        handlers=handlers,
        force=True,  # override existing config (important for CLI apps)
    )


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
