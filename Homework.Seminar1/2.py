# Задача 2. Найдите сумму цифр трехзначного числа.
# 123 -> 1+2+3 = 6 

a = int (input("Введите трехзначное число: "))

print (int((a%10) + (a%100)/10 + (a/100)))