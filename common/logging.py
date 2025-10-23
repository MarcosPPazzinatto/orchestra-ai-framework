# orchestrAIframework/common/logging.py
"""
OrchestrAIFramework - Logging Utility
-------------------------------------
Author: Marcos Paulo Pazzinatto
License: MIT

This module provides a unified logging interface for all sections of the
OrchestrAIFramework. It defines color-coded levels, timestamps, and formatting
to maintain readability and harmony across components.
"""

import logging
import sys
from pathlib import Path

from orchestrAIframework.common.paths import ORCH_PATHS

LOG_FILE = Path(ORCH_PATHS["logs"]) / "orchestrai.log"

# --- Logging configuration ---
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def configure_logger(name: str = "OrchestrAI") -> logging.Logger:
    """
    Configure and return a logger with both console and file handlers.
    """
    logger = logging.getLogger(name)

    if not logger.handlers:  # avoid duplicate handlers
        logger.setLevel(logging.DEBUG)

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))

        # File handler
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger


# --- Color-enhanced helper (optional but aesthetic) ---
class LogColors:
    INFO = "\033[94m"
    SUCCESS = "\033[92m"
    WARNING = "\033[93m"
    ERROR = "\033[91m"
    END = "\033[0m"

def log_message(level: str, message: str, name: str = "OrchestrAI") -> None:
    """
    Simplified helper for quick colorful messages without configuring manually.
    """
    logger = configure_logger(name)

    if level.lower() == "info":
        print(f"{LogColors.INFO}{message}{LogColors.END}")
        logger.info(message)
    elif level.lower() == "success":
        print(f"{LogColors.SUCCESS}{message}{LogColors.END}")
        logger.info(message)
    elif level.lower() == "warning":
        print(f"{LogColors.WARNING}{message}{LogColors.END}")
        logger.warning(message)
    elif level.lower() == "error":
        print(f"{LogColors.ERROR}{message}{LogColors.END}")
        logger.error(message)
    else:
        logger.debug(message)

