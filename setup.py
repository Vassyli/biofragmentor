import sys

from .biofragmentor import PATH_CONFIG, \
    APP_AUTHOR, APP_DESC, APP_LICENSE, \
    APP_NAME, APP_URL, APP_VERSION

if sys.platform == 'win32':
    from disutils.core import setup
    import py2exe

    # Additional files (data/*.xml), license, readme..
    dataFiles = (
        ("", [
            "LICENSE",
            "README.md"]),
        ("data", [
            "data/atoms.xml",
            "data/monomers.xml"
            "data/sequences.xml"]),
    )

    # py2exe options
    py2exe_options = {
        "bundle_files" : 1,
        "compressed" : True,
        "optimize" : 2,
        "excludes" : ["Tkconstants", "Tkinter", "tcl"],
    }

    setup(
        name = APP_NAME,
        version = APP_VERSION,
        description = APP_DESC,
        author = APP_AUTHOR,
        url = APP_URL,
        license = APP_LICENSE,
        windows = ["biofragmentor.py"],
        data_files = dataFiles,
        options = {"py2exe" : py2exe_options},
        zipfile = None
    )
elif sys.platform == 'darwin':
    pass
else:
    pass