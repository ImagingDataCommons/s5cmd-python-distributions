from __future__ import annotations

import subprocess
import sys
import sysconfig
from pathlib import Path

import pytest

if sys.version_info < (3, 10):
    from importlib_metadata import distribution
else:
    from importlib.metadata import distribution

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
    dist = distribution("s5cmd")
    scripts_paths = [
        Path(sysconfig.get_path("scripts", scheme)).resolve()
        for scheme in sysconfig.get_scheme_names()
    ]
    scripts = []
    for file in dist.files:
        if file.locate().parent.resolve(strict=True) in scripts_paths:
            scripts.append(file.locate().resolve(strict=True))
    return scripts


@all_tools
def test_package_script(tool):
    expected_version = "2.3.0"
    scripts = [script for script in _get_scripts() if script.stem == tool]
    assert len(scripts) == 1
    output = subprocess.check_output([str(scripts[0]), "version"]).decode("ascii")
    # Output of the form "vX.Y.Z-SHA{N}"
    assert output.splitlines()[0].split("-")[0] == f"v{expected_version}"
