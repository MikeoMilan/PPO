import argparse
from distutils.util import strtobool
def parse_args():
    # fmt: off
    parser = argparse.ArgumentParser()
    parser.add_argument("--sb", type=float, default= 0.314444,
        help="the name of this experiment")
    args = parser.parse_args()
    return args

args = parse_args()
print(args.sb)