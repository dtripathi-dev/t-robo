from typing import TypeVar, Generic, Protocol, ClassVar
from dataclasses import dataclass

from robo import RoboSimLike

@dataclass
class CmdArgs:
    args: list[str]

@dataclass
class CmdOutput:
    success: bool
    data: object

T = TypeVar("T", bound=CmdArgs)

class Cmd(Protocol, Generic[T]):

    code: ClassVar[str]
    
    @classmethod
    def parse(cls, raw_args: str) -> T: ...
    
    @classmethod
    def execute(cls, sim: RoboSimLike, parsed_args: T) -> CmdOutput: ...