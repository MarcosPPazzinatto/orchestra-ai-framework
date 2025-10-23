# orchestrAIframework/conductor/conductor.py
"""
OrchestrAIFramework - Conductor Module
--------------------------------------
Author: Marcos Paulo Pazzinatto
License: MIT

The Conductor is the central manager of the OrchestrAIFramework.
It coordinates all orchestral sections (Strings, Brass, Woodwinds, Percussion, etc.)
by handling registration, configuration, and communication among them.

Each section acts as a specialized AI unit, and the Conductor ensures that
all modules play together in harmony — like a real orchestra.
"""

from typing import Dict, Any, Optional

class Conductor:
    """Main orchestrator of the AI framework."""

    def __init__(self):
        self.sections: Dict[str, Any] = {}
        print("[Conductor] Initialized.")

    def register_section(self, name: str, section: Any) -> None:
        """Register a new orchestral section (e.g., Brass, Strings)."""
        self.sections[name] = section
        print(f"[Conductor] Registered section: {name}")

    def play(self, score: Optional[Dict[str, Any]] = None) -> None:
        """
        Execute the orchestral performance.
        The 'score' defines which sections to activate and in what order.
        """
        print("[Conductor] Beginning orchestral performance...")

        for name, section in self.sections.items():
            print(f"[Conductor] Cueing section: {name}")
            if hasattr(section, "perform"):
                section.perform(score or {})
            else:
                print(f"[Conductor] Section '{name}' has no 'perform' method.")

        print("[Conductor] Performance complete.")

    def summary(self) -> None:
        """Display a summary of registered sections."""
        print("\n=== OrchestrAIFramework Summary ===")
        for name in self.sections:
            print(f"🎵 Section: {name}")
        print("===================================")

