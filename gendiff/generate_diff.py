import json
import yaml
import os
from gendiff.parser import parser_data


def parse_wrapper(file1, file2):
    return {
        'name': 'main',
        'type': 'root',
        'children': parser_data(file1, file2)
    }


def open_json(file1, file2):
    return parse_wrapper(json.load(open(file1)), json.load(open(file2)))


def open_yaml(file1, file2):
    return parse_wrapper(
        yaml.safe_load(open(file1)), yaml.safe_load(open(file2)))


def generate_diff(file_name1, file_name2):
    extension_file1 = os.path.splitext(file_name1)[1]
    extension_file2 = os.path.splitext(file_name2)[1]
    if extension_file1 == '.json' and extension_file2 == '.json':
        return open_json(file_name1, file_name2)
    elif extension_file1 == '.yaml' and extension_file2 == '.yaml':
        return open_yaml(file_name1, file_name2)
    elif extension_file1 == '.yml' and extension_file2 == '.yml':
        return open_yaml(file_name1, file_name2)
    else:
        print("Error")


# print(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file3.json'))
