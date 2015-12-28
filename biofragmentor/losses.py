from .compound import Compound

class Losses:
    """ An abstract class containing attributes and methods dealing with neutral
        losses of a compound.

    Attributes:
        losses (list): List of Compounds describing a neutral loss of a part of
            the molecule.

    Arguments:
        None
    """
    losses = []
    def __init__(self):
        self.losses = []

    def addLoss(self, name, formula, **kwargs):
        """ Adds a loss to the object.

        Arguments:
            name (str): Name of the loss
            formula (str): Chemical sum Formula of the loss
        """
        self.losses.append(Compound(name=name, formula=formula))

    def hasLoss(self):
        """ Checks if an object has at least one loss registered

        Returns:
            (Boolean) True if at least one loss is registered, False if not.
        """
        return True if len(self.losses) > 0 else False

    def getLosses(self):
        """ Yields all losses registered for an object.

        Yields:
            (Compound) A Compound object repressenting a neutral loss
        """
        for x in self.losses:
            yield x