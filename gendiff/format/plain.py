def make_plain(diff, path=''):
    rows = []
    children = diff.get('children')
    for _elem in children:
        key = _elem.get('name')
        type = _elem.get('type')
        value = to_str(_elem.get('value'))
        new = to_str(_elem.get('new_value'))
        old = to_str(_elem.get('old_value'))
        current_path = f"{path}.{key}" if path else key
        if type == 'add':
            rows.append(f"Property '{current_path}' was added with value: {value}")
        if type == 'remove':
            rows.append(f"Property '{current_path}' was removed")
        if type == 'nested':
            rows.append(f"{make_plain(_elem, current_path)}")
        if type == 'modified':
            rows.append(f"Property '{current_path}' was updated. From {old} to {new}")
    format = "\n".join(rows)
    return f"{format}"


def to_str(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int):
        return value
    if isinstance(value, (dict, list)):
        return '[complex value]'
    return f"'{value}'"
