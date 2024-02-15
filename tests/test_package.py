from __future__ import annotations

import importlib.metadata

import s5cmd as m


def test_version():
    assert importlib.metadata.version("s5cmd") == m.__version__
