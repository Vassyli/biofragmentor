import re

class Compound:
    """ Represents the sum formula of a compound without any structural
        informations

    Attributes:
        name (str): Given name of the compound
        formula (str): String repressentation of the sum formula
        listofelements (dict): A dictionary containing the information of
            the attribute formula with elements as keys and number of atoms as
            values.

    Arguments:
        name (str): Given name of the compound
        formula (str): String repressentation of the sum formula
    """
    formula = ""
    listofelements = {}
    name = ""

    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.formula = kwargs["formula"]
        self.__interpretateFormula()

    def __interpretateFormula(self):
        """ Analyzes the chemical sum formula and converts it into a machine-readable
            dictionary which gets stored in listofelements
        """
        self.listofelements = {}
        # from http://stackoverflow.com/questions/9782835/break-string-into-list-elements-based-on-keywords
        a = re.findall(r'[A-Z][a-z]*|\d+', re.sub('[A-Z][a-z]*(?![\da-z])', r'\g<0>1', self.formula))
        for i in range(0, len(a), 2):
            self.listofelements[a[i]] = int(a[i+1])

    def getExactMass(self, elementdata):
        """ Returns the exact mass of the compound according to elemental composition.
            A table containing the physical informations of the elements is needed.

        Arguments:
            elementdata (dict): Dictionary containing elemental symbol : Element object
                association

        Returns:
            (float): The exact mass of the compound
        """
        emass = 0.0
        for element in self.listofelements:
            emass+= elementdata[element].getExactMass() * self.listofelements[element]
        #print(self.name, self.formula, emass)
        return emass