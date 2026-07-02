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
