def added(key, value):
    return {
        'name': key,
        'value': value,
        'type': 'add'
    }


def removed(key, value):
    return {
        'name': key,
        'value': value,
        'type': 'remove'
    }


def nested(key, value1, value2):
    return {
        'name': key,
        'type': 'nested',
        'children': calculate_diff(value1, value2),
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
        'type': 'unchanged'
    }


def calculate_diff(file1, file2):
    diff_add = file2.keys() - file1.keys()
    diff_remove = file1.keys() - file2.keys()
    union_keys = sorted(file2.keys() | file1.keys())

    differents = []

    for _key in union_keys:
        _value1 = file1.get(_key)
        _value2 = file2.get(_key)

        if _key in diff_remove:
            differents.append(removed(_key, _value1))
        elif _key in diff_add:
            differents.append(added(_key, _value2))
        elif isinstance(_value1, dict) and isinstance(_value2, dict):
            differents.append(nested(_key, _value1, _value2))
        elif _value1 != _value2:
            differents.append(modified(_key, _value1, _value2))
        else:
            differents.append(unchanged(_key, _value1))

    sorted_diff = sorted(differents, key=lambda x: x['name'])

    return sorted_diff
