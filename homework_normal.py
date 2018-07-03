__author__ = 'Бурик Сергей Сергеевич'

#1
n = 0
num = input('Введите целое число: ')
for i in num:
    if (int(i)) > n:
        n = int(i)
print(n)

#2
a = int(input('Введите число A ')) 
b = int(input('Введите число B '))

print('a = ', a, 'b = ', b)
a, b = b, a
print('a = {0}, b = {1}'.format(a, b))

#3
import math
a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = -b + math.sqrt(d) / 2*a
    x2 = -b - math.sqrt(d) / 2 *a
    print('Корни уравнения: ', x1, x2)
if d == 0:
    x = -b / 2*a
    print('Корни уравнения: ', x)
if d < 0:
    print('НЕТ корней')





