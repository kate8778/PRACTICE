# Напишите программу
# Камера наблюдения регистрирует скорости автомобилей
# Необходимо определить среднюю зарегестрированную скорость всех автомобилей 

number_of_cars = int(input())
sum_v = 0

for i in range(number_of_cars):
    v = int(input())
    sum_v += v

print(f"Средняя скорось: {sum_v/number_of_cars}")