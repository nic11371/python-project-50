from gendiff.generate_diff import generate_diff


# def to_string(value):
    
    # if isinstance(value, dict):
    #     list_ = []
    #     for key, item in value.items():
    #         list_.append(f"{key}: {to_string(item)}")
    #     return "\n".join(list_)
    # return f"{value}"




def stylish(diff):
    list_ = []
    key_ = diff.get('name')
    type_ = diff.get('type')
    # children = diff.get('children')
    if type_ == 'nested' or type_ == 'root':
        for elem in diff['children']:
            list_.append(f'{stylish(elem)}')
    return list_
    #     list_.append(f"{type_} {key_}: {children}")
    # return list_
        # list_.append(f"{k}: {stylish(v)}")
        # print(v)
    
    
    # list_dict = []
    # for key, value in diff.items():
    #     if key == 'children':
    #         list_dict.append(stylish(value))
    # return list_dict
    
# generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')