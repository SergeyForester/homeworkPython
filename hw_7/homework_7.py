__author__ = 'Burik Sergey Sergeyevich'
import random
import sys
import time
while True:
#     print('Loto')
#     print('---------Ваша карта---------')
#     def st_ring(temp):
#         nums = []
#         while len(nums) < 5:
#             elem = str(random.randint(1, 90))
#             if elem not in temp:
#                 nums.append(elem)
#                 temp.append(elem)
#         nums = list(nums) + list(' ' * 12)
#         random.shuffle(nums)
#         return ' '.join(nums)
#
#     temp = []
#     for _ in range(3):
#         print(st_ring(temp))
#     print("------------------")
#
#     print('---------Карта компьютера---------')
#
#     def с_st_ring(kart):
#         nums = []
#         while len(nums) < 5:
#             elem = str(random.randint(1, 90))
#             if elem not in temp:
#                 nums.append(elem)
#                 temp.append(elem)
#         nums = list(nums) + list(' ' * 12)
#         random.shuffle(nums)
#         return ' '.join(nums)
#
#     kart = []
#     for _ in range(3):
#         print(c_st_ring(kart))
#     print("------------------")
#     boch = random.randint(1, 91)
#     print('Вам выпал бочонок',boch)
#     human_ans = int(input('Зачеркнуть цифру? (1.y/2.n)'))
#     if human_ans == 1:
#         if boch == temp:
#             print('Вы победили')
#         elif boch != temp:
#             print('Вы проиграли!!!!!')
#     if human_ans == 2:
#         for _ in range(3):
#             print(st_ring(temp))
#
#         for _ in range(3):
#             print(c_st_ring(kart))
    class Cask:
        # Достаем бочонки по 1 штуке
        def f(self):
            lst = [x for x in range(1, self.amount + 1)]
            random.shuffle(lst)
            for i, y in enumerate(lst):
                print('{:*^30}'.format('*'))
                print('Новый бочонок: {} (осталось {})'.format(y, self.amount - (i + 1)))
                yield y

        def __init__(self, amount):
            self.amount = amount
            self.gen = self.f()


    class Loto:
        # Нарезаем карточки
        def __set_card(self):
            num = set()
            while len(num) < self.all_row * 5:
                num.add(random.randint(1, 91))
            cards = list(num)
            random.shuffle(cards)

            while len(cards) % self.all_row != 0:
                cards.append('None')
            self.all_row = int(len(cards) / self.all_row)
            cards = [cards[i: i + self.all_row] for i in range(0, len(cards), self.all_row)]

            for i in range(len(cards)):
                cards[i].sort()
            self.card_user = cards[:3]
            self.card_comp = cards[3:]

        def __init__(self, amount_card):
            row = 3
            self.all_row = row * amount_card
            self.__set_card()

        def get_card(self, card_player):
            print('{:-^25}'.format(self.name))
            print('{0[0]:>2} {0[1]:<10} {0[2]:<5} {0[3]} {0[4]} '.format(card_player[0]))
            print('{0[0]:>4} {0[1]:<6} {0[2]:<4} {0[3]:<4} {0[4]} '.format(card_player[1]))
            print('{0[0]} {0[1]:<5} {0[2]:<5} {0[3]:<5} {0[4]} '.format(card_player[2]))
            print('{:-^25}'.format('-'))

        # Поиск номера на карточке и определение победителя
        def search(self, card_player, num_cask):
            for i, n in enumerate(card_player):
                if num_cask in n:
                    card_player[i][n.index(num_cask)] = '-'
                    self.score += 1
                    if self.score == 15:
                        print('{} Победила!'.format(self.name))
                        sys.exit(1)
                    return True
            return False


    class Player(Loto):

        def __init__(self, name):
            self.name = name
            self.score = 0


    def main():
        game = Loto(2)
        cask = Cask(90)
        player1 = Player('Ваша карточка')
        player2 = Player('Карточка компьютера')

        while True:
            num_cask = next(cask.gen)
            player1.get_card(game.card_user)
            player2.get_card(game.card_comp)

            inp_user = input('Зачеркнуть цифру? (y/n)')
            if inp_user == 'y':
                if player1.search(game.card_user, num_cask):
                    continue
                else:
                    print('Game Over')
                    sys.exit(1)
            if inp_user == 'n':
                if player1.search(game.card_user, num_cask):
                    print('Game Over')
                    sys.exit(1)
                elif player2.search(game.card_comp, num_cask):
                    continue
            if inp_user != 'n' and inp_user != 'y':
                print('Введите y or n')
                time.sleep(1)
                continue


    if __name__ == '__main__':
        main()