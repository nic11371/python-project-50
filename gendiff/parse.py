import json
import yaml
import os


def get_data(path):
    with open(path) as file:
        data = file.read()
        _, format = os.path.splitext(path)
        return parse(data, format)


def parse(data, format):
    if format == '.json':
        return json.loads(data)
    elif format in ['.yaml', '.yml']:
        return yaml.safe_load(data)
    else:
        raise ValueError(f"Not found such format: {format}")
