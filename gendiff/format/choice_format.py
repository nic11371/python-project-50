from gendiff.format.stylish import make_stylish
from gendiff.format.plain import make_plain
from gendiff.format.format_json import make_json


def choice_format(data, formatter='stylish'):
    if formatter == 'plain':
        return make_plain(data)
    if formatter == 'json':
        return make_json(data)
    return make_stylish(data)
