from dataclasses import dataclass


@dataclass
class Function:

    address: int
    callers: list


class FunctionScanner:

    def __init__(self, rom):

        self.rom = rom

    def scan(self):

        functions = {}

        size = self.rom.size

        for offset in range(0, size - 6, 2):

            op = self.rom.word(offset)

            #
            # JSR absoluto longo
            #
            if op == 0x4EB9:

                address = self.rom.long(offset + 2)

                if address < size:

                    if address not in functions:

                        functions[address] = Function(
                            address=address,
                            callers=[]
                        )

                    functions[address].callers.append(offset)

        return functions