def _try_to_numeric(value):
    try:
        return __try_to_int(value)
    except ValueError:
        pass
    try:
        return __try_to_float(value)
    except ValueError:
        pass
    return value


def __try_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError


def __try_to_float(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError