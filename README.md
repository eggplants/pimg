# `pimg`

[![PyPI version](
  <https://img.shields.io/pypi/v/pimg?color=blue>
  )](
  <https://pypi.org/project/pimg>
) [![pre-commit.ci status](
  <https://results.pre-commit.ci/badge/github/eggplants/pimg/master.svg>
  )](
  <https://results.pre-commit.ci/latest/github/eggplants/pimg/master>
) [![Maintainability](
  <https://qlty.sh/badges/b5bbd1cc-cd7b-4beb-bcb5-8fec8591c700/maintainability.svg>
  )](
  <https://qlty.sh/gh/eggplants/projects/pimg>
) [![Code Coverage](
  <https://qlty.sh/badges/b5bbd1cc-cd7b-4beb-bcb5-8fec8591c700/test_coverage.svg>
  )](
  <https://qlty.sh/gh/eggplants/projects/pimg>
)

- CLI (and library) for saving an image in clipboard to a local file with PyGObject
- Inspired by [PasteImg](https://github.com/cas--/PasteImg)
  - requires Python 2.x and PyGTK (Last-Modified: May 2011)

## Install

```bash
pip install pimg
```

## Example

- First, crop or copy image on browser
  - e,g) Cropping a screen:
    - Ubuntu: Shift+PrtScn
    - Windows: Win+Shift+S
- To save an image in clipboard in local:

```bash
pimg g sth.png
```

- To copy a local image into clipboard:

```bash
pimg c sth.png
```

## Usage

```shellsession
$ pimg -h
usage: pimg [-h] [-V] {get,g,copy,c} ...

Save an image in clipboard / Copy an image to clipboard

positional arguments:
  {get,g,copy,c}
    get (g)       get/save an image from clipboard
    copy (c)      copy a local image to clipboard

options:
  -h, --help      show this help message and exit
  -V, --version   show program's version number and exit
```

```shellsession
$ pimg g -h
usage: pimg get [-h] PATH

positional arguments:
  PATH        path of save file

options:
  -h, --help  show this help message and exit
```

```shellsession
$ pimg c -h
usage: pimg copy [-h] PATH

positional arguments:
  PATH        path of image to copy

options:
  -h, --help  show this help message and exit
```

## license

MIT

## Author

haruna(eggplants)
