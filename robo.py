from copy import deepcopy

from commands import SimSnapshot, RoboSimLike
from grid import GridPosition, GridOrientation

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

    def moveRobo(self) -> SimSnapshot:
        if self.robo is not None:
            # x, y, d = self.robo.x, self.robo.y, self.robo.d
            x, y, d = self.robo.as_tuple()

            match d:
                case GridOrientation.NORTH:
                    self.addRobo(x, y + 1, d.name)

                case GridOrientation.EAST:
                    self.addRobo(x + 1, y, d.name)

                case GridOrientation.SOUTH:
                    self.addRobo(x, y - 1, d.name)

                case GridOrientation.WEST:
                    self.addRobo(x - 1, y, d.name)

        return self.snapshot()
