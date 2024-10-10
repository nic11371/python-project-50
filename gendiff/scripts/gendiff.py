#!/usr/bin/env python3
from gendiff.generate_diff import generate_diff as gendiff
from gendiff.cli import print_invitation


def main():
    file1, file2, format = print_invitation()
    print(gendiff(file1, file2, format))


if __name__ == '__main__':
    main()
