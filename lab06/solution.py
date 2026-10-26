def count_items(values):
    result = {}
    for i in values:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

def unique_sorted(values):
    values = sorted(set(values))
    return values

def common(first, second):
    result = [i for i in first if i in second]
    return result

def only_in_first(first, second):
    result = [i for i in first if not (i in second)]
    return result
