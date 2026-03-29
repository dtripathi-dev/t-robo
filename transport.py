from typing import Protocol, runtime_checkable, TypeAlias, Callable

TypeWriter: TypeAlias = Callable[[str], None]

@runtime_checkable
class Transport(Protocol):
    def read(self) -> str: ...
    def write(self, message: str) -> None: ...


class CliTransport(Transport):
    def __init__(self, prompt: str = "Enter your command ") -> None:
        self.prompt = prompt

    def read(self) -> str:
        return input(self.prompt).strip().upper()

    def write(self, message: str) -> None:
        print(message)