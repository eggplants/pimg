from __future__ import annotations

import os

import gi

if gi.get_required_version("Gdk") is None:
    gi.require_version("Gdk", "3.0")

if gi.get_required_version("Gtk") is None:
    gi.require_version("Gtk", "3.0")

from gi.repository import Gdk, GdkPixbuf, GLib, Gtk


class PimgSavePathError(Exception):
    pass


class PimgClipBoardError(Exception):
    pass


class PimgGLibError(Exception):
    pass


class Pimg:

    EXTS = ["png", "bmp", "jpg", "jpeg", "tiff"]

    def __init__(self) -> None:
        pass

    def get_clip_img(self, save_fname: str) -> None:
        try:
            self.__get_clip_img(save_fname)
        except Exception as e:
            raise PimgGLibError(str(e))

    def __get_clip_img(self, save_fname: str) -> None:
        ext = self.__check_file_format(save_fname)
        cb = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        pixbuf = cb.wait_for_image()
        if pixbuf is None:
            raise PimgClipBoardError("Image does not exist in your clipboard.")
        else:
            pixbuf.savev(save_fname, ext, [], [])

    def __check_file_format(self, filename: str) -> str:
        _, ext = os.path.splitext(filename)
        ext = str(ext).replace(".", "")
        if ext == "":
            raise PimgSavePathError(
                f"Save filename {repr(filename)} does not contain an extension."
            )
        elif ext not in self.EXTS:
            raise PimgSavePathError(
                f"Save file extension {repr(ext)} seem to be invalid."
            )
        else:
            return str(ext)

    def copy_local_img(self, img_path: str) -> None:
        try:
            loop = GLib.MainLoop()
            self.__copy_local_img(img_path)
            GLib.timeout_add(100, self.__copy_local_img, os.path.expanduser(img_path))
            GLib.timeout_add(1000, loop.quit)
            loop.run()
        except Exception as e:
            raise PimgGLibError(str(e))

    def __copy_local_img(self, img_path: str) -> None:
        cb = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        pixbuf = GdkPixbuf.Pixbuf.new_from_file(img_path)
        cb.set_image(pixbuf)
        cb.store()
