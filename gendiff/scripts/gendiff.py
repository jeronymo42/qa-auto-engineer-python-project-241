from gendiff.general.constants import DESCRIPTION
import argparse


def main():
    parser = argparse.ArgumentParser(prog="gendiff", description=DESCRIPTION)

    parser.add_argument("-f", "--format", dest="FORMAT", help="set format of output")

    parser.add_argument("first_file")
    parser.add_argument("second_file")

    parser.parse_args()


if __name__ == "__main__":
    main()
