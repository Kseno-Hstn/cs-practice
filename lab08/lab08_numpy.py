import numpy as np

#Задание 1
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zero = np.zeros(6, int)
unknown_table = np.full((2,3), -1)
identity = np.full((3,3), 1)
print(hours, f'Форма {hours.shape}',
      f'Кол-во осей {hours.ndim}',
      f'Общее кол-во элементов {hours.size}',
      f'Тип данных {hours.dtype}', sep='\n')

