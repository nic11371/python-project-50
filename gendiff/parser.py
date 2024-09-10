import itertools


def transform(value):
    return str(value).lower() if isinstance(value, bool) else value


def parser_data(file1, file2):
    merge = [keys for keys in (file1, file2)]
    return different(merge)


def different(node):

    def walk(elem):
        key, value = elem
        if isinstance(value, dict):
            return key, different(value)
        return key, value

    for elem in node:
        key, value = walk(elem)
        print(key, value)




    # add = [f"  + {key}: {transform(value)}"
    #        for key, value in file2.items() - file1.items()]
    # remove = [f"  - {key}: {transform(value)}"
    #           for key, value in file1.items() - file2.items()]
    # union = [f"    {key}: {transform(value)}"
    #          for key, value in file2.items() & file1.items()]
    # result = remove + add + union
    # f = list(itertools.chain('{', sorted(result, key=lambda s: s[4]), '}'))
    # return '\n'.join(f)
