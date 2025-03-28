"""CLI for pimg."""

from __future__ import annotations

import argparse
import contextlib
import sys
from pathlib import Path
from shutil import get_terminal_size
from typing import TYPE_CHECKING

from pimg import __version__

from . import pimg

if TYPE_CHECKING:
    from collections.abc import Callable


class CustomFormatter(
    argparse.ArgumentDefaultsHelpFormatter,
    argparse.RawDescriptionHelpFormatter,
):
    """Custom formatter for argparse."""


def __func_get(ns: argparse.Namespace) -> None:
    try:
        p = pimg.Pimg()
    except pimg.PimgSavePathError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    try:
        p.get_clip_img(ns.save_file)
    except (pimg.PimgClipBoardError, pimg.PimgGLibError) as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)


def __func_copy(ns: argparse.Namespace) -> None:
    try:
        p = pimg.Pimg()
    except pimg.PimgSavePathError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    try:
        p.copy_local_img(ns.img_file)
    except (pimg.PimgClipBoardError, pimg.PimgGLibError) as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)


def __parse_args(test: tuple[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="pimg",
        formatter_class=(
            lambda prog: CustomFormatter(
                prog,
                width=get_terminal_size(fallback=(120, 50)).columns,
                max_help_position=25,
            )
        ),
        description="Save an image in clipboard / Copy an image to clipboard",
    )

    print_usage_func: Callable[[argparse.Namespace], None] = (  # noqa: E731
        lambda _args: parser.print_usage()
    )
    parser.set_defaults(func=print_usage_func)

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers()

    get_parser = subparsers.add_parser(
        "get",
        aliases=["g"],
        help="get/save an image from clipboard",
    )

    get_parser.add_argument(
        "save_file",
        metavar="PATH",
        type=Path,
        help="path of save file",
    )
    get_parser.set_defaults(func=__func_get)

    copy_parser = subparsers.add_parser(
        "copy",
        aliases=["c"],
        help="copy a local image to clipboard",
    )

    copy_parser.add_argument(
        "img_file",
        metavar="PATH",
        type=Path,
        help="path of image to copy",
    )
    copy_parser.set_defaults(func=__func_copy)

    return parser.parse_args() if test is None else parser.parse_args(test)


def main() -> None:
    """Main function to run the CLI."""
    args = __parse_args()
    args.func(args)


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        main()
