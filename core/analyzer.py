from core.database import Resource


class Analyzer:

    def __init__(self, rom):
        self.rom = rom

    def find_vectors(self):

        vectors = []

        for i in range(0, 0x100, 4):

            addr = self.rom.long(i)

            if addr < self.rom.size:

                vectors.append((i, addr))

        return vectors