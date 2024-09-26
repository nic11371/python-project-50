def plain(diff, depth=2):
    lists = []
    children = diff.get('children')
    for elem in children:
        key = elem.get('name')
        type = elem.get('type')
        value = elem.get('value')
        new = to_string(elem.get('new_value'))
        old = to_string(elem.get('old_value'))
        if type == 'add':
            lists.append(f"{key} was added with value: {to_string(value)}")
        if type == 'remove':
            lists.append(f"{key} was removed")
        if type == 'nested':
            lists.append(f"{key}.{plain(elem, depth)}")
        if type == 'modified':
            lists.append(
                f"{key} was updated. From {old} to {new}")
    format = "\n".join(lists)

    return f"{format}"


def to_string(item, depth=2):
    lists = []
    if item is None:
        return 'null'
    if isinstance(item, bool):
        return str(item).lower()
    if isinstance(item, dict):
        for key, val in item.items():
            # format = to_string(val, depth)
            lists.append("")
        format = "\n".join(lists)
        return f"{format}"
    return f"{item}"
