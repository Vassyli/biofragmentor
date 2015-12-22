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