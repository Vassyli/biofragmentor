from .compound import Compound
from .losses import Losses

class Monomer(Compound, Losses):
    """ Contains a Monomer for MS analysis. Inherits all arguments for Compound
        as well.

    Arguments:
        (see class Compound for more)
        id (str): A string with the monomer identifier.
        sequence (str): A comma separated list of sequences that are using this
            Monomer.
        implicit (boolean): True if this is an implicit Monomer, which gets
            hidden in sequence representation (for example, phosphates between
            single bases in DNA).

    Attributes:
        id (str): A string with the monomer identifier.
        sequence (str): A comma separated list of sequences that are using this
            Monomer.
        implicit (boolean): True if this is an implicit Monomer, which gets
            hidden in sequence representation (for example, phosphates between
            single bases in DNA).
    """
    id = ""
    sequence = []
    implicit = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Losses.__init__(self)
        self.id = kwargs["id"]
        self.sequence = [x.strip() for x in kwargs["sequence"].split(",")]
        self.implicit = True if "implicit" in kwargs else False

    def __repr__(self):
        """ Returns a repressentative string of a Monomer Object """
        #return "<Monomer (%s): %s>" % (self.id, self.name, )
        return "%s" % (self.name, )

    def __str__(self):
        """ Returns a string representation of the monomer. This is, typically
            a single letter.
        """
        if self.implicit == False:
            return "%s" % (self.name, )
        else:
            return ""

