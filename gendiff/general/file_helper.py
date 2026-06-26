import json

import yaml


def open_json(path: str) -> dict:
    with open(path) as file:
        return json.load(file)


def open_yaml(path: str) -> dict:
    with open(path) as file:
        yaml_data = yaml.safe_load(file)
        return {} if yaml_data is None else yaml_data


def open_file(path: str) -> dict:
    openning_func = {"json": open_json, "yml": open_yaml, "yaml": open_yaml}

    extension = path.split(".")[-1]
    if extension in openning_func:
        return openning_func[extension](path)
    return {}
