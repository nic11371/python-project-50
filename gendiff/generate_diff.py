from gendiff.parse import get_data
from gendiff.calculate import build_root
from gendiff.formatters import formatting


def generate_diff(file_name1, file_name2, format_name='stylish'):
    data1 = get_data(file_name1)
    data2 = get_data(file_name2)
    different = build_root(data1, data2)
    return formatting(different, format_name)
