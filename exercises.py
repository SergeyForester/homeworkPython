#1
def arithmetic(a, b, oper):
	if oper == '+':
		return a + b
	elif oper == '-':
		return a - b
	elif oper == '/':
		if b != 0:
			return a / b
		else:
			return 'Невозможно выполнить операцию'
	elif oper == '*':
		return a * b
	else:
		return 'ты шо дурак!!'

print(arithmetic(1,0, '/'))		
#2
def is_year_leap(year):
	if year % 4 == 0:
		if year % 400 == 0:
			return 'Год {} високосный'.format(year)
	else:
		return 'Год {} не високосный'.format(year)

print(is_year_leap(2019))			

#3
import math

def square(sideOfSquare):
	perOfS = sideOfSquare * 4
	sOfS = sideOfSquare ** 2
	diagOfS = sideOfSquare * math.sqrt(2)
	return (perOfS, sOfS, diagOfS)

print(square(10))


#4
def season(month):
	if month >=3 and month <= 5:
		return 'весна'
	elif month >= 6 and month <= 8:	
		return 'лето'
	elif month >= 9 and month <= 11:
		return 'осень'
	elif month == 12 or month == 1 or month == 2:
		return 'зима'
	else:
		return 'нет такого месяца'	
print(season(2))

#5
def is_prime(n):
	if n < 1000 and n < 0:
		return 'Неверно задно значение' 
	else:
		if n % n == 0 and n % 1 == 0 and n % 2 !=0:
			return 'Число {} простое'.format(n)
		else:
			return 'Число {} не простое'.format(n)	

print(is_prime(2))

#6
char = input()
word = input()

score = 0
for i in word:
	if i == char:
		score += 1
		continue
	else:
		continue	
print(score)

#7
n = [int(i) for i in input().split()]
num = 0
for i in range(len(n) - 1):
	n[i] %= 100
print(max(n))

R = input().split()
c = 0
for x in R:
	 if x[0] == 'R':
	 	c += 1
print(c)	 	

#8
R = input().split()
c = 0
for each in R:
    if each[0] == 'R':
        c += 1
print(c)