# main libraries
import sys
import os
import argparse

# import libraries
import lib
import lib.ms as ms

PATH_CONFIG = [os.path.dirname(os.path.realpath(__file__)), "data"]

APP_DESC = "BPFrag -- Biopolymer in silico fragmentation tool"

class bpfrag:
	data = None
	def __init__(self):
		self.data = lib.Data(os.path.join(*PATH_CONFIG))
		
	def run(self, type, sequence, **kwargs):
		seqlist = self.data.sequences[type].cleanup(sequence)
		fragments = self.data.sequences[type].fragment(seqlist)
		
		# Additional parameters
		mode = kwargs["mode"]
		maxcharges = kwargs["maxcharges"]
		
		output = []
		
		for fragment in fragments:
			masses = self.data.sequences[type].calculateMasses(fragment, self.data.elements)
			for mass in masses:
				output.append([mass[0], mass[1]])
				# And now, add additional sequence losses
				if self.data.sequences[type].hasLoss():
					for loss in self.data.sequences[type].getLosses():
						output.append([mass[0]-loss.getExactMass(self.data.elements), mass[1]+"-"+loss.name])
		output2 = []
		# Creating ions
		for line in output:
			if mode == "negative":
				finalloss = -lib.Compound(name="", formula="H").getExactMass(self.data.elements)
				finaladd = "-H"
			else:
				finalloss = lib.Compound(name="", formula="H").getExactMass(self.data.elements)
				finaladd = "+H"
			for c in range(0, maxcharges):
				charge = c+1
				m = ("M/%i" % (charge, )) if charge > 1 else "M"
				output2.append([(line[0]+finalloss)/charge, line[1] + finaladd, m])
		
		output = sorted(output2, key=lambda x : x[0])
		for line in output:
			print("%f\t%s\t%s" % (line[0], line[2], line[1]))

if __name__ == "__main__":
	# Initialize Main instance (load database)
	main = bpfrag()
	
	# Command line tools
	parser = argparse.ArgumentParser(description = APP_DESC)
	
	parser.add_argument("--gui", action="store_true", default = False)
	parser.add_argument("--debug", action='store_true', default = False)
	
	# Get all possible sequence types
	choices = [x for x in main.data.sequences]
	default = "dna" if "dna" in choices else choices[0]
	parser.add_argument("--type", type=str, choices=choices, default="dna")
	
	# Additional MS parameters
	parser.add_argument("--mode", type=str, choices=["positive", "negative"], default="negative")
	parser.add_argument("--maxcharges", type=int, default=2)
	
	parser.add_argument("sequence", metavar = "SEQUENCE", type = str, 
		help = "The biopolymer sequence")
	
	args = parser.parse_args()
	
	# Run either GUI or CLI
	if args.gui == False:
		# CLI
		main.run(args.type, args.sequence, mode=args.mode, maxcharges=args.maxcharges)
	else:
		# GUI
		print("GUI not implemented yet. Sorry!")