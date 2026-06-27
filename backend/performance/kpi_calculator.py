def normalize(value, max_value):
    if max_value == 0:
        return 0
    return round((value / max_value) * 100, 2)
