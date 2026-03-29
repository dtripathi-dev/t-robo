from typing import ClassVar
from copy import deepcopy

from robo import RoboSimLike
from .base import Cmd, CmdArgs, CmdOutput

class ReportCmd(Cmd[CmdArgs]):
        
    code: ClassVar[str] = 'REPORT'

    @classmethod
    def parse(cls, raw_args: str) -> CmdArgs:
        return CmdArgs([])

    @classmethod
    def execute(cls, sim: RoboSimLike, parsed_args: CmdArgs) -> CmdOutput:
        snap = sim.snapshot()
        return CmdOutput(True, deepcopy(snap))