"""Entry program for the 20 November 2026 news image.

Copies the entry.png shipped beside this file to the output directory
(MAKEFUN_OUTPUT_DIR, default /output) as entry.png. Standard library
only, no network. Fails loudly when the image is missing so a bad
run can never silently pass.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isfile(SRC):
        print("entry.png missing beside main.py", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    if sha256(SRC) != sha256(dst):
        print("copied entry.png does not match the shipped one", file=sys.stderr)
        raise SystemExit(1)
    print("wrote", dst)


if __name__ == "__main__":
    main()
