import os
from typing import Any

import gi

if gi.get_required_version("Gdk") is None:  # type: ignore[attr-defined]
    gi.require_version("Gdk", "3.0")

if gi.get_required_version("Gtk") is None:  # type: ignore[attr-defined]
    gi.require_version("Gtk", "3.0")

from gi.repository import Gdk, Gtk


class PimgSavePathError(Exception):
    pass


class PimgClipBoardError(Exception):
    pass


class PimgGLibError(Exception):
    pass


class Pimg:

    EXTS = ["png", "bmp", "jpg", "jpeg", "tiff"]

    def __init__(self, savefile: Any) -> None:
        self.save_fname = savefile
        self.ext = self._check_file_format()

    def _check_file_format(self) -> str:
        ext = os.path.splitext(self.save_fname)[1]
        ext = str(ext).replace(".", "")
        if ext == "":
            raise PimgSavePathError(
                "Save filename '" + self.save_fname + "' does not contain an extension."
            )
        elif ext not in self.EXTS:
            raise PimgSavePathError(
                "Save file extension '" + ext + "' seem to be invalid. "
            )
        else:
            return str(ext)

    def get_clip_img(self) -> None:
        try:
            self._get_clip_img()
        except Exception as e:
            raise PimgGLibError(str(e))

    def _get_clip_img(self) -> None:
        cb = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        pixbuf = cb.wait_for_image()
        if pixbuf is None:
            raise PimgClipBoardError("Image does not exist in your clipboard.")
        else:
            pixbuf.savev(self.save_fname, self.ext, [], [])
