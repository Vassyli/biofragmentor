class Isotope:
    """ Represents Informations needed for an Isotope

    Arguments:
        mass (str, float): Exact mass of the isotope
        abundance (str, float): Natural abundance of the isotope, in percent
        n (str, int): Number of neutrons

    Attributes:
        mass (float): Exact mass of the isotope
        abundance (float): Natural abundance of the isotope, in percent
        n (float): Number of neutrons
    """
    mass = 0.0
    abundance = 0.0
    n = 0

    def __init__(self, mass, abundance, n):
        self.mass = float(mass)
        self.abundance = float(abundance)
        self.n = int(n)

    def __repr__(self):
        """ Returns a repressentative string of an isotope object """
        return "<Isotope: %i;%f;%f>" % (self.n, self.mass, self.abundance)