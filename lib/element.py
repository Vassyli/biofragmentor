from .isotope import Isotope

class Element:
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
		self.isotopes.append(Isotope(**attribs))
		
	def getExactMass(self, mostabundant = True):
		list = []
		for isotope in self.isotopes:
			list.append((isotope.mass, isotope.abundance))
		list = sorted(list, key=lambda x: x[1])
		if mostabundant == True:
			return list[-1][0]