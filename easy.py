__author__ = 'Бурик Сергей Сергеевич'
#1
fruits = ["яблоко", "банан", "киви", "арбуз"]
for num, fruit in enumerate (fruits):
    print(str(num)+ ' . {:>7}'.format(fruit))

          
#2


veg = ['огурец', 'помидор', 'капуста', "морковь"]
veg_fru = ['огурец','ананас','лимон', '''\nкиви''', 'арбуз', 'помидор', '''\nкапуста''', "морковь"]
print('Список овощей {}'.format(veg), 'Список овощей и фруктов {}'.format(veg_fru))
for v in veg[:]:
    for vf in veg_fru[:]:
        if v == vf:
            veg_fru.remove(vf)
print('Только фрукты {}'.format(veg_fru))            
            
#3
num = []
new_num = []
for i in range(1,10):
    num.append(i)
print(num)

for el in reversed(num):
     count = num.index(el)
     if (el % 2) == 0:
         new_el= el/4
         new_num.insert(0, new_el)
         num.remove(el)

     else:
         el = el*2
         num[count] = el

print(new_num)
    
