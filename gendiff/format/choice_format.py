from gendiff.format.stylish import stylish
from gendiff.format.plain import plain
from gendiff.format.format_json import make_json


def choice_format(data, format_name='stylish'):
    if format_name == 'plain':
        return plain(data)
    if format_name == 'json':
        return make_json(data)
    return stylish(data)
