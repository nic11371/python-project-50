from gendiff.extension import open_file
from gendiff.format.choice_format import choice_format


def generate_diff(file_name1, file_name2, format_name='stylish'):
    data = open_file(file_name1, file_name2)
    return choice_format(data, format_name)
