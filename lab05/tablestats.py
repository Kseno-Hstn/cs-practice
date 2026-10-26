def read_rows(lines):
    flag = False
    result = []
    for i in lines:
        cleaned_line = i.strip()
        if not cleaned_line:
            continue
        if not flag:
            zagolovok = [j.strip() for i in cleaned_line.split(',')]
            flag = True
            continue
        znacheniya = [x.strip() for x in i.split(',')]
        if len(znacheniya) != len(zagolovok):
            continue
        slovar = dict(zip(zagolovok, znacheniya)
        result.append(slovar)
    return result

def count_types(rows):
    result = {}
    for i in rows:
        value_type = i['тип']
        if value_type in result:
            result[value_type] += 1
        else:
            result[value_type] = 1
    return result
