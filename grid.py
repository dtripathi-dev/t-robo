from enum import Enum
from dataclasses import dataclass

class GridOrientation(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

@dataclass
class GridPosition:
    x: int
    y: int
    d: GridOrientation

