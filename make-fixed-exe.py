#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

SOURCE_MD5 = "8498af75c683e163ea6e4ee00e91c14e"
FINAL_MD5 = "d84b47ea26be620f4bcc34dd819022ab"
FINAL_SHA256 = "04ed54c3a6e5217afe7f2413c34dab3ba2bb1994accbd6a48f0f6ccb9d6fc894"

PATCHES = [
    (0x218, "8023", "0024"),
    (0x268, "dce8", "00e9"),
    (0x33B96, "a1ac664a", "e9e5f701"),
    (0x33C02, "c70590614a0000000000", "e8b9f701009090909090"),
    (0x4190D, "8bd0", "31d2"),
    (0x53380, "0000000000", "833ddc4850"),
    (0x53387, "000000000000000000", "750f83c408a140664a"),
    (0x53391, "0000000000000000000000", "8b08e93708feffa1ac664a"),
    (0x5339D, "000000000000000000", "83c40885c0a140664a"),
    (0x533A7, "00000000000000", "8b08e9f907feff"),
    (0x533C0, "0000000000", "c70590614a"),
    (0x533CA, "0000000000", "c705dc4850"),
    (0x533D0, "00", "01"),
    (0x533D4, "00", "c3"),
]

def digest(data, name):
    return hashlib.new(name, data).hexdigest()

def main():
    if len(sys.argv) > 2:
        print("Usage: python3 make-fixed-exe.py [original-exe]")
        return 1

    src = Path(sys.argv[1]) if len(sys.argv) == 2 else Path("TJPC (release).exe")
    if not src.exists():
        print(f"Could not find: {src}")
        print('Put this script next to your original "TJPC (release).exe" and run it again.')
        return 1

    data = bytearray(src.read_bytes())
    if digest(data, "md5") != SOURCE_MD5:
        print("This does not match the game executable this fix was made for.")
        print(f"Expected MD5: {SOURCE_MD5}")
        print(f"Your MD5:     {digest(data, 'md5')}")
        return 1

    for offset, old_hex, new_hex in PATCHES:
        old = bytes.fromhex(old_hex)
        new = bytes.fromhex(new_hex)
        if data[offset:offset+len(old)] != old:
            print(f"Unexpected data at file offset 0x{offset:X}. Nothing was written.")
            return 1
        data[offset:offset+len(old)] = new

    out = Path("TJPC-CrossOver-M2-Final.exe")
    out.write_bytes(data)

    md5 = digest(data, "md5")
    sha256 = digest(data, "sha256")
    if md5 != FINAL_MD5 or sha256 != FINAL_SHA256:
        out.unlink(missing_ok=True)
        print("Verification failed. Nothing was kept.")
        return 1

    print(f"Created: {out}")
    print(f"MD5: {md5}")
    print(f"SHA256: {sha256}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
