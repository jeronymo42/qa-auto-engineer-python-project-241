from typing import Callable
from gendiff.general.stylers import stylish
from gendiff.general.file_helper import open_file


def return_str_key(json: dict, key: str) -> str:
    value = json.get(key, False)
    if isinstance(value, bool):
        return str(value).lower()
    return value

def diff_parser(path_1: str, path_2: str, styler: Callable[[str], str] = stylish) -> str:
    file_1 = open_file(path_1)
    file_2 = open_file(path_2)

    if not file_1 and not file_2:
        return styler('')
    
    if isinstance(file_1, dict) and isinstance(file_2, dict):
        result_json = {**file_1, **file_2}
        sorted_data = {
            key: return_str_key(result_json, key)
            for key in sorted(result_json.keys())
        }
        result = ""
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
        return styler(result)
    return styler('')