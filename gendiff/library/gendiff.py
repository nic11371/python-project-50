import json
import itertools


def transform(value):
    return str(value).lower() if isinstance(value, bool) else value


def generate_diff(file_path1, file_path2):
    dict1 = json.load(open(file_path1))
    dict2 = json.load(open(file_path2))

    add = [f"  + {key}: {transform(value)}"
           for key, value in dict2.items() - dict1.items()]
    remove = [f"  - {key}: {transform(value)}"
              for key, value in dict1.items() - dict2.items()]
    union = [f"    {key}: {transform(value)}"
             for key, value in dict2.items() & dict1.items()]
    result = remove + add + union
    f = list(itertools.chain('{', sorted(result, key=lambda s: s[4]), '}'))
    return '\n'.join(f)


print(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file3.json'))
