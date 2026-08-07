from dataclasses import dataclass, field


@dataclass
class MegaProject:

    rom = None

    header: dict = field(default_factory=dict)

    vectors: list = field(default_factory=list)

    instructions: list = field(default_factory=list)

    functions: dict = field(default_factory=dict)

    pointers: dict = field(default_factory=dict)

    resources: list = field(default_factory=list)

    compressions: list = field(default_factory=list)

    graphics: list = field(default_factory=list)

    tilemaps: list = field(default_factory=list)

    palettes: list = field(default_factory=list)