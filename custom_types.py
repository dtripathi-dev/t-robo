from typing import Any, TypeAlias, Callable

SimSnapshot: TypeAlias = dict[str, Any]

TypeRegistry: TypeAlias = dict[str,  Any]
TypeWriter: TypeAlias = Callable[[str], None]