from dataclasses import dataclass


@dataclass
class Reference:

    source: int

    target: int

    kind: str


class ReferenceScanner:

    def __init__(self, rom):

        self.rom = rom

    def scan(self):

        refs = []

        size = self.rom.size

        for offset in range(0, size - 6, 2):

            op = self.rom.word(offset)

            #
            # JSR absoluto
            #
            if op == 0x4EB9:

                addr = self.rom.long(offset + 2)

                if addr < size:

                    refs.append(
                        Reference(
                            offset,
                            addr,
                            "JSR"
                        )
                    )

            #
            # JMP absoluto
            #
            elif op == 0x4EF9:

                addr = self.rom.long(offset + 2)

                if addr < size:

                    refs.append(
                        Reference(
                            offset,
                            addr,
                            "JMP"
                        )
                    )

        return refs