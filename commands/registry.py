from typing import Any

from .base import Cmd
from .place import PlaceCmd
from .report import ReportCmd

registry: dict[str, type[Cmd[Any]]] = {
    PlaceCmd.code: PlaceCmd,
    ReportCmd.code: ReportCmd
}