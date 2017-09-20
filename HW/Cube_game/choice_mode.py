from init_cube1 import *
from init_cube2 import *
from ch_who_first import *


def balans1 ():
    while True:
        balans1 = input("Введите ваш кеш :")
        try:
            balans1 = int(balans1)
            if balans1<49 or balans1>300:
                print("Ваша ставка должна быть от 50 до 300")
                continue
            break
        except ValueError:
            print("Хитрец, разве $ у нас буквы?))))))))")
    return balans1

def balans2 ():
    while True:
        balans2 = input("Введите кеш соперника :")
        try:
            balans2 = int(balans2)
            if balans2<49 or balans2>300:
                print("Ваша ставка должна быть от 50 до 300")
                continue
            break
        except ValueError:
            print("Хитрец, разве $ у нас буквы?))))))))")
    print("Ваша ставка =",balans1(),"$ и ставка соперника =",balans2, "$")
    print("Теперь кинем кости и выберем кто первый начинает")
    x=input("Нажимаем что Вам угодно и начинаем ;-)")
    return balans2 

    print(balans1())
    print(balans2())
    
    ##print(ch_who_first ())
    
    x=input("Вы начинаете первый!! Нажимаем что Вам угодно ;-)")
    
def mode_single():
    balans=0
    print("Начнем!")
    print('Ваш выбор "Игра с комьютером" !')
    while True:
        balans = input("Введите ваш кеш :")
        try:
            balans = int(balans)
            if balans<49 or balans>300:
                print("Ваша ставка должна быть от 50 до 300")
                continue
            break
        except ValueError:
            print("Хитрец, разве $ у нас буквы?))))))))")
          


    
