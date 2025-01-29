import logging
from datetime import datetime
import os
from pathlib import Path


def setup_logger(name: str, log_file_prefix: str = None) -> logging.Logger:
    logger = logging.getLogger(name)

    # Only set up handlers if they don't exist
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Create formatters
        log_format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_format)
        logger.addHandler(console_handler)

        # File handler (optional)
        if log_file_prefix:
            # Create logs directory if it doesn't exist
            log_dir = Path("logs")
            log_dir.mkdir(exist_ok=True)
            log_file_path = (
                log_dir / f'{log_file_prefix}_{datetime.now().strftime("%Y%m%d")}.log'
            )
            file_handler = logging.FileHandler(log_file_path)
            file_handler.setFormatter(log_format)
            logger.addHandler(file_handler)

    return logger
