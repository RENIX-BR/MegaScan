"""
MegaScan
Motorola 68000 Reader
Versão 0.1
"""

from dataclasses import dataclass


@dataclass
class Instruction:
    address: int
    opcode: int
    mnemonic: str
    size: int


class CPU68000:

    def __init__(self, rom):
        self.rom = rom

    def decode(self, pc):

        op = self.rom.word(pc)

        # RTS
        if op == 0x4E75:
            return Instruction(pc, op, "RTS", 2)

        # NOP
        if op == 0x4E71:
            return Instruction(pc, op, "NOP", 2)

        # JSR absoluto longo
        if op == 0x4EB9:
            return Instruction(pc, op, "JSR", 6)

        # JMP absoluto longo
        if op == 0x4EF9:
            return Instruction(pc, op, "JMP", 6)

        # BSR
        if (op & 0xFF00) == 0x6100:
            return Instruction(pc, op, "BSR", 2)

        return Instruction(pc, op, "???", 2)