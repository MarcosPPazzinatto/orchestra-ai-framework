# orchestrAIframework/interfaces/section_protocol.py
"""
Section Protocol (Base Interface)
Author: Marcos Paulo Pazzinatto | License: MIT
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class Section(ABC):
    """Abstract base for all orchestral sections."""

    @abstractmethod
    def perform(self, score: Optional[Dict[str, Any]] = None) -> None:
        """Entry point called by the Conductor."""
        raise NotImplementedError

