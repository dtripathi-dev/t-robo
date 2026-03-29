from typing import Any, TypeAlias, Protocol
from copy import deepcopy

from grid import GridPosition

SimSnapshot: TypeAlias = dict[str, Any]


class RoboSimLike(Protocol):
    def snapshot(self) -> SimSnapshot: ...
    def addRobo(self, pos: GridPosition) -> None: ...

class RoboSim(RoboSimLike):
    
    robo: GridPosition | None = None
    
    def snapshot(self) -> SimSnapshot:
        return {
            'robo': deepcopy(self.robo)
        }
    
    def addRobo(self, pos: GridPosition) -> None:
        self.robo = pos
