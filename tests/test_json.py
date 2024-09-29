import pytest
from tests._test_format import _test_format


@pytest.mark.parametrize('file1_name, file2_name, out, format', [
    ('file1.json', 'file2.json', 'except_result_diff_json.txt', 'json'),
    ('file1.yaml', 'file2.yaml', 'except_result_diff_json.txt', 'json'),
    ('file1.yml', 'file2.yml', 'except_result_diff_json.txt', 'json'),
    ('file1.json', 'file3.json', 'except_result_json.txt', 'json'),
    ('file1.yaml', 'file3.yaml', 'except_result_json.txt', 'json'),
    ('file1.yml', 'file3.yml', 'except_result_json.txt', 'json'),
])


def test_json(file1_name, file2_name, out, format):
    actual_result, expected_result = _test_format(file1_name, file2_name, out, format)
    assert actual_result == expected_result
