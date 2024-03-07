#Задание 6
N = int(input())
i = 1
while i < N:
    print(i)
    i += 1
#Задание 7
a = int(input())
n = 1
sum = 0

while True:
    sum += 1/n
    if sum > a:
        break
    n += 1

print("Натуральные числа n, при которых выполняется условие 1 + 1/2 + 1/3 + ... + 1/n > a:")
print(list(range(1, n)))

#Задание # 8
n = int(input("Введите число n: ")) 

i = 1
while i*i <= n:
    i += 1

print(f"Первое натуральное число, квадрат которого больше {n}, равно {i}")
