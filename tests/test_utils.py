import json
import os
import pytest
from gendiff.generate_diff import generate_diff


def read_file(file_name):
    fixture_path = os.path.join('tests', 'fixtures', f'{file_name}')
    with open(fixture_path) as file:
        return file.read()


def get_file_path(filename):
    return os.path.join('tests', 'fixtures', filename)


def get_input_data(file_name):
    return json.load(read_file(file_name))


def get_expected_data(file_name):
    return read_file(file_name)


@pytest.fixture
def input_diff():
    return get_input_data('file1.json')


@pytest.fixture
def get_expected_result():
    return get_expected_data('except_result_diff.txt')


@pytest.mark.parametrize('file1_name, file2_name, out', [
    ('file1.json', 'file2.json', 'except_result_diff_stylish.txt'),
    ('file1.json', 'file3.json', 'except_result_stylish.txt'),
    ('file1.yaml', 'file2.yaml', 'except_result_diff_stylish.txt'),
    ('file1.yaml', 'file3.yaml', 'except_result_stylish.txt'),
    ('file1.yml', 'file2.yml', 'except_result_diff_stylish.txt'),
    ('file1.yml', 'file3.yml', 'except_result_stylish.txt'),
    ('file1.json', 'file2.json', 'except_result_diff_plain.txt'),
    ('file1.yaml', 'file2.yaml', 'except_result_diff_plain.txt'),
    ('file1.yml', 'file2.yml', 'except_result_diff_plain.txt'),
])
def test_generate_diff(file1_name, file2_name, out):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    expected_result = get_expected_data(out)

    actual_result = generate_diff(file1_path, file2_path)

    assert actual_result == expected_result
