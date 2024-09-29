from gendiff.generate_diff import generate_diff
from tests.test_utils import get_expected_data, get_file_path


def formated(file1_name, file2_name, out, format_name='stylish'):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    expected_result = get_expected_data(out)

    actual_result = generate_diff(file1_path, file2_path, format_name)
    return actual_result, expected_result
