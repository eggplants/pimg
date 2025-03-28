"""Clipboard image manager."""

from __future__ import annotations

from typing import TYPE_CHECKING

import gi

for ns in ("Gtk", "Gdk"):
    gi.require_version(ns, "4.0")

from gi.repository import Gdk, GdkPixbuf, GLib, Gtk  # noqa: E402

if TYPE_CHECKING:
    from pathlib import Path


class PimgSavePathError(Exception):
    """Raised when the save path is invalid."""


class PimgClipBoardError(Exception):
    """Raised when the clipboard image is invalid."""


class PimgGLibError(Exception):
    """Raised when the GLib main loop fails."""


class Pimg:
    """Clipboard image manager."""

    EXTS = ("png", "bmp", "jpg", "jpeg", "tiff")

    def __init__(self) -> None:
        """Initialize the Pimg class."""

    def get_clip_img(self, save_path: Path) -> None:
        """Get the image from the clipboard and save it to the specified path.

        Args:
            save_path (Path): Path to save the image."
        Raises:
            PimgSavePathError: If the save path is invalid.
            PimgClipBoardError: If the clipboard image is invalid.
            PimgGLibError: If the GLib main loop fails.

        """
        try:
            self.__get_clip_img(save_path)
        except Exception as e:
            raise PimgGLibError from e

    def __get_clip_img(self, save_path: Path) -> None:
        ext = self.__check_file_format(save_path.suffix)
        cb = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        pixbuf = cb.wait_for_image()
        if pixbuf is None:
            msg = "Image does not exist in your clipboard."
            raise PimgClipBoardError(msg)
        pixbuf.savev(save_path.as_posix(), ext, [], [])

    def __check_file_format(self, ext: str) -> str:
        if ext not in self.EXTS:
            msg = f"Save file extension {ext!r} seem to be invalid."
            raise PimgSavePathError(msg)
        return str(ext)

    def copy_local_img(self, save_path: Path) -> None:
        """Copy the image from the local path to the clipboard.

        Args:
            save_path (Path): Path to save the image.

        Raises:
            PimgSavePathError: If the save path is invalid.
            PimgGLibError: If the GLib main loop fails.

        """
        try:
            loop = GLib.MainLoop()
            self.__copy_local_img(save_path)
            GLib.timeout_add(100, self.__copy_local_img, save_path)
            GLib.timeout_add(1000, loop.quit)
            loop.run()
        except Exception as e:
            raise PimgGLibError from e

    def __copy_local_img(self, save_path: Path) -> None:
        cb = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        pixbuf = GdkPixbuf.Pixbuf.new_from_file(save_path.as_posix())
        cb.set_image(pixbuf)
        cb.store()
