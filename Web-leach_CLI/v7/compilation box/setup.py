from msilib.schema import Icon
import sys
from xml.etree.ElementInclude import include
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"], "includes":('requests', 'bs4', 'natsort', 'googlesearch', 'rjsmin', 'win32ctypes', 'comtypes', 'psutil', 'lxml', 'win32api'), "include_files":["wl-page-2.html"], }

# base="Win32GUI" should be used only for Windows GUI app
base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

setup(
    name = "goo",
    version = "0.1",
    description = "My GUI application!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main_static.py", base=base, icon="icon.ico")]
)

# py setup.py build