import json


def generate_diff(file_path1, file_path2):
    dict1 = json.load(open(file_path1))
    dict2 = json.load(open(file_path2))
    string = ''
    for key1 in dict1.keys():
        values1 = dict1[key1]
        if key1 in dict2:
            if values1 == dict2[key1]:
                string += f"{key1}: {values1}, "
            string += f"{key1}: {dict2[key1]}, "
            string += f"{key1}: {values1}"
    print(string)
    # add = {key: value for key, value in dict2.items() - dict1.items()}
    # remove = {key: value for key, value in dict1.items() - dict2.items()}
    # union = {key: value for key, value in dict1.items() & dict2.items()}

    # diff = add | remove | union

    # string = str(map(f"\n{key}: {value}", add))
    # for items in dict1.keys() | dict2.keys():
    #     key, value = 
    #     string += f'''\n{div * count * depth}{div * count}{key}: {value}'''
    #     result = list(
    #         itertools.chain("{", string, "\n", div * depth, "}"))
    # return ''.join(result)

    # print(diff)
