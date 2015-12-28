from .isotope import Isotope

class Element:
    """ Contains information about an element

    Attributes:
        symbol (str): Elemental symbol (H, He, Cl, Pt)
        name (str): The english name of the element (Hydrogen, Helium, Chlorine, Platinum)
        z (int): atomic number of the element ("number of protons")
        mass (float): Average mass of the element
        isotopes (list): A list of all isotopes for this element

    Arguments:
        symbol (str): Elemental symbol
        name (str): The english name of the element
        z (int, str): Atomic number
        mass (float, str): Average elemental mass

    """
    symbol = ""
    name = ""
    mass = 0.0
    isotopes = []

    def __init__(self, symbol, name, z, mass):
        self.symbol = symbol
        self.name = name
        self.mass = float(mass)
        self.z = int(z)
        self.isotopes = []

    def __repr__(self):
        return "<Element <%s>: %s; mass=%f; z=%i; isotopes=%i>" % (self.symbol, self.name, self.mass, self.z, len(self.isotopes))

    def addIsotope(self, attribs):
        """ Adds an isotope to a element instance

        Arguments:
            attribs (dict): Dictionary containing arguments for the class Isotope
        """
        self.isotopes.append(Isotope(**attribs))

    def getExactMass(self, mostabundant = True):
        """ Returns the exact mass of an element

        Note:
            The argument "mostabundant" is not implemented yet.

        Arguments:
            mostabundant (bool): ***NOT IMPLEMENTED YET***

        Returns:
            (float) The exact mass of an element
        """
        list = []
        for isotope in self.isotopes:
            list.append((isotope.mass, isotope.abundance))
        list = sorted(list, key=lambda x: x[1])
        if mostabundant == True:
            return list[-1][0]