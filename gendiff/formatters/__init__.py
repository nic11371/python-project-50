from gendiff.formatters.format_stylish import make_stylish
from gendiff.formatters.format_plain import make_plain
from gendiff.formatters.format_json import make_json
from gendiff.exception import FormatError


def formatting(data, formatter='stylish'):
    if formatter == 'plain':
        return make_plain(data)
    if formatter == 'json':
        return make_json(data)
    if formatter == 'stylish':
        return make_stylish(data)
    return FormatError("This format not support")
