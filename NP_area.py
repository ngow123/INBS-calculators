# author: Ben Stordy
# python based NP concentration calculator
# takes command line inputs

# imports the sys module, and the argparse module, allowing for command line
# input.
import sys
import argparse

import nano_area_calcs as calcs

# tell the user that the script is running
print("running", sys.argv[0], "\n")

# define parse to be the funtion ArgumentParser from the argparse module
parse = argparse.ArgumentParser()
# use the add_argument function to specify which command line options the
# calculator will accept. We need three inputs, the diameter, concentration,
# and target area.
parse.add_argument("diameter", type=float, help='the diameter of the NP (in nm)')
parse.add_argument("concentration", type=float, help="the concentration of the"
                    "NP solution (in nM)")
parse.add_argument("target_area", type=float, help="the target area of the NP"
                    " (in cm^2)")
parse.add_argument("-v", "--verbose", action="store_true", help="increase"
                    "verbosity of output")
# parse the arguments passed in the command line
args = parse.parse_args()

area = calcs.sphere_area(args.diameter)
number = calcs.number_NP(area, args.target_area)
mols = calcs.mols_NP(number)
volume = calcs.volume_NP(args.concentration, mols)

if args.verbose:
    print("The area of a single nanoparticle is", "%.4E" % area, "cm^2 \n")
    print("The number of nanoparticles required for", args.target_area, "cm^2",
        "is", "%.4E" % number, "\n")
    print("The number of moles required for", args.target_area, "cm^2 is",
        "%.4E" % mols,"\n")
    print("The volume of", args.concentration, "nM nanoparticle solution",
        "required for", args.target_area, "cm^2 is", "%.2f" % volume, "uL \n")
else:
    print("Use", "%.2f" % volume, "uL for", args.target_area, "cm^2 \n")
