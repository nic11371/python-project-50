import json
import itertools


def generate_diff(file_path1, file_path2):
    dict1 = json.load(open(file_path1))
    dict2 = json.load(open(file_path2))

    add = [f"+ {key}: {str(value).lower()}"
           for key, value in dict2.items() - dict1.items()]
    remove = [f"- {key}: {str(value).lower()}"
              for key, value in dict1.items() - dict2.items()]
    union = [f"  {key}: {str(value).lower()}"
             for key, value in dict2.items() & dict1.items()]
    result = remove + add + union
    f = list(itertools.chain('{', sorted(result, key=lambda s: s[2]), '}'))
    return '\n'.join(f)


print(generate_diff('gendiff/path/file1.json', 'gendiff/path/file2.json'))
