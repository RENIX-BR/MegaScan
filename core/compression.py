from dataclasses import dataclass


@dataclass
class CompressionBlock:

    offset: int

    algorithm: str

    size: int = 0

    references: list[int] = None

    valid: bool = False