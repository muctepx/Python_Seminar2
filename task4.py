#4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
#-2 -1 0 1 2
#Позиции: 0,1 -> 2

from os import system
system("cls")
print("Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. \nПозиции хранятся в файле file.txt в одной строке одно число.")
with open("file.txt", "r") as f:
    pos = f.read().split("\n")
pos = list(map(int, pos))

n = int(input("Введите число N больше 0: "))
new_list = [i for i in range(-n, n+1)]
mplication = 1
for digit in pos:
    mplication *= new_list[digit]
print(f"Список [-N, N]: {new_list}")
print(f"Произведение элементов на позициях {pos}: {mplication}")