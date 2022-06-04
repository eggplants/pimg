# `pimg`

[![PyPI version](https://badge.fury.io/py/pimg.svg)](https://badge.fury.io/py/pimg)

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/eggplants/pimg/master.svg)](https://results.pre-commit.ci/latest/github/eggplants/pimg/master)

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
- Then, to save the image in clipboard in local:

```shellsession
$ pimg sth.png
$ file sth.png
sth.png: PNG image data, ...
```

## Usage

```shellsession
$ pimg -h
usage: pimg [-h] [-V] savefile

Save an image in clipboard

positional arguments:
  savefile       File name to save

optional arguments:
  -h, --help     show this help message and exit
  -V, --version  show program's version number and exit
```

## license

MIT

## Author

haruna(eggplants)
