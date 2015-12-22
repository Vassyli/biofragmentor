import importlib

from ..compound import Compound
from ..losses import Losses

class Sequence(Losses):
	id = ""
	name = ""
	ligationloss = []
	sequencer = None
	monomers = {}
	monomersByName = {}

	def __init__(self, id, name, ligationloss = "", **kwargs):
		self.id = id
		self.name = name
		self.ligationloss = Compound(**{"name":"Ligationloss", "formula":ligationloss})
		self.losses = [] if "losses" not in kwargs else [Compound(name=x.strip(), formula=x.strip()) for x in kwargs["losses"].split(",")]

	def __repr__(self):
		return "<Sequence: %s>" % (self.name, )

	@classmethod
	def create(cls, sequencemodule = None, **kwargs):
		if sequencemodule is not None:
			try:
				i = importlib.import_module("." + sequencemodule, "biofragmentor.sequence")
				return i.SequenceModule(**kwargs)
			except:
				print("Sequencemodule %s not found, using default one." % (sequencemodule))

		return cls(**kwargs)

	def addMonomer(self, monomer):
		self.monomers[monomer.id] = monomer
		self.monomersByName[monomer.name] = monomer

	def checkMonomer(self, monomer_name):
		if monomer_name in self.monomersByName:
			return True
		else:
			return False

	def getMonomer(self, monomer_name):
		return self.monomersByName[monomer_name]

	def cleanup(self, inputsequence):
		l = []
		for a in inputsequence:
			if self.checkMonomer(a) is False:
				raise ValueError("Monomer %s is not a valid Monomer of %s" % (a, str(self)))
			l.append(self.getMonomer(a))
		return l

	def fragment(self, cleansequence):
		# Create every possible sequential combination
		fragments = [cleansequence[start:end+1]
			for start in range(len(cleansequence))
			for end in range(start, len(cleansequence))]
		# Walk trough the fragments and delete any copies
		frag2 = []
		for frag in fragments:
			if frag not in frag2:
				frag2.append(frag)
		return frag2

	def calculateMasses(self, subsequence, elementdata):
		masses = [[self.ligationloss.getExactMass(elementdata), "".join(str(x) for x in subsequence)]]
		for monomer in subsequence:
			# Add Monomer, Substract Ligationloss
			for x in range(0, len(masses)):
				masses[x][0] += monomer.getExactMass(elementdata)-self.ligationloss.getExactMass(elementdata)
			# Has the monomer a specific loss? If you, calculate it.
			if monomer.hasLoss():
				for x in monomer.getLosses():
					appendum = [masses[0][0] - x.getExactMass(elementdata) , masses[0][1] + "-" + x.name]
					if appendum[1] not in [row[1] for row in masses]:
						masses.append([masses[0][0] - x.getExactMass(elementdata) , masses[0][1] + "-" + x.name])
		return masses
