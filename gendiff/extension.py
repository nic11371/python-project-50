import json
import yaml
import os
from gendiff.root import get_root


def get_json(file1, file2):
    return get_root(json.load(open(file1)), json.load(open(file2)))


def get_yaml(file1, file2):
    return get_root(
        yaml.safe_load(open(file1)), yaml.safe_load(open(file2)))


def open_file(file_name1, file_name2):
    _, extension_file1 = os.path.splitext(file_name1)
    _, extension_file2 = os.path.splitext(file_name2)
    if extension_file1 == '.json' and extension_file2 == '.json':
        return get_json(file_name1, file_name2)
    elif extension_file1 == '.yaml' and extension_file2 == '.yaml':
        return get_yaml(file_name1, file_name2)
    elif extension_file1 == '.yml' and extension_file2 == '.yml':
        return get_yaml(file_name1, file_name2)
    else:
        return "Error. Not found such format"