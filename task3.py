#3.Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
#*Пример:*
#- Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

from os import system
system("cls")
print("Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.")
n = int(input("Введите число n: "))
mplication = [(round((1+1/i)**i, 5)) for i in range(1, n+1)]
print(f"Список n чисел последовательности (1+1/n)^n: {mplication}")
print(f"Сумма n чисел последовательности (1+1/n)^n равна: {(sum(mplication))}")