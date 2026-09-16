import random

"""Compatibility helpers backed by the shared game engine."""

import random

from menu_screen import RockPaperScissorsGame


choices = RockPaperScissorsGame.choices


def get_action():
    """Return a random computer move using the engine's choices."""
    return random.choice(choices)

