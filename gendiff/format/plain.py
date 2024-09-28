def plain(diff, path=''):
    lists = []
    children = diff.get('children')
    for elem in children:
        key = elem.get('name')
        type = elem.get('type')
        value = to_str(elem.get('value'))
        new = to_str(elem.get('new_value'))
        old = to_str(elem.get('old_value'))
        cur_path = f"{path}.{key}" if path else key
        if type == 'add':
            lists.append(
                f"Property '{cur_path}' was added with value: {value}")
        if type == 'remove':
            lists.append(f"Property '{cur_path}' was removed")
        if type == 'nested':
            lists.append(f"{plain(elem, cur_path)}")
        if type == 'modified':
            lists.append(
                f"Property '{cur_path}' was updated. From {old} to {new}")
    format = "\n".join(lists)

    return f"{format}"


def to_str(item):
    if item is None:
        return 'null'
    if isinstance(item, bool):
        return str(item).lower()
    if isinstance(item, (dict, list)):
        return '[complex value]'
    return f"'{item}'"
