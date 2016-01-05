# main libraries
import sys
import os
import xml.etree.ElementTree as ET

from .element import Element
from .isotope import Isotope
from .sequence import Sequence
from .monomer import Monomer

class Data:
    path = None
    elements = {}
    sequences = {}
    monomers = {}

    def __init__(self, path):
        self.path = path
        # Initialize Databases
        self.initAtoms()
        self.initSequences()
        self.initMonomers()

    def _getRoot(self, file):
        return ET.parse(os.path.join(*[self.path, file])).getroot()

    def initAtoms(self):
        elements = self._getRoot("atoms.xml")
        for element in elements:
            e = Element(**element.attrib)
            self.elements[element.attrib["symbol"]] = e
            # Add Isotopes
            for isotopes in element:
                e.addIsotope(isotopes.attrib)

    def initSequences(self):
        sequences = self._getRoot("sequences.xml")
        for sequence in sequences:
            seq = Sequence.create(**sequence.attrib)
            self.sequences[seq.id] = seq

    def initMonomers(self):
        monomers = self._getRoot("monomers.xml")
        for monomer in monomers:
            mon = Monomer(**monomer.attrib)
            # Add losses
            for loss in monomer:
                mon.addLoss(**loss.attrib)
            self.monomers[mon.id] = mon
            for seqid in  mon.sequence:
                if seqid in self.sequences:
                    self.sequences[seqid].addMonomer(mon)