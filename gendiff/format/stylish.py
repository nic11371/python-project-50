OLD = '- '
NEW = '+ '
EMPTY = '  '
SEPARATOR = " "


def make_stylish(performance, depth=2):
    space = depth * SEPARATOR
    tree = []
    children = performance.get('children')
    for _elem in children:
        key = _elem.get('name')
        type = _elem.get('type')
        value = _elem.get('value')
        string = to_str(value, depth)
        old = to_str(_elem.get('old_value'), depth)
        new = to_str(_elem.get('new_value'), depth)
        if type == 'add':
            tree.append(f"{space}{NEW}{key}: {string}")
        if type == 'remove':
            tree.append(f"{space}{OLD}{key}: {string}")
        if type == 'unchanged':
            tree.append(f"{space}{EMPTY}{key}: {string}")
        if type == 'nested':
            tree.append(
                f"{space}{EMPTY}{key}: {make_stylish(_elem, depth + 4)}")
        if type == 'modified':
            tree.append(f"{space}{OLD}{key}: {old}")
            tree.append(f"{space}{NEW}{key}: {new}")
    format = "\n".join(tree)
    end_space = SEPARATOR * (depth - 2)
    return f"{{\n{format}\n{end_space}}}"


def to_str(value, depth=2):
    rows = []
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int):
        return value
    if isinstance(value, dict):
        space = SEPARATOR * (depth + 4)
        for _key, _row in value.items():
            format = to_str(_row, depth + 4)
            rows.append(f"{space}{EMPTY}{_key}: {format}")
        format = "\n".join(rows)
        end_space = SEPARATOR * (depth + 2)
        return f"{{\n{format}\n{end_space}}}"
    return f"{value}"
