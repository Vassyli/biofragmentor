import sys
import os

import biofragmentor as BFrag

def get_data_path():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.realpath(__file__))

PATH_CONFIG = [get_data_path(), "data"]

APP_AUTHOR = "Basilius Sauter"
APP_NAME = "BioFragmentor"
APP_DESC = "BioFragmentor -- Biopolymer in silico fragmentation tool"
APP_VERSION = "0.1.1"

APP_URL = "https://github.com/Vassyli/biofragmentor"
APP_LICENSE = "GNU General Public License Version 3"

class BioFragmentor:
    data = None
    def __init__(self):
        self.data = BFrag.Data(os.path.join(*PATH_CONFIG))

    def run_gui(self):
        from gui import MainWindow
        gui = MainWindow()


    def run(self, type, sequence, **kwargs):
        seqlist = self.data.sequences[type].cleanup(sequence)
        fragments = self.data.sequences[type].fragment(seqlist)

        # Additional parameters
        mode = kwargs["mode"]
        maxcharges = kwargs["maxcharges"]

        output = []

        for fragment in fragments:
            masses = self.data.sequences[type].calculateMasses(fragment, self.data.elements)
            for mass in masses:
                output.append([mass[0], mass[1]])
                # And now, add additional sequence losses
                if self.data.sequences[type].hasLoss():
                    for loss in self.data.sequences[type].getLosses():
                        output.append([mass[0]-loss.getExactMass(self.data.elements), mass[1]+"-"+loss.name])
        output2 = []
        # Creating ions
        for line in output:
            if mode == "negative":
                finalloss = -BFrag.Compound(name="", formula="H").getExactMass(self.data.elements)
                finaladd = "-H"
            else:
                finalloss = BFrag.Compound(name="", formula="H").getExactMass(self.data.elements)
                finaladd = "+H"
            for c in range(0, maxcharges):
                charge = c+1
                m = ("M/%i" % (charge, )) if charge > 1 else "M"
                output2.append([(line[0]+finalloss)/charge, line[1] + finaladd, m])

        output = sorted(output2, key=lambda x : x[0])
        for line in output:
            print("%f\t%s\t%s" % (line[0], line[2], line[1]))