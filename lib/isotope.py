class Isotope:
	mass = 0.0
	abundance = 0.0
	n = 0
	
	def __init__(self, mass, abundance, n):
		self.mass = float(mass)
		self.abundance = float(abundance)
		self.n = int(n)
		
	def __repr__(self):
		return "<Isotope: %i;%f;%f>" % (self.n, self.mass, self.abundance)