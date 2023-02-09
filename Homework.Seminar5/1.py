#Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# 2, 3 -> 2**3 = 8 -> (2*2)*2 = 8


def degree(a,b):
    if b==1:
        return a
    else:
        return (degree(a,b-1) * a)


a = int(input('Введите A: '))
b = int(input('Введите B: '))
print(degree(a,b))