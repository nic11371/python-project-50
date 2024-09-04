import itertools


def transform(value):
    return str(value).lower() if isinstance(value, bool) else value


def parser_data(file1, file2):
    add = [f"  + {key}: {transform(value)}"
           for key, value in file2.items() - file1.items()]
    remove = [f"  - {key}: {transform(value)}"
              for key, value in file1.items() - file2.items()]
    union = [f"    {key}: {transform(value)}"
             for key, value in file2.items() & file1.items()]
    result = remove + add + union
    f = list(itertools.chain('{', sorted(result, key=lambda s: s[4]), '}'))
    return '\n'.join(f)
