import json


def open_json(path: str) -> dict:
    with open(path) as file:
        return json.load(file)


def open_txt(path: str) -> str:
    with open(path) as file:
        return file.read()


def open_file(path: str) -> dict | str:
    if path.endswith(".json"):
        return open_json(path)
    return open_txt(path)
