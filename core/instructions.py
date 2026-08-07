from dataclasses import dataclass


@dataclass
class Opcode:

    offset: int
    opcode: int
    mnemonic: str


class InstructionScanner:

    def __init__(self, rom):
        self.rom = rom

    def scan(self):

        result = []

        size = self.rom.size

        for offset in range(0, size - 2, 2):

            op = self.rom.word(offset)

            mnemonic = None

            # JSR absoluto longo
            if op == 0x4EB9:
                mnemonic = "JSR"

            # JMP absoluto longo
            elif op == 0x4EF9:
                mnemonic = "JMP"

            # LEA
            elif (op & 0xF1C0) == 0x41C0:
                mnemonic = "LEA"

            # BSR
            elif (op & 0xFF00) == 0x6100:
                mnemonic = "BSR"

            # RTS
            elif op == 0x4E75:
                mnemonic = "RTS"

            if mnemonic:
                result.append(
                    Opcode(
                        offset,
                        op,
                        mnemonic
                    )
                )

        return result