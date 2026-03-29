import importlib
import pkgutil

from .protocols import RoboSimLike, SimSnapshot
from .custom_types import TypeCmd, TypeRegistry
from .base import Cmd, CmdArgs, CmdOutput
# from .report import ReportCmd
# from .place import PlaceCmdArgs, PlaceCmd
from .registry import register_command, Registry


__all__ = [
    'RoboSimLike', 'SimSnapshot',
    'TypeCmd', 'TypeRegistry',
    "Registry", "register_command",
    "Cmd", "CmdArgs", "CmdOutput",
    # "ReportCmd",
    # "PlaceCmd", "PlaceCmdArgs",
]


def _autoload():
    for module in pkgutil.iter_modules(__path__):
        importlib.import_module(f'{__name__}.{module.name}')


_autoload()