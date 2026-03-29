from enum import Enum
from dataclasses import dataclass
from typing import Tuple

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

    def as_tuple(self) -> Tuple[int, int, GridOrientation]:
        return self.x, self.y, self.d 

