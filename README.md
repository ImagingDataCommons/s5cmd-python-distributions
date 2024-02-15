# s5cmd Python Distributions

[![Actions Status][actions-badge]][actions-link]

[![PyPI version][pypi-version]][pypi-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

<!-- SPHINX-START -->

## Overview

`s5cmd` is a very fast S3 and local filesystem execution tool. It comes with
support for a multitude of operations including tab completion and wildcard
support for files, which can be very handy for your object storage workflow
while working with large number of files.

This project provides the infrastructure for building the `s5cmd` Python wheels.
For more information about `s5cmd`, please refer to
https://github.com/peak/s5cmd.

The Python wheels provided here contain the official `s5cmd` executable, which
is sourced from the [GitHub releases](https://github.com/peak/s5cmd/releases).
Once the wheel is installed, a convenient launcher executable is automatically
placed in the PATH. This launcher is created during installation by pip,
leveraging the `[project.scripts]` configuration defined in the `pyproject.toml`
file.

## Platforms

The following platforms are supported by the binary wheels:

| OS            | Arch                                                                                   |
| ------------- | -------------------------------------------------------------------------------------- |
| Windows       | 64-bit<br>32-bit                                                                       |
| Linux Intel   | manylinux2010+ 64-bit<br>musllinux 64-bit<br>manylinux2010+ 32-bit<br>musllinux 32-bit |
| Linux ARM     | manylinux2014+ AArch64<br>musllinux AArch64                                            |
| Linux PowerPC | manylinux2014+ ppc64le<br>musllinux ppc64le                                            |
| Linux IBM Z   | manylinux2014+ s390x<br>musllinux s390x                                                |
| macOS 10.10+  | Intel                                                                                  |
| macOS 11+     | Apple Silicon                                                                          |

## License

This project is maintained by Jean-Christophe Fillion-Robin from Kitware Inc. It
is covered by the OSI-approved MIT License.

`s5cmd` is distributed under the OSI-approved MIT License. For further details
regarding `s5cmd`, please visit https://github.com/peak/s5cmd.

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/jcfr/s5cmd-python-distributions/workflows/CI/badge.svg
[actions-link]:             https://github.com/jcfr/s5cmd-python-distributions/actions
[pypi-link]:                https://pypi.org/project/s5cmd/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/s5cmd
[pypi-version]:             https://img.shields.io/pypi/v/s5cmd

<!-- prettier-ignore-end -->
