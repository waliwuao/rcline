# rcline/__init__.py
from .cat import Cat
from .line import Line
from .map import Map
from .entity import Entity
from .collide import Collide
from .colors import (
    PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR,
    LIGHT_GRAY, MEDIUM_GRAY, DARK_GRAY, SIMPLE_CMAP, ENTITY_COLORS,
    BACKGROUND_COLOR, GRID_MAJOR_COLOR, GRID_MINOR_COLOR
)

__version__ = "0.2.0"
__author__ = "Wally Hao"
__description__ = "A 2D simulation package for cat and line interaction with collision detection"
__all__ = [
    "Cat", "Line", "Map", "Entity", "Collide",
    "PRIMARY_COLOR", "SECONDARY_COLOR", "ACCENT_COLOR",
    "LIGHT_GRAY", "MEDIUM_GRAY", "DARK_GRAY", "SIMPLE_CMAP", "ENTITY_COLORS",
    "BACKGROUND_COLOR", "GRID_MAJOR_COLOR", "GRID_MINOR_COLOR"
]