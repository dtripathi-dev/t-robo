from typing import Callable, TypeVar, Generic, TypeAlias
from dataclasses import dataclass, field

from grid import GridOrientation, GridPosition
from robo import RoboSim

from copy import deepcopy

@dataclass
class CmdArgs:
    args: list[str] | None

@dataclass
class PlaceCmdArgs(CmdArgs):
    pos: GridPosition = field(init=False)

    def __post_init__(self):
        if not self.args or len(self.args) != 3:
            raise ValueError('PLACE requires X,Y,DIRECTION')
        x, y, direction = self.args
        self.pos = GridPosition(x, y, GridOrientation[direction])

@dataclass
class CmdOutput:
    success: bool
    data: object

T = TypeVar("T", bound=CmdArgs)


@dataclass
class CmdWithArgs(Generic[T]):
    code: str
    parse: Callable[[str], T]
    execute: Callable[[RoboSim, T], CmdOutput]


@dataclass
class CmdNoArgs:
    code: str
    parse: None
    execute: Callable[[RoboSim], CmdOutput]

def parse_place_args(raw_args: str) -> PlaceCmdArgs:
    if not raw_args:
        raise ValueError('PLACE requires arguments.')

    parsed_args = raw_args.strip().split(',')

    return PlaceCmdArgs(parsed_args)

def execute_place(sim: RoboSim, args: PlaceCmdArgs) -> CmdOutput:
    sim.addRobo(args.pos)
    return CmdOutput(True, None)

def execute_report(sim: RoboSim) -> CmdOutput:
    snap = sim.snapshot()
    return CmdOutput(True, deepcopy(snap))

CmdType: TypeAlias = CmdWithArgs[CmdArgs] | CmdWithArgs[PlaceCmdArgs] | CmdNoArgs

CMD_PLACE = CmdWithArgs('PLACE', parse_place_args, execute_place)
CMD_REPORT = CmdNoArgs('REPORT', None, execute_report)

CMD_REGISTRY: dict[str, CmdType] = {
    CMD_PLACE.code: CMD_PLACE,
    CMD_REPORT.code: CMD_REPORT
}
