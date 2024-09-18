import itertools


def to_string(value):
    if isinstance(value, dict):
        list_ = []
        for key, item in value.items():
            list_.append(f"{key}: {to_string(item)}")
        return "\n".join(list_)
    return f"{value}"


def stylish(diff):
    list_dict = []
    for key, value in diff.items():
        if key == 'children':
            list_dict.append(stylish(value))
    return list_dict
    
