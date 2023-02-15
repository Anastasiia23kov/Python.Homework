#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
#заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7
#    1                   9        13 14           19
# 5 (min)
# 15 (max)
# -> [1, 9, 13, 14, 19]


arr = list(map(int,input("Введите  массив:").split()))
max1 = int(input('Введите MAX заданного диапазона: '))
min1 = int(input('Введите MIN заданного диапазона: '))
print(arr)

'''
for i in arr:
    if i >= min1 and i <= max1:
        print(arr.index(i), end=' ')
'''

result_arr = []
for i in arr:
    if i >= min1 and i <= max1:
        result_arr.append(arr.index(i))

print(result_arr)
