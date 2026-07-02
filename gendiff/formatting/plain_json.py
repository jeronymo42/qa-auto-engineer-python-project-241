import json


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
