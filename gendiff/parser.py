def add(key, value):
    return {
        'name': key,
        'value': value,
        'type': 'add'
    }


def remove(key, value):
    return {
        'name': key,
        'value': value,
        'type': 'remove'
    }


def nested(key, value1, value2):
    return {
        'name': key,
        'type': 'nested',
        'children': parser_data(value1, value2),
    }


def modified(key, value1, value2):
    return {
        'name': key,
        'old_value': value1,
        'new_value': value2,
        'type': 'modified'
    }


def unchanged(key, value):
    return {
        'name': key,
        'value': value,
        'type': 'uncharged'
    }


def transform_type(value):
    if value is None:
        return 'null'
    return str(value).lower() if isinstance(value, bool)else value


def parser_data(file1, file2):
    diff_add = file2.keys() - file1.keys()
    diff_remove = file1.keys() - file2.keys()
    union = sorted(file2.keys() | file1.keys())

    differents = []

    for keys in union:
        values1 = transform_type(file1.get(keys))
        values2 = transform_type(file2.get(keys))

        if keys in diff_remove:
            differents.append(remove(keys, values1))
        elif keys in diff_add:
            differents.append(add(keys, values2))
        elif isinstance(values1, dict) and isinstance(values2, dict):
            differents.append(nested(keys, values1, values2))
        elif values1 != values2:
            differents.append(modified(keys, values1, values2))
        else:
            differents.append(unchanged(keys, values1))

    sorted_diff = sorted(differents, key=lambda x: x['name'])

    return sorted_diff
