"""
Copyright (c) 2024 Jean-Christophe Fillion-Robin. All rights reserved.

s5cmd: This project provides the infrastructure to build s5cmd Python wheels.
"""


from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import NoReturn

from ._version import version as __version__

__all__ = ["__version__", "s5cmd"]


S5CMD_BIN_DIR: Path = Path(__file__).parent


def _program(name: str, args: list[str]) -> int:
    return subprocess.call([S5CMD_BIN_DIR / name, *args], close_fds=False)


def s5cmd() -> NoReturn:
    """Run the s5cmd executable with arguments passed to a Python script."""
    raise SystemExit(_program("s5cmd", sys.argv[1:]))
