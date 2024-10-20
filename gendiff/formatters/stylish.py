def make_ident(depth):
    return " " * (depth * 4)


def make_stylish(performance, depth=0):
    deep_ident = make_ident(depth)
    tree = []
    children = performance.get('children')
    for _elem in children:
        key = _elem.get('name')
        type = _elem.get('type')
        value = _elem.get('value')
        string = to_str(value, depth + 1)
        old = to_str(_elem.get('old_value'), depth + 1)
        new = to_str(_elem.get('new_value'), depth + 1)
        if type == 'add':
            tree.append(f"{deep_ident}  + {key}: {string}")
        if type == 'remove':
            tree.append(f"{deep_ident}  - {key}: {string}")
        if type == 'unchanged':
            tree.append(f"{deep_ident}    {key}: {string}")
        if type == 'nested':
            tree.append(
                f"{deep_ident}    {key}: {make_stylish(_elem, depth + 1)}")
        if type == 'modified':
            tree.append(f"{deep_ident}  - {key}: {old}")
            tree.append(f"{deep_ident}  + {key}: {new}")
    format = "\n".join(tree)
    return f"{{\n{format}\n{deep_ident}}}"


def to_str(value, depth):
    deep_ident = make_ident(depth)
    rows = []
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int):
        return value
    if isinstance(value, dict):
        for _key, _row in value.items():
            rows.append(
                f"{deep_ident}    {_key}: {to_str(_row, depth + 1)}")
        format = "\n".join(rows)
        return f"{{\n{format}\n{deep_ident}}}"
    return f"{value}"
