import json


def generate_diff(file_path1, file_path2):
    dictionary1 = json.load(open(file_path1))
    dictionary2 = json.load(open(file_path2))
    dictionary_diff = {}
    
    # dictionary1.items() - dictionary2.items()
    # dictionary2.items() - dictionary1.items()
    print(dictionary1, dictionary2)
    print(dictionary_diff)
