"""
MegaScan
Módulo de leitura de ROM
"""

from pathlib import Path
import hashlib
import struct
import zlib


class ROM:

    def __init__(self, filename):

        self.filename = Path(filename)

        self.data = self.filename.read_bytes()

        self.size = len(self.data)

    # -----------------------------

    def byte(self, offset):

        return self.data[offset]

    def word(self, offset):

        return struct.unpack_from(">H", self.data, offset)[0]

    def long(self, offset):

        return struct.unpack_from(">I", self.data, offset)[0]

    # -----------------------------

    def crc32(self):

        return zlib.crc32(self.data) & 0xFFFFFFFF

    def sha1(self):

        return hashlib.sha1(self.data).hexdigest()

    def md5(self):

        return hashlib.md5(self.data).hexdigest()

    # -----------------------------

    def read_string(self, offset, size):

        return (
            self.data[offset:offset + size]
            .decode("ascii", errors="ignore")
            .strip()
        )
    # -----------------------------
    # Header Mega Drive
    # -----------------------------

    def console(self):
        return self.read_string(0x100, 16)

    def copyright(self):
        return self.read_string(0x110, 16)

    def domestic_name(self):
        return self.read_string(0x120, 48)

    def international_name(self):
        return self.read_string(0x150, 48)

    def serial(self):
        return self.read_string(0x180, 14)

    def checksum(self):
        return self.word(0x18E)

    def rom_start(self):
        return self.long(0x1A0)

    def rom_end(self):
        return self.long(0x1A4)

    def ram_start(self):
        return self.long(0x1A8)

    def ram_end(self):
        return self.long(0x1AC)

    def region(self):
        return self.read_string(0x1F0, 16)

    def reset_vector(self):
        return self.long(0x0004)