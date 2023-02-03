"""
2. Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
"""
# Вариант 1
new_lst = []
left = 0
right = -1

my_lst = [2, 3, 4, 5, 6]
long = len(my_lst) / 2
for i in my_lst:
    if (left < long):
        new_lst.append(my_lst[left] * my_lst[right])
    right -= 1
    left += 1
print(new_lst)

# Вариант 2
# Здесь немного замудрил: хотел сразу перезаписывать 1 индекс и удалять последний ( криво, косо, но получилось)))  )

my_lst = [2, 3, 4, 5]
long = round(len(my_lst) / 2 + 0.5)

count = 0
for i in my_lst:
    if count < long:
        my_lst[count] = i * my_lst[-1]
        if count < long - 1:
            my_lst.pop(-1)
        count += 1
my_lst = my_lst[0:long]
print(my_lst)
