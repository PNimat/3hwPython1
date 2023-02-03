"""
5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
"""


def Febonachi(i):
    if i == 1 or i == 2:
        return 1
    else:
        i = Febonachi(i - 1) + Febonachi(i - 2)
        return i


def NeFebonachi(i):
    result = (-1) ** (i + 1) * Febonachi(i * (-1))
    return round(result)


number = int(input('Введите число '))

if number > 0:
    print(Febonachi(number))
elif number < 0:
    print(NeFebonachi(number))
