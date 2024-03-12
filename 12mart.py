m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']
m.remove(0.25)
m.remove(15)
m.remove('10')
print(m)
#Задание2
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
del abc[1] 
del abc[1:4]
print(abc)
#Задание3
numbers = [1, 4]
min_num = min(numbers)
max_num = max(numbers)

for num in range(min_num+1, max_num):
    for i in range(len(numbers)):
        if num < numbers[i]:
            numbers.insert(i, num)
            break
    else:
        numbers.append(num)
print(numbers)
#задние4
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
mass = [num for num in mass if num >= 0]
mass.sort()
print("По возрастанию:", mass)
mass.sort(reverse=True)
print("По убыванию:", mass)
#Задание5
n = int(input("введите количество чисел: "))
numbers = list(map(int, input("введите числа: ").split()))
a = sum(num for num in numbers if num < 0)
r = [num for num in numbers if num > 0]
e = sum(r) / len(r) if r else 0
z = [num for num in numbers if num == 0]
for z in z:
    numbers.remove(z)
print(f"Сумма чисел списка с отрицательными числами: {a}")
print(f"Среднее арифметическое списка с положительными числами: {e}")
print("Список без нулей:")
print(numbers)
