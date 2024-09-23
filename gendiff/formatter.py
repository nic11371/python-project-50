import itertools


OLD = '+'
NEW = '-'
UNCHARGED = ' '


def stylish(diff):
    lists = []
    children = diff.get('children')
    for elem in children:
        key = elem.get('name')
        type = elem.get('type')
        value = elem.get('value')
        if type == 'add':
            lists.append(f"{key}: {to_string(value)}")
        if type == 'remove':
            lists.append(f"{key}: {to_string(value)}")
        if type == 'uncharged':
            lists.append(f"{key}: {to_string(value)}")
        if type == 'nested':
            lists.append(f"{key}: {stylish(elem)}")
        if type == 'modified':
            lists.append(f"{key}: {to_string(elem.get('old_value'))}")
            lists.append(f"{key}: {to_string(elem.get('new_value'))}")
    format = "\n".join(lists)
    return f"{{\n{format}\n}}"


def to_string(item):
    lists = []
    if item is None:
        return 'null'
    if isinstance(item, bool):
        return str(item).lower()
    if isinstance(item, dict):
        for key, val in item.items():
            format = to_string(val)
            lists.append(f"{'{'}\n{key}: {format}\n{'}'}")
        return "\n".join(lists)
    return item
