from tablestats import read_rows, count_types, total_minutes, to_csv

name = input().strip()
with open(name, encoding='utf-8') as table:
    rows = read_rows(table)
counts = count_types(rows)
error_minutes = total_minutes(rows, "ошибка")
print(len(rows))
print(len(counts))
print(error_minutes)
result_csv = to_csv(counts)
with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(result_csv)
