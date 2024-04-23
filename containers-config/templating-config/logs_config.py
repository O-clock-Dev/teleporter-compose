import logging


def configure_logs():
    # Create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(
        logging.DEBUG
    )  # Set logger level to the lowest level (DEBUG) by default

    # Create handlers for each log level
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(
        logging.DEBUG
    )  # Set handler level to the lowest level (DEBUG) by default

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Add formatter to handler
    stream_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(stream_handler)

    return logger
