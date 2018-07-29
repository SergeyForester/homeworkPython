__author__ = 'Burik Sergey Sergeyevich'
import random
import sys
import time
while True:
    print('Loto')
#создаем нашу карту
    print('---------Ваша карта---------')
    def pl_card(card):
        num = []
        while len(num) < 5:
            elem = str(random.randint(1, 90))
            if elem not in card:
                num.append(elem)
                card.append(elem)
        num = list(num) + list(' ' * 12)
        random.shuffle(num)
        return ' '.join(num)

    card = []
    for _ in range(3):
        print(pl_card(card))
    print("------------------")

    print('---------Карта компьютера---------')
#создаем карту компьтера
    def c_card(comp_card):
        nums = []
        while len(nums) < 5:
            elem = str(random.randint(1, 90))
            if elem not in comp_card:
                nums.append(elem)
                comp_card.append(elem)
        nums = list(nums) + list(' ' * 12)
        random.shuffle(nums)
        return ' '.join(nums)


    comp_card = []
    for _ in range(3):
        print(c_st_ring(comp_card))
    print("------------------")
    '''
    мой ход
    '''
    step = 90
    score = 0
    if score == 15:
        print ('Вы победили')
    else:
        cask = random.randint(1, 91)
        print ('Вам выпал бочонок  с номером ', cask)
        human_ans = input('Зачеркнуть цифру?(д\н)')
        if human_ans == "д":
            if cask == card:
                print('Вы получили очко ',)
                card.remove(cask)
                b = step - 1
            elif cask != card:
                print('Вы проиграли!!!!!')
        if human_ans == "н":
            if cask == card:
                print (
                "Вы проиграли потому, что он выбрал\n не заркивать цифру", cask, "хоть она там была")
            if cask != temp:
                print ('Игра продолжается')

                for _ in range(3):
                    print(st_ring(card))

                for _ in range(3):
                    print(c_st_ring(comp_card))

    '''
    ход компьютера
    '''
    comp_step = 90
    comp_score = 0

            comp_cask = random.randint(1, 91)
            print ('Компьтеру выпал бочонок  с номером ',comp_cask)
            comp_ans = random.randint(1, 2)
            if comp_ans == 1:
                if boch_comp == comp_card:
                    print('Компьютер получил очко ',)
                    comp_card.remove(comp_cask)
                    a = comp_step - 1
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

