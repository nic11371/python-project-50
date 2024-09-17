import itertools


def stylish(diff):
    list_dict = []
    for key, value in diff.items():
        if isinstance(key, dict):
            list_dict.append(f"{key}: {stylish(value)}")
    return list_dict
    
