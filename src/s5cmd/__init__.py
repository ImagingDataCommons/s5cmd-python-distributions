"""
Copyright (c) 2024 Jean-Christophe Fillion-Robin. All rights reserved.

s5cmd: This project provides the infrastructure to build s5cmd Python wheels.
"""


from __future__ import annotations

import subprocess
import sys
from importlib.metadata import distribution
from pathlib import Path
from typing import NoReturn

from ._version import version as __version__

__all__ = ["__version__", "s5cmd"]


def _lookup(name: str) -> Path:
    executable_path = f"s5cmd/bin/{name}"
    files = distribution("s5cmd").files
    if files is not None:
        for _file in files:
            if str(_file).startswith(executable_path):
                return Path(_file.locate()).resolve(strict=True)
    msg = f"Failed to lookup '{executable_path}` directory."
    raise FileNotFoundError(msg)


def _program(name: str, args: list[str]) -> int:
    return subprocess.call([_lookup(name), *args], close_fds=False)


def s5cmd() -> NoReturn:
    """Run the s5cmd executable with arguments passed to a Python script."""
    raise SystemExit(_program("s5cmd", sys.argv[1:]))
