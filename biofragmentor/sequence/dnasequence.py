from . import Sequence

class SequenceModule(Sequence):
	def __repr__(self):
		return "<DNASequence: %s>" % (self.name, )
		
	def cleanup(self, inputsequence):
		l = []
		last = None
		for a in inputsequence:
			# Add implicit phosphate if not explicit given
			if last is not None and last.isupper() == True and a.isupper() == True and self.checkMonomer("p") == True:
				l.append(self.getMonomer("."))
			if self.checkMonomer(a) is False:
				raise ValueError("Monomer %s is not a valid Monomer of %s" % (a, str(self)))
			l.append(self.getMonomer(a))
			last = a
		return l