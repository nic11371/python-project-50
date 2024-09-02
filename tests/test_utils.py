import json
import os
import pytest
from gendiff.library.gendiff import generate_diff


def read_file(file_name):
    fixture_path = os.path.join('tstst', 'fixtures', f'{file_name}')
    with open(fixture_path) as file:
        return file.read()


def get_input_data(file_name):
    return json.load(read_file(file_name))


def get_expected_data(file_name):
    return read_file(file_name)


@pytest.fixture
def input_diff():
    return get_input_data('file1.json')


@pytest.fixture
def get_expected_result():
    return get_expected_data('except_result_json.txt')


def test_generate_diff(file_1, file_2, format):
    file1_path = read_file(file_1)
    file2_path = read_file(file_2)
    expected_result = get_expected_data(f'exp_{format}.txt')

    actual_result = generate_diff(file1_path, file2_path, format)

    assert actual_result == expected_result
