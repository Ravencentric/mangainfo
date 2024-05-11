<p align="center">
<a href="https://pypi.org/project/mangainfo/"><img src="https://img.shields.io/pypi/v/mangainfo" alt="PyPI - Version" ></a>
<img src="https://img.shields.io/pypi/pyversions/mangainfo" alt="PyPI - Python Version">
<img src="https://img.shields.io/github/license/Ravencentric/mangainfo" alt="License">
<img src="https://www.mypy-lang.org/static/mypy_badge.svg" alt="Checked with mypy">
<img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
</p>

<p align="center">
<img src="https://img.shields.io/github/actions/workflow/status/Ravencentric/mangainfo/release.yml?" alt="GitHub Workflow Status">
<img src="https://img.shields.io/github/actions/workflow/status/Ravencentric/mangainfo/test.yml?label=tests" alt="GitHub Workflow Status">
<a href="https://codecov.io/gh/Ravencentric/mangainfo"><img src="https://codecov.io/gh/Ravencentric/mangainfo/graph/badge.svg?token=6W8R2NKWIQ"/></a>
</p>

## Table Of Contents

* [About](#about)
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)

## About

`mangainfo` is both a library and CLI tool to generate mediainfo for manga archives.

## Installation

`mangainfo` is both a library and CLI tool to generate mediainfo for manga archives. This relies on [archivefile](https://ravencentric.github.io/archivefile/) for reading the archives and [pymediainfo](https://pymediainfo.readthedocs.io/en/stable/) for generating the mediainfo.

```sh
pip install mangainfo
```

## Usage

As a library:

```py
from mangainfo import MangaParser

archive = "~/Blue Box (Digital) (1r0n)/Blue Box v06 (2023) (Digital) (1r0n).cbz"

manga = MangaParser(archive).partial_scan()

for page in manga.pages:
    print(page.resolution)
```

As a CLI:

```sh
❯ mangainfo --help
usage: mangainfo [-h] [--full] path

Generate mediainfo-esque text from a manga archive.

positional arguments:
  path        Path to a manga archive.

options:
  -h, --help  show this help message and exit
  --full      Scan every page. More accurate data but far slower.
```

Refer to the [API reference](https://ravencentric.github.io/mangainfo/api-reference/mangaparser/) for more details.

## License

Distributed under the [Unlicense](https://choosealicense.com/licenses/unlicense/) License. See [UNLICENSE](https://github.com/Ravencentric/mangainfo/blob/main/UNLICENSE) for more information.
