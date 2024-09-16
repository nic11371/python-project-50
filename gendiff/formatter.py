import itertools


def stylish(value, space=" ", count=1):

    def iter_(data):
        list_diff = []
        for key, value in data.items():
            list_diff.append(f"\n{key}: {value}")
        return '\n'.join(list_diff)
    return iter_(value)
        # deep_ident_size = count + depth
        # deep_ident = space * deep_ident_size
        # control = space * depth
        # list = []
        # for key, val in data.items():
        #     list.append(f"{deep_ident}{key}: {iter_(val, deep_ident_size)}")
        # collection = itertools.chain('{', list, [control + '}'])
        # return '\n'.join(collection)

    # return iter_(value, 0)
