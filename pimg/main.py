#!/usr/bin/env python3
import argparse
import sys
from typing import Optional, Tuple

from pimg import __version__

from . import pimg


def parse_args(test: Optional[Tuple[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="pimg",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Save an image in clipboard",
    )

    parser.add_argument(
        "savefile", metavar="savefile", type=str, help="File name to save"
    )
    parser.add_argument(
        "-V", "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    if test is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(test)
    return args


def main() -> None:
    args = parse_args()
    try:
        p = pimg.Pimg(args.savefile)
    except pimg.PimgSavePathError as e:
        print(str(e), file=sys.stderr)
        exit(1)

    try:
        p.get_clip_img()
    except (pimg.PimgClipBoardError, pimg.PimgGLibError) as e:
        print(str(e), file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
