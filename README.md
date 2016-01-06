# BioFragmentor
A tool for fragmenting biopolymers such as DNA, RNA or proteins for MS/MS.

## Requirements
- Python 3

## Installation
Not possible right now. Run the main script from a console with "python biofragmentor.py"

## Usage
### Windows executable
> biofragmentor_cli.exe --help
### Python script
> python biofragmentor_cli.py --help

Displays an overview to all commands
> biofragmentor_cli.exe [--type {protein,rna,dna}] [--mode {positive,negative}] [--maxcharges MAXCHARGES] SEQUENCE

- --type defines the biopolymer. Right now, basic protein, RNA and DNA is supported, but more can be easily defined in the files data/sequences.xml and data/monomers.xml
- --mode defines the type of MS/MS you want to calculate: Positive (+H) or Negative (-H). Currently, it does not support adducts. Default is negative.
- --maxcharges defines the maximum charge on a fragment. Default is 2.

## Examples
```
$ biofragmentor_cli.py TAC --maxcharges=1
78.958508       M       .-H2O-H
96.969073       M       .-H
97.028955       M       C-b(C)-H2O-H
97.028955       M       A-b(A)-H2O-H
97.028955       M       T-b(T)-H2O-H
115.039520      M       C-b(C)-H
115.039520      M       A-b(A)-H
115.039520      M       T-b(T)-H
176.995288      M       .A-b(A)-H2O-H
176.995288      M       A.-b(A)-H2O-H
176.995288      M       .C-b(C)-H2O-H
176.995288      M       T.-b(T)-H2O-H
195.005853      M       A.-b(A)-H
195.005853      M       .C-b(C)-H
195.005853      M       .A-b(A)-H
195.005853      M       T.-b(T)-H
208.072217      M       C-H2O-H
223.071883      M       T-H2O-H
226.082782      M       C-H
232.083450      M       A-H2O-H
241.082448      M       T-H
250.094015      M       A-H
256.961621      M       .A.-b(A)-H2O-H
274.972186      M       .A.-b(A)-H
288.038550      M       .C-H2O-H
303.038216      M       T.-H2O-H
306.049115      M       .C-H
312.049783      M       .A-H2O-H
312.049783      M       A.-H2O-H
321.048781      M       T.-H
330.060348      M       .A-H
330.060348      M       A.-H
386.075330      M       A.C-b(A)-H2O-H
392.016116      M       .A.-H2O-H
401.074996      M       T.A-b(A)-H2O-H
404.085895      M       A.C-b(A)-H
410.026681      M       .A.-H
410.086563      M       A.C-b(C)-H2O-H
410.086563      M       T.A-b(T)-H2O-H
419.085561      M       T.A-b(A)-H
428.097128      M       A.C-b(C)-H
428.097128      M       T.A-b(T)-H
466.041663      M       .A.C-b(A)-H2O-H
481.041329      M       T.A.-b(A)-H2O-H
484.052228      M       .A.C-b(A)-H
490.052896      M       .A.C-b(C)-H2O-H
490.052896      M       T.A.-b(T)-H2O-H
499.051894      M       T.A.-b(A)-H
508.063461      M       .A.C-b(C)-H
508.063461      M       T.A.-b(T)-H
521.129825      M       A.C-H2O-H
536.129491      M       T.A-H2O-H
539.140390      M       A.C-H
554.140056      M       T.A-H
601.096158      M       .A.C-H2O-H
616.095824      M       T.A.-H2O-H
619.106723      M       .A.C-H
634.106389      M       T.A.-H
690.121371      M       T.A.C-b(A)-H2O-H
699.132938      M       T.A.C-b(T)-H2O-H
708.131936      M       T.A.C-b(A)-H
714.132604      M       T.A.C-b(C)-H2O-H
717.143503      M       T.A.C-b(T)-H
732.143169      M       T.A.C-b(C)-H
825.175866      M       T.A.C-H2O-H
843.186431      M       T.A.C-H
```

```
$ biofragmentor_cli.exe --type=protein AGP --maxcharges=1 --mode=positive
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
