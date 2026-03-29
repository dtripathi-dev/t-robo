from typing import Any, TypeAlias, Protocol
from copy import deepcopy

from grid import GridPosition, GridOrientation

SimSnapshot: TypeAlias = dict[str, Any]


class RoboSimLike(Protocol):
    def snapshot(self) -> SimSnapshot: ...
    def addRobo(self, x: int, y: int, dir: str) -> None: ...

class RoboSim(RoboSimLike):
    
    robo: GridPosition | None = None
    
    def snapshot(self) -> SimSnapshot:
        return {
            'robo': deepcopy(self.robo)
        }
    
    def addRobo(self, x: int, y: int, dir: str) -> None:
        
        if dir not in GridOrientation.__members__:
            raise ValueError(f'Invalid direction: {dir}')
        
        self.robo = GridPosition(x, y, GridOrientation[dir])
