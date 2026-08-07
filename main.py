from pathlib import Path

from rom import ROM
from core.cpu68k import CPU68000
from core.analyzer import Analyzer
from core.pointers import PointerScanner
from core.instructions import InstructionScanner
from core.functions import FunctionScanner


class MegaScan:

    def __init__(self, rom_file):

        self.rom = ROM(rom_file)

        self.cpu = CPU68000(self.rom)

        self.analyzer = Analyzer(self.rom)

        self.pointer_scanner = PointerScanner(self.rom)

        self.instruction_scanner = InstructionScanner(self.rom)

        self.function_scanner = FunctionScanner(self.rom)

    # -------------------------------------------------

    def separator(self, title):

        print()
        print("=" * 60)
        print(title)
        print("=" * 60)

    # -------------------------------------------------

    def header(self):

        self.separator("Informações da ROM")

        print(f"Arquivo        : {self.rom.filename.name}")
        print(f"Tamanho        : {self.rom.size:,} bytes")
        print(f"CRC32          : {self.rom.crc32():08X}")
        print(f"SHA1           : {self.rom.sha1()}")

        self.separator("Cabeçalho")

        print(f"Console        : {self.rom.console()}")
        print(f"Copyright      : {self.rom.copyright()}")
        print(f"Nome Japonês   : {self.rom.domestic_name()}")
        print(f"Nome Mundial   : {self.rom.international_name()}")
        print(f"Serial         : {self.rom.serial()}")
        print(f"Checksum       : {self.rom.checksum():04X}")
        print(f"ROM            : {self.rom.rom_start():06X}-{self.rom.rom_end():06X}")
        print(f"RAM            : {self.rom.ram_start():06X}-{self.rom.ram_end():06X}")
        print(f"Região         : {self.rom.region()}")

    # -------------------------------------------------

    def reset_vector(self):

        self.separator("Reset Vector")

        reset = self.rom.reset_vector()

        print(f"{reset:06X}")

        return reset

    # -------------------------------------------------

    def instructions(self, pc):

        self.separator("Primeiras Instruções")

        for _ in range(20):

            ins = self.cpu.decode(pc)

            print(
                f"{ins.address:06X}   "
                f"{ins.opcode:04X}   "
                f"{ins.mnemonic}"
            )

            pc += ins.size

    # -------------------------------------------------

    def vectors(self):

        self.separator("Vetores")

        vectors = self.analyzer.find_vectors()

        for offset, addr in vectors:

            print(f"{offset:06X} -> {addr:06X}")

        print()
        print(f"Total de vetores : {len(vectors)}")

    # -------------------------------------------------

    def pointers(self):

        self.separator("Primeiros Ponteiros")

        pointers = self.pointer_scanner.scan()

        shown = 0

        for target in sorted(pointers):

            print(f"{target:06X}")

            for ref in pointers[target][:5]:

                print(f"   <- {ref:06X}")

            print()

            shown += 1

            if shown == 30:
                break

        print(f"Ponteiros únicos : {len(pointers)}")

    # -------------------------------------------------

    def known_instructions(self):

        self.separator("Instruções Encontradas")

        instructions = self.instruction_scanner.scan()

        for ins in instructions[:100]:

            print(
                f"{ins.offset:06X}   "
                f"{ins.opcode:04X}   "
                f"{ins.mnemonic}"
            )

        print()
        print(f"Instruções encontradas : {len(instructions)}")

    # -------------------------------------------------

    def functions(self):

        self.separator("Funções Descobertas")

        functions = self.function_scanner.scan()

        shown = 0

        for address in sorted(functions):

            fn = functions[address]

            print(f"{address:06X}")

            for caller in fn.callers[:10]:

                print(f"   <- {caller:06X}")

            print()

            shown += 1

            if shown == 25:
                break

        print(f"Funções encontradas : {len(functions)}")

    # -------------------------------------------------

    def run(self):

        self.header()

        reset = self.reset_vector()

        self.instructions(reset)

        self.vectors()

        self.pointers()

        self.known_instructions()

        self.functions()


def main():

    rom_dir = Path("roms")

    roms = (
        list(rom_dir.glob("*.bin")) +
        list(rom_dir.glob("*.md")) +
        list(rom_dir.glob("*.smd"))
    )

    if not roms:

        print("Nenhuma ROM encontrada.")

        return

    print("=" * 60)
    print("MegaScan v0.6")
    print("=" * 60)

    app = MegaScan(roms[0])

    app.run()


if __name__ == "__main__":
    main()