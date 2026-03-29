# from typing import Any

# from .base import Cmd
# from .place import PlaceCmd
# from .report import ReportCmd

# registry: dict[str, type[Cmd[Any]]] = {
#     PlaceCmd.code: PlaceCmd,
#     ReportCmd.code: ReportCmd
# }


from .custom_types import TypeCmd, TypeRegistry

class Registry:
    _registry: TypeRegistry = {}

    @classmethod
    def register(cls, cmd: TypeCmd) -> None:
        code = cmd.code
        
        if code in cls._registry:
            raise ValueError(f'Duplicate command registration: {code}')
        
        cls._registry[code] = cmd

    @classmethod
    def get(cls, code: str) -> TypeCmd:
        return cls._registry[code]

    @classmethod
    def all(cls) -> TypeRegistry:
        return dict(cls._registry)

def register_command(cmd: TypeCmd) -> TypeCmd:
    Registry.register(cmd)
    return cmd
