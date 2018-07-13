#1
import random
lst = []
i = 0
while i < 6:
    lst.append(random.randint(0,10))
    i += 1
print(lst)
print(list(map(lambda x: x*x, lst)))
#2

lst1 = ['яблоко','банан','груша','слива']
lst2 = ['абрикос','персик','киви','яблоко','груша']
lst = []
for el in lst1:
    for i in lst2:
        if el == i:
            lst.append(el)
print(lst)

#3
i = 0
lis1 = []
l = []
while i < 10:
    lis1.append(random.randint(0,1000))
    i += 1
print(lis1)

for elem in lis1:
    if elem % 3 == 0:
        if elem > 0:
            if elem % 4 != 0:
                l.append(elem)
print(l)                
