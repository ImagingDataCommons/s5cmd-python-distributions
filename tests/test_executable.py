from __future__ import annotations

import subprocess
import sysconfig
from pathlib import Path

import pytest

import s5cmd

from . import push_argv

all_tools = pytest.mark.parametrize("tool", ["s5cmd"])


def _run(program, args):
    func = getattr(s5cmd, program)
    args = [f"{program}.py", *args]
    with push_argv(args), pytest.raises(SystemExit) as excinfo:
        func()
    assert excinfo.value.code == 0


@all_tools
def test_module(tool):
    _run(tool, ["version"])


def _get_scripts():
    # Collect all "scripts" directories from sysconfig schemes
    scripts_paths = [
        Path(sysconfig.get_path("scripts", scheme)).resolve()
        for scheme in sysconfig.get_scheme_names()
    ]
    scripts = []
    for scripts_dir in scripts_paths:
        # Skip non-existent dirs to avoid Resolve errors
        if not scripts_dir.exists():
            continue
        # Add regular files in the scripts dir (resolve to absolute Path)
        for f in scripts_dir.iterdir():
            if f.is_file():
                scripts.append(f.resolve())
    # remove duplicates while preserving order
    return list(dict.fromkeys(scripts))


@all_tools
def test_package_script(tool):
    expected_version = "2.3.0"
    scripts = [script for script in _get_scripts() if script.stem == tool]
    assert len(scripts) == 1
    output = subprocess.check_output([str(scripts[0]), "version"]).decode("ascii")
    # Output of the form "vX.Y.Z-SHA{N}"
    assert output.splitlines()[0].split("-")[0] == f"v{expected_version}"
