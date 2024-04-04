#35
A = [[random.randint(-10, 10) for _ in range(4)] for _ in range(7)]
print("Матрица A[7,4]:")
for row in A:
    print(row)
positive_sums = [sum(max(0, num) for num in row) for row in A]
print("Список с суммами положительных элементов каждой строки:")
print(positive_sums)
#36
M = 5
N = 3
A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(M)]
print("Матрица A[{},{}]: ".format(M, N))
for row in A:
    print(row)
column_means = [sum(row[i] for row in A) / M for i in range(N)]
print("Средние арифметические каждого столбца матрицы:")
print(column_means)
#37
M = 4
N = 3
A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(M)]
print("Матрица A[{},{}]: ".format(M, N))
for row in A:
    print(row)
nonzero_counts = [sum(1 for element in row if element != 0) for row in A]
print("Количество ненулевых элементов в каждой строке матрицы:")
print(nonzero_counts)
