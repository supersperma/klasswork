#Задание35
import numpy as np
A = np.random.randint(-10, 10, size=(7, 4))
print("Матрица A[7,4]:")
print(A)
positive_sums = [sum(filter(lambda x: x > 0, row)) for row in A]
print("\nОдномерный массив из сумм положительных элементов каждой строки матрицы:")
print(positive_sums)
#Задание36
import numpy as np
M = 5
N = 3
A = np.random.randint(-10, 10, size=(M, N))
print("Матрица A[{},{}]:\n{}".format(M, N, A))
column_means = np.mean(A, axis=0)
print("\nОдномерный массив из средних арифметических элементов каждого столбца матрицы:")
print(column_means)
#ЗАдание37
import numpy as np
M = 5
N = 3
A = np.random.randint(-10, 10, size=(M, N))
print("Матрица A[{},{}]:\n{}".format(M, N, A))
nonzero_counts = np.count_nonzero(A, axis=1)
print("\nОдномерный массив из количества ненулевых элементов каждой строки матрицы:")
print(nonzero_counts)
#ЗАдание38
import numpy as np
M = 4
N = 3
A = np.random.randint(-10, 10, size=(M, N))
print("Матрица A[{},{}]:\n{}".format(M, N, A))
neg_product = np.prod(A[A < 0].reshape(N, -1), axis=1)
print("\nОдномерный массив из произведений отрицательных элементов каждого столбца матрицы:")
print(neg_product)
#ЗАдание39
import numpy as np
M = 4
N = 3
A = np.random.randint(-10, 10, size=(M, N))
print("Матрица A[{},{}]:\n{}".format(M, N, A))
nonzero_count = np.count_nonzero(A, axis=1)
print("\nОдномерный массив из количества ненулевых элементов каждой строки матрицы:")
print(nonzero_count)
