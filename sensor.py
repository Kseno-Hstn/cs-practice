porog = float(input())
n = int(input())
all, errors, excess, mx, sm = 0, 0, 0, 0, 0
for i in range(n):
    znach = input()
    all += 1
    if znach == 'error': errors += 1
    else:
        znach = float(znach)
        if znach >= mx:
            mx = znach
        if znach > porog:
            excess += 1
        sm += znach
print(f"Всего {all}")
print(f"Ошибки {errors}")
print(f"Превышения порога {excess}")
print(f"Максимальное значение{mx:1f}")
print(f"Среднее арифмитическое {sm/all:1f}")
