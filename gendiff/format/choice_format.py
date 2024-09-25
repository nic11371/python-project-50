from gendiff.format.stylish import stylish
from gendiff.format.plain import plain


def choice_format(data, format_name='stylish'):
    if format_name == 'plain':
        return plain(data)
    return stylish(data)
