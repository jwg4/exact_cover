def add_optional(data, optional):
    """
        Add columns which can be covered 0 or 1 times.
    """
    row_size = len(data[0])
    for row in data:
        yield row
    for point in optional:
        yield [1 if a == point else 0 for a in range(0, row_size)]


def _power_set(l):
    if not l:
        yield []
        return
    car, cdr = l[0], l[1:]
    for s in _power_set(cdr):
        yield s
        yield [car] + s


def add_multiple(data, multiple):
    """
        Add columns which can be covered 1 or more times.

        Doing this can lead to a combinatorial explosion
        of newly added rows.
    """
    for row in data:
        matches = [i for i in multiple if row[i]]
        for s in _power_set(matches): 
            new_row = [(1 if i in s else 0) if i in matches else x for i, x in enumerate(row)]
            yield new_row
