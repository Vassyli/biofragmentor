import sys, os, glob

from cx_Freeze import setup, Executable

from biofragmentor_main import APP_AUTHOR, APP_DESC, \
    APP_LICENSE, APP_NAME, APP_URL, APP_VERSION

# Additional files (data/*.xml), license, readme..
includefiles = [
    "LICENSE",
    "README.md",
    "data",
    ]

uifiles = glob.glob("gui/*.ui")
for file in uifiles:
    includefiles.append((file, file))

packages = [
    "biofragmentor.sequence.dnasequence"]
excludes = ["Tkinter"]

# build_exe Options
build_exe_options = {
    "excludes" : excludes,
    "packages" : packages,
    "include_files" : includefiles}

cli_base = None
gui_base = None

if sys.platform == "win32":
    gui_base = "Win32GUI"

setup(
    name = APP_NAME,
    version = APP_VERSION,
    description = APP_DESC,
    author = APP_AUTHOR,
    url = APP_URL,
    license = APP_LICENSE,
    windows = ["biofragmentor.py"],
    options = {
        "build_exe" : build_exe_options},
    executables = [
        Executable("biofragmentor_cli.py", base=cli_base),
        Executable("biofragmentor_gui.py", base=gui_base)
    ]
)