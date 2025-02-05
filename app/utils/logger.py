import logging


def logger_config(module: str) -> logging.Logger:
    """Extends Python logging module and set a custom config."""

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    custom_logger = logging.getLogger(module)
    custom_logger.setLevel(logging.DEBUG)

    custom_logger.addHandler(handler)

    return custom_logger
