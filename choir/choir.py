# orchestrAIframework/choir/choir.py
"""
Choir Section — Evaluation & Monitoring
Author: Marcos Paulo Pazzinatto | License: MIT
"""

from typing import Any, Dict, List, Optional
from orchestrAIframework.common.logging import log_message
from orchestrAIframework.interfaces.section_protocol import Section

class Choir(Section):
    """
    Metrics registry, slice analysis, and simple reporting.
    """

    def __init__(self, name: str = "Choir"):
        self.name = name
        self.metrics: Dict[str, float] = {}
        log_message("info", f"[Choir] Initialized section: {self.name}")

    def log_metric(self, key: str, value: float) -> None:
        self.metrics[key] = value
        log_message("info", f"[Choir] metric {key}={value}")

    def report(self) -> Dict[str, float]:
        log_message("info", f"[Choir] report -> {self.metrics}")
        return dict(self.metrics)

    def perform(self, score: Optional[Dict[str, Any]] = None) -> None:
        log_message("info", "[Choir] Performing evaluation step...")
        # Example: aggregate a provided metric
        provided = (score or {}).get("metrics", {"accuracy": 0.0})
        for k, v in provided.items():
            self.log_metric(k, float(v))
        _ = self.report()
        log_message("success", f"[Choir] Section '{self.name}' completed performance.")

