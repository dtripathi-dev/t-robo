from typing import ClassVar
from dataclasses import dataclass
from functools import cached_property

from .base import CmdArgs, Cmd, CmdOutput
from robo import RoboSimLike

@dataclass
class PlaceCmdArgs(CmdArgs):

    @cached_property
    def x(self) -> int:
        return int(self.args[0])
    
    @cached_property
    def y(self) -> int:
        return int(self.args[1])
    
    @cached_property
    def direction(self) -> str:
        return str(self.args[2])

class PlaceCmd(Cmd[PlaceCmdArgs]):

    code: ClassVar[str] = 'PLACE'
    
    @classmethod
    def parse(cls, raw_args: str) -> PlaceCmdArgs: 
        if not raw_args:
            raise ValueError('PLACE requires arguments.')

        parts = raw_args.strip().split(',')

        if len(parts) < 3:
            raise ValueError('PLACE requires exactly 3 args i.e. X,Y,Direction')

        return PlaceCmdArgs(parts)
    
    @classmethod
    def execute(cls, sim: RoboSimLike, parsed_args: PlaceCmdArgs) -> CmdOutput:
        sim.addRobo(parsed_args.x, parsed_args.y, parsed_args.direction)
        return CmdOutput(True, None)