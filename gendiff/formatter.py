def stylish(diff):
    lists = []
    children = diff.get('children')
    if children:
        for elem in children:
            key = elem.get('name')
            type = elem.get('type')
            if type == 'add':
                lists.append(f"{key}: {string(elem.get('value'))}")
            if type == 'remove':
                lists.append(f"{key}: {string(elem.get('value'))}")
            if type == 'uncharged':
                lists.append(f"{key}: {string(elem.get('value'))}")
            if type == 'nested':
                lists.append(f"{key}: {stylish(elem)}")
            if type == 'modified':
                lists.append(f"{key}: {string(elem.get('old_value'))}")
                lists.append(f"{key}: {string(elem.get('new_value'))}")
    return "\n".join(lists)


def string(item):
    lists = []
    if item is None:
        return 'null'
    if isinstance(item, bool):
        return str(item).lower()
    if isinstance(item, dict):
        for k, val in item.items():
            format = string(val)
            lists.append(f"{k}: {format}")
        return "\n".join(lists)
    return item
