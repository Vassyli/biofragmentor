import re

class Compound:
	formula = ""
	listofelements = {}
	name = ""
	
	def __init__(self, **kwargs):
		self.name = kwargs["name"]
		self.formula = kwargs["formula"]
		self.interpretateFormula()
		
	def interpretateFormula(self):
		self.listofelements = {}
		# from http://stackoverflow.com/questions/9782835/break-string-into-list-elements-based-on-keywords
		a = re.findall(r'[A-Z][a-z]*|\d+', re.sub('[A-Z][a-z]*(?![\da-z])', r'\g<0>1', self.formula))
		for i in range(0, len(a), 2):
			self.listofelements[a[i]] = int(a[i+1])
		
	def getExactMass(self, elementdata):
		emass = 0.0
		for element in self.listofelements:
			emass+= elementdata[element].getExactMass() * self.listofelements[element]
		#print(self.name, self.formula, emass)
		return emass