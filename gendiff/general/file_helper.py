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
    if path.endswith(".txt"):
        return open_txt(path)
    return ""


def return_str_key(json: dict, key: str) -> str:
    value = json.get(key, False)
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(path_1: str, path_2: str) -> str:
    file_1 = open_file(path_1)
    file_2 = open_file(path_2)
    if isinstance(file_1, dict) and isinstance(file_2, dict):
        result_json = {**file_1, **file_2}
        sorted_data = {
            key: return_str_key(result_json, key) for key in sorted(result_json.keys())
        }
        result = "{\n"
        for key in sorted_data.keys():
            if key not in file_2:
                result += f"  - {key}: {sorted_data[key]}\n"
            elif key not in file_1:
                result += f"  + {key}: {sorted_data[key]}\n"
            else:
                if sorted_data[key] == file_1[key]:
                    result += f"    {key}: {sorted_data[key]}\n"
                else:
                    result += f"  - {key}: {sorted_data[key]}\n"
                    result += f"  + {key}: {file_1[key]}\n"
        result += "}"
        return result
    return ""
