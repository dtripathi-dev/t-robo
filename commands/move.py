
from typing import ClassVar

from .base import Cmd, CmdArgs, CmdOutput
from .registry import register_command
from .protocols import RoboSimLike

@register_command
class MoveCmd(Cmd[CmdArgs]):

    code: ClassVar[str] = 'MOVE'
    
    @classmethod
    def parse(cls, raw_args: str) -> CmdArgs: 
        return CmdArgs([])
    
    @classmethod
    def execute(cls, sim: RoboSimLike, parsed_args: CmdArgs) -> CmdOutput:
        snapshot = sim.moveRobo()
        return CmdOutput(True, snapshot)