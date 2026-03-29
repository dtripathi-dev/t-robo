from typing import TypeAlias, Any
from .base import Cmd

TypeCmd: TypeAlias = type[Cmd[Any]]
TypeRegistry: TypeAlias = dict[str, TypeCmd]