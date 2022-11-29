#5'. Реализуйте алгоритм перемешивания списка.

from os import system
from random import shuffle
from random import randint
system("cls")
print("Реализуйте алгоритм перемешивания списка.")
print("Напечатайте список через пробел: ")
new_list = list(map(int, input().split()))
for i in range(len(new_list)-1):
    n = randint(0, len(new_list)-1)
    new_list[i], new_list[n] = new_list[n], new_list[i]
print(f"Перемешаный список: {new_list}")