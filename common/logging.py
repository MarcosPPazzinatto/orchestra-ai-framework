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

