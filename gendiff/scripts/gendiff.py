#!/usr/bin/env python3
import argparse
from gendiff.generate_diff import generate_diff as gendiff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument("file1", help='first_file')
    parser.add_argument("file2", help='second_file')
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    different = gendiff(args.file1, args.file2)
    print(different)


if __name__ == '__main__':
    main()
