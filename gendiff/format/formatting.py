from gendiff.format.format_stylish import make_stylish
from gendiff.format.format_plain import make_plain
from gendiff.format.format_json import make_json


def formatting(data, formatter='stylish'):
    if formatter == 'plain':
        return make_plain(data)
    if formatter == 'json':
        return make_json(data)
    return make_stylish(data)
