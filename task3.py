"""
3. Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
"""

my_lst = [1, 1, 3.1, 5, 10.01]
my_next = 0
while (my_lst[my_next] % 1) == 0:
    next += 1
# Для красоты запустил цикл, который найдет первый элемент с плавающей запятой

my_max, my_min = my_lst[my_next] % 1, my_lst[my_next] % 1

for i in my_lst:
    if (i % 1) != 0:
        i = round(i % 1, 2)
        if i > my_max:
            my_max = i
        if i < my_min:
            my_min = i

        print(round(my_max - my_min, 2))
