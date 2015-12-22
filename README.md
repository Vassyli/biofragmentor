# BioFragmentor
A tool for fragmenting biopolymers such as DNA, RNA or proteins for MS/MS.

## Requirements
- Python 3

## Installation
Not possible right now. Run the main script from a console with "python biofragmentor.py"

## Usage
> biofragmentor.py --help

Displays an overview to all commands
> biofragmentor.py [--type {protein,rna,dna}] [--mode {positive,negative}] [--maxcharges MAXCHARGES] SEQUENCE

- --type defines the biopolymer. Right now, basic protein, RNA and DNA is supported, but more can be easily defined in the files data/sequences.xml and data/monomers.xml
- --mode defines the type of MS/MS you want to calculate: Positive (+H) or Negative (-H). Currently, it does not support adducts. Default is negative.
- --maxcharges defines the maximum charge on a fragment. Default is 2.

## Examples
```
biofragmentor.py TAC --maxcharges=1
70.029289       M       A-H2O-H
78.958508       M       .-H2O-H
88.039854       M       A-H
96.969073       M       .-H
100.039854      M       T-H2O-H
102.001361      M       C-H2O-H
118.050419      M       T-H
120.011926      M       C-H
149.995622      M       .A-H2O-H
149.995622      M       A.-H2O-H
168.006187      M       .A-H
168.006187      M       A.-H
180.006187      M       T.-H2O-H
181.967694      M       .C-H2O-H
198.016752      M       T.-H
199.978259      M       .C-H
229.961955      M       .A.-H2O-H
247.972520      M       .A.-H
251.043301      M       T.A-H2O-H
253.004808      M       A.C-H2O-H
269.053866      M       T.A-H
271.015373      M       A.C-H
331.009634      M       T.A.-H2O-H
332.971141      M       .A.C-H2O-H
349.020199      M       T.A.-H
350.981706      M       .A.C-H
434.018820      M       T.A.C-H2O-H
452.029385      M       T.A.C-H
```

```
biofragmentor.py --type=protein AGP --maxcharges=1 --mode=positive
58.029289       M       G-H2O+H
59.013305       M       G-NH3+H
72.044939       M       A-H2O+H
73.028955       M       A-NH3+H
76.039854       M       G+H
90.055504       M       A+H
98.060589       M       P-H2O+H
99.044605       M       P-NH3+H
116.071154      M       P+H
129.066403      M       AG-H2O+H
130.050419      M       AG-NH3+H
147.076968      M       AG+H
155.082053      M       GP-H2O+H
156.066069      M       GP-NH3+H
173.092618      M       GP+H
226.119167      M       AGP-H2O+H
227.103183      M       AGP-NH3+H
244.129732      M       AGP+H
```
