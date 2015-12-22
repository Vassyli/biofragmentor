from .compound import Compound

class Losses:
	losses = []
	def __init__(self):
		self.losses = []
		
	def addLoss(self, name, formula, **kwargs):
		self.losses.append(Compound(name=name, formula=formula))
		
	def hasLoss(self):
		return True if len(self.losses) > 0 else False
		
	def getLosses(self):
		for x in self.losses:
			yield x