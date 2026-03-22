from typing import Callable, TypeVar, Generic, Any
from dataclasses import dataclass

from grid import GridOrientation, GridPosition
from robo import RoboSim

from copy import deepcopy

@dataclass
class CmdArgs:
    args: list[str] | None

@dataclass
class PlaceCmdArgs(CmdArgs):
    pos: GridPosition

@dataclass
class CmdOutput:
    success: bool
    data: object

T = TypeVar("T", bound=CmdArgs)

@dataclass
class Cmd(Generic[T]): 
    code: str
    parse: Callable[[str], T]
    execute: Callable[[RoboSim, T], CmdOutput]

def parse_place_args(raw_args: str) -> PlaceCmdArgs:
    if not raw_args:
        raise ValueError('PLACE requires arguments.')

    parts = raw_args.strip().split(',')

    x, y, direction = parts
    pos = GridPosition(x, y, GridOrientation[direction])

    return PlaceCmdArgs(parts, pos)

def execute_place(sim: RoboSim, args: PlaceCmdArgs) -> CmdOutput:
    sim.addRobo(args.pos)
    return CmdOutput(True, None)

def parse_report(_: str) -> CmdArgs:
    return CmdArgs(None)

def execute_report(sim: RoboSim, _: CmdArgs) -> CmdOutput:
    snap = sim.snapshot()
    return CmdOutput(True, deepcopy(snap))

CMD_PLACE = Cmd('PLACE', parse_place_args, execute_place)
CMD_REPORT = Cmd('REPORT', parse_report, execute_report)

CMD_REGISTRY: dict[str, Cmd[Any]] = {
    CMD_PLACE.code: CMD_PLACE,
    CMD_REPORT.code: CMD_REPORT
}
