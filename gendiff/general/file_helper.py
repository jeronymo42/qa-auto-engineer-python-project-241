import json
import yaml


def open_json(path: str) -> dict:
    with open(path) as file:
        return json.load(file)


def open_txt(path: str) -> str:
    with open(path) as file:
        return file.read()
    
def open_yaml(path: str) -> dict:
    with open(path) as file:
        return yaml.safe_load(file)


def open_file(path: str) -> dict | str:
    openning_func = {"json": open_json,
                     "yml": open_yaml,
                      "yaml": open_yaml}

    extension = path.split(".")[-1]
    if extension in openning_func:
        return openning_func[extension](path)
    return ""

