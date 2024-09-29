from gendiff.calculate import calculate_diff


def get_root(file1, file2):
    return {
        'name': 'main',
        'type': 'root',
        'children': calculate_diff(file1, file2)
    }