def add(key, value):
    return {key: {
        'value': value,
        'action': 'add'
    }}


def remove(key, value):
    return {key: {
        'value': value,
        'action': 'remove'
    }}


def nested(key, value1, value2):
    return {key: {
        'value': parser_data(value1, value2),
        'action': 'nested'
    }}


def modified(key, value1, value2):
    return {key: {
        'old_value': value1,
        'new_value': value2,
        'action': 'modified'
    }}


def unchanged(key, value):
    return {key: {
        'value': value,
        'action': 'uncharged'
    }}


def transform_type(value):
    if value is None:
        return 'null'
    return str(value).lower() if isinstance(value, bool)else value


def parser_data(file1, file2):
    diff_add = file2.keys() - file1.keys()
    diff_remove = file1.keys() - file2.keys()
    union = file2.keys() | file1.keys()

    differents = {}

    for keys in union:
        values1 = transform_type(file1.get(keys))
        values2 = transform_type(file2.get(keys))

        if keys in diff_remove:
            differents |= remove(keys, values1)
        elif keys in diff_add:
            differents |= add(keys, values2)
        elif isinstance(values1, dict) and isinstance(values2, dict):
            differents |= nested(keys, values1, values2)
        elif values1 != values2:
            differents |= modified(keys, values1, values2)
        else:
            differents |= unchanged(keys, values1)

    sorted_diff = dict(sorted(differents.items()))

    return sorted_diff
