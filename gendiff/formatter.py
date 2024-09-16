import itertools


def stylish(diff):
    dictionary = {}
    for elem in diff:
        dictionary[elem['name']] = elem
    return dictionary
