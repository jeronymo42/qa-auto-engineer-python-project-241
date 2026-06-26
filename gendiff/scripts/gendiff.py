import argparse

from gendiff.general.constants import DESCRIPTION
from gendiff.general.diff_parser import diff_parser as dp


def main():
    parser = argparse.ArgumentParser(prog="gendiff", description=DESCRIPTION)

    parser.add_argument(
        "-f", "--format", dest="FORMAT", help="set format of output"
    )

    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)

    args = parser.parse_args()

    print(dp(args.first_file, args.second_file, args.FORMAT))


if __name__ == "__main__":
    main()
