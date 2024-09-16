import itertools


def stylish(diff):
    list_diff = []
    for elem in diff:
        # key = elem['name']
        # type = elem['type']
        # list_diff.append(f"{type} {key}: ")
        for keys, values in elem.items():
            list_diff.append(f"{keys}: {values} ")
    return list_diff
