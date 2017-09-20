#game 'cube game'
from os import system
from time import sleep
from random import *
from ch_who_first import *
from init_cube1 import *
from init_cube2 import *
from play_mode import *
#main

print('        Привет! Сейчас поиграем в игру "Кости"!')
print("1) Начать игру.")
print("2) Если ты не азартный человек, лучше и не начинай ;-)")

#Начало 

choice=0
while choice!=1 and choice!=2:
    while True:
        choice = input("Ваш выбор : ")
        try:
            choice = int(choice)
            break
        except ValueError:
            print("Ваш выбор : ")
            
#Выбор режима игры (соло или мултиплей)

    #игра мультиплей
if choice==1: 
    print("Начнем!")
    print("И так ты азартный человек ;-)")
    print("1) Игра в 2-ем")
    print("2) Игра с комьютером")
    ch_mode=0
    while ch_mode!=1 and ch_mode!=2:
        while True:
            ch_mode = input("Ваш выбор : ")
            try:
                ch_mode = int(ch_mode)
                break
            except ValueError:
                print("Ваш выбор : ")
    if ch_mode == 1:
        print("Начнем!")
        print('Ваш выбор "Игра в 2-ем" !')

    #Вводим имена
        
        name1 = str(input("Введите ваше имя : "))
        name2 = str(input("Введите имя соперника : "))
        print("Начнем!")
        print('Ваш выбор "Игра в 2-ем" !')
        
        #Вводим баланс
        
        while True:
            balans1 = input("Введите ваш кеш :")
            try:
                balans1 = int(balans1)
                if balans1<49 or balans1>1000:
                    print("Ваша ставка должна быть от 50 до 1000")
                    continue
                break
            except ValueError:
                print("Хитрец, разве $ у нас буквы?))))))))")
                
        while True:
            balans2 = input("Введите кеш соперника :")
            try:
                balans2 = int(balans2)
                if balans2<49 or balans2>1000:
                    print("Ваша ставка должна быть от 50 до 1000")
                    continue
                break
            except ValueError:
                print("Хитрец, разве $ у нас буквы?))))))))")
        print("Ваша ставка =",balans1,"$ и ставка соперника =",balans2, "$")
        print("Теперь кинем кости и выберем кто первый начинает")
        x=input("Нажимаем что Вам угодно и начинаем ;-)")

        #Определяем кто первый кидает кости 

        ch_who_first()

        #Игру начинает 1 игрок(Вы)
        rate1=0
        rete2=0
        a=1
        if ch_who_first()==1:
            x=input("И так Вы начинаете первый!! Нажимаем что Вам угодно ;-)")
            while True:
                while True:
                    rate1 = input("Делаем ставку Вашу :")
                    try:
                        rate1 = int(rate1)
                        if rate1<1 or rate1 > balans1:
                            print("Ваша ставка должна быть от 1 до",balans1)
                            continue
                        break
                    except ValueError:
                        print("Хитрец, разве $ у нас буквы?))))))))")
                while True:
                    rate2 = input("Ставка противника :")
                    try:
                        rate2 = int(rate1)
                        if rate2<1 or rate2 > balans2:
                            print("Ваша ставка должна быть от 1 до",balans2)
                            continue
                        break
                    except ValueError:
                        print("Хитрец, разве $ у нас буквы?))))))))")

                print("Ваша ставка =",rate1,"$ и ставка соперника =",rate2, "$")
                x=input("   Кидаем кости! Игра ",a," \n         !! Нажимаем что Вам угодно ;-)")

                play_mode1()

                if play_mode1()==1:
                    a+=a
                    if rate1>rate2:
                        a=rate2
                        balans1+=a
                        balans2-=a
                    elif rate1<rate2:
                        a=rate1
                        balans1+=a
                        balans2-=a
                print("Ваша баланс : ",balans1,"$ ,баланс соперника =",balans2, "$")
                x=input("   Кидаем кости! Игра ",a," \n         !! Нажимаем что Вам угодно ;-)")
                if balans1==0 or balans2==0:
                    break

    #игра соло
        
    elif ch_mode == 2:
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
else:
    quit

    








