#!/usr/bin/env python3
# import argparse
from gendiff.module.gendiff import generate_diff as gendiff


def main():
    # parser = argparse.ArgumentParser(
    #     description='Compares two configuration files and shows a difference.')
    # parser.add_argument('first_file')
    # parser.add_argument('second_file')
    # parser.add_argument("-f", "--format", help="set format of output")
    # args = parser.parse_args()
    gendiff('gendiff/path/file1.json', 'gendiff/path/file2.json')
    # print(args)


if __name__ == '__main__':
    main()
