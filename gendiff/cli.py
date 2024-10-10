import argparse


def print_invitation():    
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument("file1", help='first_file')
    parser.add_argument("file2", help='second_file')
    parser.add_argument(
        "-f", "--format", help="set format of output")
    parser.set_defaults(format='stylish')
    args = parser.parse_args()
    return args.file1, args.file2, args.format