from copy import deepcopy

from custom_types import SimSnapshot
from grid import GridPosition


class RoboSim:
    
    robo: GridPosition | None = None
    
    def snapshot(self) -> SimSnapshot:
        return {
            'robo': deepcopy(self.robo)
        }
    
    def addRobo(self, pos: GridPosition) -> None:
        self.robo = pos
