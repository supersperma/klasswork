#Задача 11
def compare_speed():
    a = float(input("Введите скорость в км/ч: "))
    b = float(input("Введите скорость в м/сек: "))
    
    kmh_to_ms = a / 3.6
    
    if kmh_to_ms > b:
        print(f"Скорость в км/ч ({a}) больше скорости в м/сек ({b})")
    elif kmh_to_ms < b:
        print(f"Скорость в м/сек ({b}) больше скорости в км/ч ({a})")
    else:
        print("Скорости равны")

compare_speed()

#Задача 2
radius = float(input("Введите радиус круга: "))
side = float(input("Введите сторону квадрата: "))

circle_area = 3.14159 * radius**2
square_area = side**2

if circle_area > square_area:
    print("Площадь круга больше площади квадрата.")
elif circle_area < square_area:
    print("Площадь квадрата больше площади круга.")
else:
    print("Площади круга и квадрата равны.")
