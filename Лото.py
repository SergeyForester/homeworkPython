__author__ = 'Burik Sergey Sergeyevich'
import random
import sys
import time
while True:
    print('Loto')
#создаем нашу карту
    print('---------Ваша карта---------')
    def st_ring(temp):
        nums = []
        while len(nums) < 5:
            elem = str(random.randint(1, 90))
            if elem not in temp:
                nums.append(elem)
                temp.append(elem)
        nums = list(nums) + list(' ' * 12)
        random.shuffle(nums)
        return ' '.join(nums)

    temp = []
    for _ in range(3):
        print(st_ring(temp))
    print("------------------")

    print('---------Карта компьютера---------')
#создаем карту компьтера
    def с_st_ring(kart):
        nums = []
        while len(nums) < 5:
            elem = str(random.randint(1, 90))
            if elem not in temp:
                nums.append(elem)
                temp.append(elem)
        nums = list(nums) + list(' ' * 12)
        random.shuffle(nums)
        return ' '.join(nums)

    kart = []
    for _ in range(3):
        print(c_st_ring(kart))

    print("------------------")
    '''
    мой ход
    '''

    score = 0
    if score == 15:
        print ('Вы победили')
    else:
        boch = random.randint(1, 91)
        print ('Вам выпал бочонок  с номером ', boch,)
        human_ans = input('Зачеркнуть цифру?(д\н)')
        if comp_ans == "д":
            if boch == kart:
                print('Компьютер получил очко ',)
                temp.remove(boch)
                b = hod - 1
            elif boch != temp:
                print('Компьютер проиграл!!!!!')
        if human_ans_ans == "н":
            if boch_ == temp:
                print (
                "Вы проиграли потому, что он выбрал\n не заркивать цифру", boch_comp, "хоть она там была")
            if boch != temp:
                print ('Игра продолжается')

                for _ in range(3):
                    print(st_ring(temp))

                for _ in range(3):
                    print(c_st_ring(kart))

    '''
    ход компьютера
    '''
    comp_score = 0
    if comp_score == 15:
        print ('Компьтер выиграл')
    else:
        boch_comp = random.randint(1, 91)
        print ('Компьтеру выпал бочонок  с номером ',boch_comp,)
        comp = random.randint(1, 2)
        if comp_ans == 1:
            if boch_comp == kart:
                print('Компьютер получил очко ',)
                kart.remove(boch_comp)
                b = hod - 1
            elif boch != kart:
                print('Компьютер проиграл!!!!!')
        if comp_ans == 2:
            if boch_comp == kart:
                print ("Компьтер проиграл потому, что он выбрал\n не заркивать цифру", boch_comp,"хоть она там была")
            if boch_comp != kart:
                print ('Игра продолжается')

                for _ in range(3):
                    print(st_ring(temp))

                for _ in range(3):
                    print(c_st_ring(kart))


