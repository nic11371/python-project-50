#!/usr/bin/env python3
import argparse
from gendiff.library.gendiff import generate_diff as gendiff


def main():
    parser = argparse.ArgumentParser(
      description='Compares two configuration files and shows a difference.')
    parser.add_argument("file1", help='first_file')
    parser.add_argument("file2", help='second_file')
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    # gendiff('gendiff/path/file1.json', 'gendiff/path/file2.json')
    print(gendiff(args.file1, args.file2))


if __name__ == '__main__':
    main()
