# orchestrAIframework/percussion/percussion.py
"""
Percussion Section — Timing, Control, RL
Author: Marcos Paulo Pazzinatto | License: MIT
"""

import time
from typing import Any, Dict, Optional, Callable
from orchestrAIframework.common.logging import log_message
from orchestrAIframework.interfaces.section_protocol import Section

class Percussion(Section):
    """
    Schedulers, feedback loops, and RL hooks.
    """

    def __init__(self, name: str = "Percussion"):
        self.name = name
        self.interval_s: float = 0.0
        self.policy: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None
        log_message("info", f"[Percussion] Initialized section: {self.name}")

    def configure(self, interval_s: float = 0.0, policy: Optional[Callable] = None) -> None:
        self.interval_s = interval_s
        self.policy = policy
        log_message("info", f"[Percussion] interval={interval_s}s policy={'set' if policy else 'none'}")

    def tick(self) -> None:
        """A simple timed tick (stub for schedulers)."""
        if self.interval_s > 0:
            time.sleep(min(self.interval_s, 0.05))  # cap for fast demos
        log_message("info", "[Percussion] tick()")

    def perform(self, score: Optional[Dict[str, Any]] = None) -> None:
        log_message("info", "[Percussion] Performing control loop...")
        self.tick()
        state = (score or {})
        if self.policy:
            _ = self.policy(state)
            log_message("info", "[Percussion] Applied policy function (stub).")
        log_message("success", f"[Percussion] Section '{self.name}' completed performance.")

