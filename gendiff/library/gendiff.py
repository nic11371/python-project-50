from gendiff.modules.parser import parser
import json
import yaml
import os


def open_json(file1, file2):
    parser(json.load(open(file1)), json.load(open(file2)))


def open_yaml(file1, file2):
    parser(yaml.load(open(file1)), yaml.load(open(file2)))


def generate_diff(file_name1, file_name2):
    extension_file1 = os.path.splitext(file_name1)[1]
    extension_file2 = os.path.splitext(file_name2)[1]
    if extension_file1 == 'json' and extension_file2 == 'json':
        open_json(file_name1, file_name2)
    elif extension_file1 == 'yaml' and extension_file2 == 'yaml':
        open_yaml(file_name1, file_name2)
    elif extension_file1 == 'yml' and extension_file2 == 'yml':
        open_yaml(file_name1, file_name2)
    else:
        print("Error")
