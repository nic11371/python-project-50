OLD = '- '
NEW = '+ '
UNCHANGED = '  '
SEPARATOR = " "


def stylish(diff, depth=2):
    space = depth * SEPARATOR
    lists = []
    children = diff.get('children')
    for elem in children:
        key = elem.get('name')
        type = elem.get('type')
        value = elem.get('value')
        if type == 'add':
            lists.append(f"{space}{NEW}{key}: {to_string(value, depth)}")
        if type == 'remove':
            lists.append(f"{space}{OLD}{key}: {to_string(value, depth)}")
        if type == 'unchanged':
            lists.append(f"{space}{UNCHANGED}{key}: {to_string(value, depth)}")
        if type == 'nested':
            lists.append(f"{space}{UNCHANGED}{key}: {stylish(elem, depth + 4)}")
        if type == 'modified':
            lists.append(
                f"{space}{OLD}{key}: {to_string(elem.get('old_value'), depth)}")
            lists.append(
                f"{space}{NEW}{key}: {to_string(elem.get('new_value'), depth)}")
    format = "\n".join(lists)
    end_space = SEPARATOR * (depth - 2)

    return f"{{\n{format}\n{end_space}}}"


def to_string(item, depth=2):
    lists = []
    if item is None:
        return 'null'
    if isinstance(item, bool):
        return str(item).lower()
    if isinstance(item, dict):
        space = SEPARATOR * (depth + 4)
        for key, val in item.items():
            format = to_string(val, depth + 4)
            lists.append(f"{space}{UNCHANGED}{key}: {format}")
        format = "\n".join(lists)
        end_space = SEPARATOR * (depth + 2)
        return f"{{\n{format}\n{end_space}}}"
    return f"{item}"
