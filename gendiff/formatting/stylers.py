import json


def stylish(diff: list) -> str:
    result = "{\n"
    change_symbols = {
        "no_key": "-",
        "new_key": "+",
        "same": " ",
        "old_value": "-",
        "new_value": "+",
    }
    for item in diff:
        change_type, key, value = item.split(":", 2)
        result += f"  {change_symbols.get(change_type)} {key}: {value}\n"
    result += "}"
    return result


def plain(diff: list) -> str:
    result = ""
    for item in diff:
        change_type, key, value = item.split(":", 2)
        if change_type == "no_key":
            result += f"Property '{key}' was removed\n"
        elif change_type == "new_key":
            result += f"Property '{key}' was added with value: {value}\n"
        elif change_type == "old_value":
            result += f"Property '{key}' was updated. From {value} to "
        elif change_type == "new_value":
            result += f"{value}\n"
    return result.strip()


def plain_json(diff: list) -> str:
    result = {}
    for item in diff:
        change_type, key, value = item.split(":", 2)
        if value.lower() == "true":
            value = True
        elif value.lower() == "false":
            value = False
        if change_type in ["no_key", "new_key", "same"]:
            result[key] = {"change": change_type, "value": value}
        elif change_type == "old_value":
            result[key] = {"change": change_type, "old_value": value}
        elif change_type == "new_value":
            result[key]["new_value"] = value
    return json.dumps(result)
