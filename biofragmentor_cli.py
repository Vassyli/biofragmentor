"""biofragmentor_cli.py, a command line interface to fragment biopolymers

This File is the main entry point to biofragmentor and offers a command line
interface (CLI) to the features of this package.

Example:
    Fragment a DNA oligomer consisting of the sequence 5'-TpApC-3'::

        $ python biofragmentor_cli.py TAC --type=dna

    Fragment a RNA oligomer consisting of the sequence 5'-UpApC-3'::

        $ python biofragmentor_cli.py TAC --type=rna

    Fragment a DNA oligomer consisting of the sequence 5'-pGpTpCpAp-3'::

        $ python biofragmentor_cli.py pGTCAp --type=dna

    Fragment a protein consisting of the sequence MALAG::

        $ python biofragmentor_cli.py MALAG --type=protein

"""
# main libraries
import sys
import os
import argparse

# import libraries
from biofragmentor_main import *

if __name__ == "__main__":
    # Initialize Main instance (load database)
    main = BioFragmentor()

    # Command line tools
    parser = argparse.ArgumentParser(description = APP_DESC)

    # Get all possible sequence types
    choices = [x for x in main.data.sequences]
    default = "dna" if "dna" in choices else choices[0]
    parser.add_argument("--type", type=str, choices=choices, default="dna",
        help="Type of the given Sequence. For DNA/RNA, phosphates are added "
        "automatically between the bases (ATC is interpretated as A.T.C). "
        "Phosphates at the start or the end of the sequence have to be added "
        "manually.")

    # Additional MS parameters
    parser.add_argument("--mode", type=str, choices=["positive", "negative"],
        default="negative", help="MS mode (positive or negative)")
    parser.add_argument("--maxcharges", type=int, default=2,
        help="Maximum amount of charges for calculating m/z. Double negative = 2")

    parser.add_argument("sequence", metavar = "SEQUENCE", type = str,
        help = "The biopolymer 1 letter sequence (for example, TAGC for DNA, "
        "UACG for RNA, MTLCCT for Protein. Phosphates at the start or the end "
        "of a phosphate connected sequence have to be added manually.")

    args = parser.parse_args()

    # Run either CLI
    main.run(args.type, args.sequence, mode=args.mode, maxcharges=args.maxcharges)