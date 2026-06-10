from gendiff.general.constants import DESCRIPTION

from gendiff.general.file_helper import open_file
import argparse


def main():
    parser = argparse.ArgumentParser(prog="gendiff", description=DESCRIPTION)

    parser.add_argument("-f", "--format", dest="FORMAT", help="set format of output")

    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)

    args = parser.parse_args()
    file1 = open_file(args.first_file)
    file2 = open_file(args.second_file)

    print(file1, file2)


if __name__ == "__main__":
    main()
