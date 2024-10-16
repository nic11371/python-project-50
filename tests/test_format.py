import pytest
from tests.test_utils import get_expected_data, get_file_path
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize('file1_name, file2_name, out, format', [
    ('file1.json', 'file2.json', 'except_result_diff_stylish.txt', 'stylish'),
    ('file1.json', 'file3.json', 'except_result_stylish.txt', 'stylish'),
    ('file1.yaml', 'file2.yaml', 'except_result_diff_stylish.txt', 'stylish'),
    ('file1.yaml', 'file3.yaml', 'except_result_stylish.txt', 'stylish'),
    ('file1.yml', 'file2.yml', 'except_result_diff_stylish.txt', 'stylish'),
    ('file1.yml', 'file3.yml', 'except_result_stylish.txt', 'stylish'),
    ('file1.json', 'file2.yaml', 'except_result_diff_json.txt', 'json'),
    ('file1.json', 'file2.json', 'except_result_diff_plain.txt', 'plain'),
    ('file1.json', 'file2.json', 'except_result_diff_json.txt', 'json'),
])
def test_format(file1_name, file2_name, out, format):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    expected = get_expected_data(out)
    actual = generate_diff(file1_path, file2_path, format)
    assert actual == expected
