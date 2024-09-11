def transform(value):
    if value is None:
        return 'null'
    return str(value).lower() if isinstance(value, bool)else value


def parser_data(file1, file2):
    add = file2.keys() - file1.keys()
    remove = file1.keys() - file2.keys()
    union = file2.keys() | file1.keys()

    differents = []

    for keys in union:
        values1 = transform(file1.get(keys))
        values2 = transform(file2.get(keys))

        if keys in remove:
            differents.append({keys: values1, 'action': 'remove'})
        elif keys in add:
            differents.append({keys: values2, 'action': 'add'})
        elif isinstance(values1, dict) and isinstance(values2, dict):
            differents.append(
                {keys: parser_data(values1, values2), 'action': 'nested'})
        elif values1 != values2:
            differents.append({keys: values2, 'action': 'modified'})
        else:
            differents.append({keys: values1, 'action': 'uncharged'})

    sorted_diff = sorted(differents, key=keys)

    return sorted_diff
