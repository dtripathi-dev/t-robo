from typing import ClassVar
from dataclasses import dataclass
from functools import cached_property

from .base import CmdArgs, Cmd, CmdOutput

from grid import GridOrientation, GridPosition
from robo import RoboSimLike

@dataclass
class PlaceCmdArgs(CmdArgs):
    # pos: GridPosition | None = None
    @cached_property
    def pos(self) -> GridPosition:
        if not self.args:
            raise ValueError('PLACE requires x, y, direction')
        if len(self.args) < 3:
            raise ValueError('PLACE requires x, y, direction')
        x, y, d = self.args
        return GridPosition(int(x), int(y), GridOrientation[d])

class PlaceCmd(Cmd[PlaceCmdArgs]):

    code: ClassVar[str] = 'PLACE'
    
    @classmethod
    def parse(cls, raw_args: str) -> PlaceCmdArgs: 
        if not raw_args:
            raise ValueError('PLACE requires arguments.')

        parts = raw_args.strip().split(',')

        if len(parts) < 3:
            raise ValueError('PLACE requires exactly 3 args i.e. X,Y,Direction')

        x, y, direction = parts

        if not direction:
            raise ValueError('PLACE seems to have invalid direction argument.')
        
        try:
            pos = GridOrientation[direction]
        except KeyError:
            raise ValueError('PLACE seems to have invalid direction argument.')

        pos = GridPosition(int(x), int(y), pos)

        return PlaceCmdArgs(parts)
    
    @classmethod
    def execute(cls, sim: RoboSimLike, parsed_args: PlaceCmdArgs) -> CmdOutput:
        sim.addRobo(parsed_args.pos)
        return CmdOutput(True, None)