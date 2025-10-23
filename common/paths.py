# orchestrAIframework/common/paths.py
"""
OrchestrAIFramework - Path Manager
----------------------------------
Author: Marcos Paulo Pazzinatto
License: MIT

This module defines and manages all default paths used by the framework.
It ensures consistent organization of directories for data, models, logs, and outputs,
independent of the runtime environment.

Usage:
    from orchestrAIframework.common.paths import ORCH_PATHS
    print(ORCH_PATHS['data'])
"""

import os
from pathlib import Path

# Determine the project root dynamically (relative to this file)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Define default directories used across the framework
ORCH_PATHS = {
    "root": PROJECT_ROOT,
    "data": PROJECT_ROOT / "data",
    "models": PROJECT_ROOT / "models",
    "logs": PROJECT_ROOT / "logs",
    "outputs": PROJECT_ROOT / "outputs",
    "configs": PROJECT_ROOT / "configs",
    "experiments": PROJECT_ROOT / "experiments",
    "tmp": PROJECT_ROOT / "tmp",
}

def ensure_directories() -> None:
    """
    Ensure all standard directories exist.
    Creates them if missing.
    """
    for name, path in ORCH_PATHS.items():
        os.makedirs(path, exist_ok=True)

def print_paths() -> None:
    """Pretty-print all registered paths."""
    print("\n=== OrchestrAIFramework Paths ===")
    for name, path in ORCH_PATHS.items():
        print(f"{name:<12}: {path}")
    print("=================================")

# Automatically ensure paths exist when the module is imported
ensure_directories()

