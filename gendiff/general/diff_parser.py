from typing import Callable

from gendiff.formatting.stylers import plain, stylish, plain_json
from gendiff.general.file_helper import open_file


def return_str_key(json: dict, key: str) -> str:
    value = json.get(key, False)
    if isinstance(value, bool):
        return str(value).lower()
    return value


def get_styler(styler_name: str) -> Callable:
    stylers = {
        "stylish": stylish,
        "plain": plain,
        "json": plain_json,
    }
    return stylers.get(styler_name, stylish)


def diff_parser(path_1: str, path_2: str, styler: str = "stylish") -> str:
    file_1 = open_file(path_1)
    file_2 = open_file(path_2)

    result_json = {**file_1, **file_2}
    sorted_data = {
        key: return_str_key(result_json, key)
        for key in sorted(result_json.keys())
    }
    result = []
    for key in sorted_data.keys():
        if key not in file_2:
            result.append(f"no_key:{key}:{sorted_data[key]}")
        elif key not in file_1:
            result.append(f"new_key:{key}:{sorted_data[key]}")
        else:
            if sorted_data[key] == file_1[key]:
                result.append(f"same:{key}:{sorted_data[key]}")
            else:
                result.append(f"old_value:{key}:{file_1[key]}")
                result.append(f"new_value:{key}:{file_2[key]}")
    return get_styler(styler)(result)
