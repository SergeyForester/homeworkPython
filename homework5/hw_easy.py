#1
import os
def make_dir():
    try:
        for i in range(1, 10):
            os.mkdir("dir_" + str(i))
    except:
        print('Уже сушествуют')


def remove_dir():
    try:
        for i in range(1, 10):
            os.rmdir("dir_" + str(i))
    except:
        print('Папки уже удалены')
do = {'mkdir':make_dir,'remdir':remove_dir}

#2
def list_dir():
    print(os.listdir(os.getcwd()))
#3
from shutil import copyfile, copy
def copy_file():
    copy(r'hw_easy', r'hw_easy_new.py')
copy_file()