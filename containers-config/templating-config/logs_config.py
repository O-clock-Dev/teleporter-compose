import os
import logging


def configure_logs():
    # Create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(
        logging.DEBUG
    )  # Set logger level to the lowest level (DEBUG) by default

    # Specify the path for logs based on the mounted volume
    logs_path = "app/logs"
    # imprimet le contennu du dossier frontend

    # Create logs directory if it does not exist
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)

    # Create handlers for each log level
    debug_handler = logging.FileHandler(f"{logs_path}/debug.log", encoding="utf-8")
    debug_handler.setLevel(logging.DEBUG)

    info_handler = logging.FileHandler(f"{logs_path}/info.log", encoding="utf-8")
    info_handler.setLevel(logging.INFO)

    error_handler = logging.FileHandler(f"{logs_path}/error.log", encoding="utf-8")
    error_handler.setLevel(logging.ERROR)

    warning_handler = logging.FileHandler(f"{logs_path}/warning.log", encoding="utf-8")
    warning_handler.setLevel(logging.WARNING)

    critical_handler = logging.FileHandler(
        f"{logs_path}/critical.log", encoding="utf-8"
    )
    critical_handler.setLevel(logging.CRITICAL)

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Add formatter to handlers
    debug_handler.setFormatter(formatter)
    info_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)
    warning_handler.setFormatter(formatter)
    critical_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(debug_handler)
    logger.addHandler(info_handler)
    logger.addHandler(error_handler)
    logger.addHandler(warning_handler)
    logger.addHandler(critical_handler)

    return logger
