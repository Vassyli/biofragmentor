from .compound import Compound
from .losses import Losses

class Monomer(Compound, Losses):
	id = ""
	sequence = []
	implicit = False
	losses = []

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.id = kwargs["id"]
		self.sequence = [x.strip() for x in kwargs["sequence"].split(",")]
		self.implicit = True if "implicit" in kwargs else False
		self.losses = []
		
	def __repr__(self):
		#return "<Monomer (%s): %s>" % (self.id, self.name, )
		return "%s" % (self.name, )
	def __str__(self):
		if self.implicit == False:
			return "%s" % (self.name, )
		else:
			return ""
			
