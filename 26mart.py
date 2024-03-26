#Задание1
ar1 = [3, 7, 2, 5, 3, 9, 8, 4, 1, 6, 5, 2, 7, 3, 8, 9, 4]
ar2 = [5, 1, 9, 2, 4, 6, 3, 8, 7, 2, 1, 4, 6, 9, 5, 7, 8, 3, 31, 55, 73, 89]
unique = set(ar1 + ar2)
ar3 = list(unique)
print("Первый массив:", ar1)
print("Второй массив:", ar2)
print("Третий массив (уникальные элементы):", ar3)
#Задание2
B = [
    [1, 0, 3],
    [0, 5, 0],
    [7, 8, 9]
]
print("Матрица B:")
for row in B:
    print(row)
non_zero_count = sum(1 for row in B for element in row if element != 0)
print("Количество ненулевых элементов:", non_zero_count)
#Здание3
B = [
    [-1, 2, 3],
    [4, 5, 6],
    [7, 8, -9]
]
# Вывести матрицу B
print("Матрица B:")
for row in B:
    print(row)
negative_product = 1
for row in B:
    for element in row:
        if element < 0:
            negative_product *= element
print("Произведение отрицательных элементов:", negative_product)
#задание4
import random
M = 3
N = 4
B = [[random.uniform(-10, 10) for _ in range(N)] for _ in range(M)]
print("Матрица B:")
for row in B:
    print(row)
positive_product = 1
for row in B:
    for element in row:
        if element > 0:
            positive_product *= element
print("Произведение положительных элементов:", positive_product)
#Задание5
import random
# Задаем размеры матрицы
M = 3
N = 4
B = [[random.uniform(-10, 10) for _ in range(N)] for _ in range(M)]
print("Матрица B:")
for row in B:
    print(row)
min_element = min(min(row) for row in B)
print("Минимальный элемент в матрице B:", min_element)
