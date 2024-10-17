def make_ident(depth):
    return depth * " "


def make_stylish(performance, depth=0):
    ident_size = depth + 1
    ident = ident_size * 4 - 2
    deep_ident = " " * ident
    end_ident = " " * (ident - 2)
    tree = []
    children = performance.get('children')
    for _elem in children:
        key = _elem.get('name')
        type = _elem.get('type')
        value = _elem.get('value')
        string = to_str(value, ident_size)
        old = to_str(_elem.get('old_value'), ident_size)
        new = to_str(_elem.get('new_value'), ident_size)
        if type == 'add':
            tree.append(f"{deep_ident}+ {key}: {string}")
        if type == 'remove':
            tree.append(f"{deep_ident}- {key}: {string}")
        if type == 'unchanged':
            tree.append(f"{deep_ident}  {key}: {string}")
        if type == 'nested':
            tree.append(
                f"{deep_ident}  {key}: {make_stylish(_elem, ident_size)}")
        if type == 'modified':
            tree.append(f"{deep_ident}- {key}: {old}")
            tree.append(f"{deep_ident}+ {key}: {new}")
    format = "\n".join(tree)
    return f"{{\n{format}\n{end_ident}}}"


def to_str(value, depth):
    ident_size = depth + 1
    ident = ident_size * 4 - 2
    deep_ident = " " * ident
    end_ident = " " * (ident - 2)
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
                f"{deep_ident}  {_key}: {to_str(_row, ident_size)}")
        format = "\n".join(rows)
        return f"{{\n{format}\n{end_ident}}}"
    return f"{value}"
