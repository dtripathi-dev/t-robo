from robo import RoboSim
from commands import Cmd
from typing import Callable, Any
from custom_types import TypeRegistry, TypeWriter


class RoboSimCommandAdaptor:
    registry: dict[str, Cmd[Any]]
    sim: RoboSim
    writer: Callable[[str], None]

    @classmethod
    def configure(cls, sim: RoboSim, registry: TypeRegistry, writer: TypeWriter):
        cls.sim = sim
        cls.writer = writer
        cls.registry = registry

    @classmethod
    def process_command(cls, raw: str):
        normalized = raw.strip().upper()

        if not normalized:
            raise ValueError('Empty command was passed to process.')
        
        cmd_code, *args = normalized.split()

        if cmd_code not in cls.registry:
            raise ValueError("Command not identified")
        
        cls.writer(f'Command received: {cmd_code}, {args}')
        
        cmd = cls.registry[cmd_code]

        parsed = cmd.parse(args[0] if args else '')
        result = cmd.execute(cls.sim, parsed)

        cls.writer(str(result))
        




