from __future__ import annotations

import argparse
import sys
from shutil import get_terminal_size

from pimg import __version__

from . import pimg


class CustomFormatter(
    argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter
):
    pass


def func_get(ns: argparse.Namespace) -> None:
    try:
        p = pimg.Pimg()
    except pimg.PimgSavePathError as e:
        print(str(e), file=sys.stderr)
        exit(1)

    try:
        p.get_clip_img(ns.save_file)
    except (pimg.PimgClipBoardError, pimg.PimgGLibError) as e:
        print(str(e), file=sys.stderr)
        exit(1)


def func_copy(ns: argparse.Namespace) -> None:
    try:
        p = pimg.Pimg()
    except pimg.PimgSavePathError as e:
        print(str(e), file=sys.stderr)
        exit(1)

    try:
        p.copy_local_img(ns.img_file)
    except (pimg.PimgClipBoardError, pimg.PimgGLibError) as e:
        print(str(e), file=sys.stderr)
        exit(1)


def parse_args(test: tuple[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="pimg",
        formatter_class=(
            lambda prog: CustomFormatter(
                prog,
                **{
                    "width": get_terminal_size(fallback=(120, 50)).columns,
                    "max_help_position": 25,
                },
            )
        ),
        description="Save an image in clipboard / Copy an image to clipboard",
    )

    parser.set_defaults(func=lambda _: parser.print_usage())

    parser.add_argument(
        "-V", "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    subparsers = parser.add_subparsers()

    get_parser = subparsers.add_parser(
        "get", aliases=["g"], help="get/save an image from clipboard"
    )

    get_parser.add_argument(
        "save_file", metavar="PATH", type=str, help="path of save file"
    )
    get_parser.set_defaults(func=func_get)

    copy_parser = subparsers.add_parser(
        "copy", aliases=["c"], help="copy a local image to clipboard"
    )

    copy_parser.add_argument(
        "img_file", metavar="PATH", type=str, help="path of image to copy"
    )
    copy_parser.set_defaults(func=func_copy)

    if test is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(test)
    return args


def main() -> None:
    args = parse_args()
    args.func(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
