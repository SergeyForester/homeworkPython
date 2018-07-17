import os
n = ['1. Перейти в папку','2. Просмотреть содержимое текущей папки','3. Удалить папку','4. Создать папку']
for i in n:
    print(i)
per_ch = input('Выберите что-нибудь\n (необходимое число)')
if per_ch == '1':
    move_dir = input('Название переходящей папки ')
    try:
        os.chdir(move_dir)
        print("Успешно перемещены")
    except:
        print('Неудается найти папку')
if per_ch == '2':
    print(os.listdir(os.getcwd()))
    print("Просмотр папок")
if per_ch == '3':
    name_dir = input('Название папки которую надо удалить')
    try:
        os.rmdir(name_dir)
        print("Успешно удалены")
    except:
        print('Папки уже удалены или не найдены')
if per_ch == '4':
    n_dir = input('Название папки')
    try:
        os.mkdir(n_dir)
        print('Успешно созданы')
    except:
         print('Папки уже удалены')



