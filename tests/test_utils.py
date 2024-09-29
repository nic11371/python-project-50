import os


def read_file(file_name):
    fixture_path = os.path.join('tests', 'fixtures', f'{file_name}')
    with open(fixture_path) as file:
        return file.read()


def get_file_path(filename):
    return os.path.join('tests', 'fixtures', filename)


def get_expected_data(file_name):
    return read_file(file_name)
