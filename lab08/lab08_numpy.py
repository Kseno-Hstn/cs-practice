import numpy as np

#Задание 1
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
print(line)
zero = np.zeros(6, int)
unknown_table = np.full((2,3), -1)
identity = np.full((3,3), 1)
print(hours, f'Форма {hours.shape}',
      f'Кол-во осей {hours.ndim}',
      f'Общее кол-во элементов {hours.size}',
      f'Тип данных {hours.dtype}', sep='\n', end='\n')

#Задание 2
print(f'Третий элемент {hours[2]}',
      f'Последний элемент {hours[-1]}',
      f'Элементы с индексами 2–5: {hours[1:4]}',
      f'Каждый второй элемент: {hours[::2]}',
      f'Массив в оратном порядке: {hours[-1:-9:-1]}', sep='\n', end='\n')

#Задание 3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18], ])
print('ЗАДАНИЕ 3')
print(f'Форма {temperatures.shape}',
      f'Число измерений {temperatures.ndim}, форма {temperatures.shape}',
      f'Число элементов {temperatures.size}',
      f'Значение из второй строки и третьего столбца {temperatures[1,2]}, форма {temperatures[1,2].shape}',
      f'Первая строка: {temperatures[0]}, форма {temperatures[0].shape}',
      f'Последний столбец: {temperatures[:, -1]}, форма {temperatures[:, -1].shape}',
      f'Первые две строки без первого столбца: {temperatures[1:4, :3]}, форма {temperatures.shape}',
      f'Фрагмент: {temperatures[0:1, 1:2]}, форма {temperatures[0:1, 1:2].shape}', sep='\n', end='\n')

#Задание 4
matrix = np.arange(1, 26).reshape(5, 5)
print('ЗАДАНИЕ 4')
print(f'Первые три строки {matrix[:3]}, форма {matrix[:3].shape}',
      f'Последние две строки {matrix[-1:-3]}, форма {matrix[-1:-3].shape}',
      f'Первые два столбца {matrix[:, :2]}, форма {matrix[:, :2].shape}',
      f' фрагмент из строк с индексами 1–3 и столбцов 2–4 {matrix[0:3,1:4]}, форма {matrix[0:3,1:4].shape}',
      f'угловой блок 2×2 в правом нижнем углу {matrix[-2:,-2:]}, форма {matrix[-2:,-2:].shape}',
      sep='\n', end='\n')

#Задание 5
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print('ЗАДАНИЕ 5', f'Новый hours: {changed_hours}', sep='\n', end='\n')
changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print(changed_matrix * 0.5)
print(f'Исходная матрица: {matrix}', f'Новая матрица: {changed_matrix}', sep='/n')

#Задание 6
numbers = np.arange(12)
table = numbers.reshape(3,4)
transposed = table.T
print(numbers.shape, table.shape, transposed.shape)


