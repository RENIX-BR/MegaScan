class PointerScanner:

    def __init__(self, rom):
        self.rom = rom

    def scan(self):

        pointers = {}
        size = self.rom.size

        for offset in range(0, size - 4, 2):

            value = self.rom.long(offset)

            # deve apontar para dentro da ROM
            if value >= size:
                continue

            # alinhamento em palavra
            if value & 1:
                continue

            pointers.setdefault(value, []).append(offset)

        return pointers