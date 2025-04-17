# Напишите программу
# Камера наблюдения регистрирует скорости автомобилей
# Необходимо определить среднюю зарегестрированную скорость всех автомобилей 
# Если скорость хотя бы 1 автомобиля была больше 60 км/ч, напечатать yes.

number_of_cars = int(input())
sum_v = 0
check = 0

for i in range(number_of_cars):
    v = int(input())
    sum_v += v
    if v >= 60:
        check = 13
    

print(f"Средняя скорось: {sum_v/number_of_cars}")
if check == 1:
    print("YES")