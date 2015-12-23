# main libraries
import sys
import os

from PyQt5 import QtGui

# import libraries
from biofragmentor_main import *

if __name__ == "__main__":
    # Initialize Main instance (load database)
    main = BioFragmentor()
    main.run_gui()