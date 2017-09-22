#game 'cube game"

from os import system
from time import sleep
from random import *
from init_cube1 import *
from init_cube2 import *
#main

print('                 Привет! Сейчас поиграем в игру "Кости"!')
print("")
print("1) Начать игру.")
print("2) Если ты не азартный человек, лучше и не начинай ;-)")
print("")

#Начало 

choice = 0
while choice != 1 and choice != 2:
    while True:
        choice = input("Ваш выбор : ")
        try:
            choice = int(choice)
            break
        except ValueError:
            print("Хитрец, жду ввода))))))))")
            
#Выбор режима игры (соло или мултиплей)


if choice == 1:
    system('cls')
    print("                               Начнем!")
    print(" ")
    print("                     И так ты азартный человек ;-)")
    print(" ")
    print("1) Игра в 2-ем")
    print("2) Игра с комьютером")
    print("")
    ch_mode = 0
    while ch_mode != 1 and ch_mode != 2:
        while True:
            ch_mode = input("Ваш выбор : ")
            try:
                ch_mode = int(ch_mode)
                break
            except ValueError:
                print("Хитрец, жду ввода))))))))")

#Игра мультиплей

    if ch_mode == 1:
        system('cls')
        print("                                  Начнем!")
        print("")
        print('                      Ваш выбор "Игра в 2-ем" !')
        print("")

#Вводим имена
        
        name1 = str(input("Введите Ваше имя : "))
        name2 = str(input("Введите имя соперника : "))

# Вводим баланс
    #проверка на ввод баланса
        system('cls')
        while True:
            print(name1)
            balans1 = input("Введите Ваш банк :")
            try:
                balans1 = int(balans1)
                if balans1 < 49 or balans1 > 1000:
                    print("Ваша ставка должна быть от 50 до 1000")
                    continue
                break
            except ValueError:
                print("Хитрец, жду ввода))))))))")
        while True:
            balans2 = input("Введите банк соперника :")
            try:
                balans2 = int(balans2)
                if balans2 < 49 or balans2 > 1000:
                    print("Банк должен быть минимум 50 $ и максимум 1000$")
                    continue
                break
            except ValueError:
                print("Хитрец, жду ввода))))))))))))))))")
        print("")
        print(name1,"Ваша банк :",balans1,"$ , банк игрока ",name2," :",balans2, "$")
        print("")

# Определяем кто первый кидает кости

        print("Теперь кинем кости и выберем кто первый начинает")
        print(name1, "Кидайте кости!!!")
        x=input("Нажмите Enter для продолжения.")
        system('cls')
        res1 = 0
        res2 = 0
        while True:
            for i in range(1, 10):
                init_cube1()
                init_cube2()
                sleep(0.2)
                system('cls')
            res1 = init_cube1() + init_cube2()
            print("")
            print("Ваш результат : ", res1)
            print(name2, "Кидайте кости!!!")
            x = input("Нажмите Enter для продолжения.")

            system('cls')
            for i in range(1, 10):
                init_cube1()
                init_cube2()
                sleep(0.2)
                system('cls')
            res2 = init_cube1() + init_cube2()
            print("")
            print("Результат ",res1, ":", res2)
            print("У игрока", name1," выпало:",res1, ", а у игрока",name2,"выпало:", res2)
            x = input("Нажмите Enter для продолжения.")

            if res1 == res2:
                x = input("Начнем заново!! Нажмите Enter для продолжения.")
                continue

# Игру начинает 1 игрок(Вы)

            elif res1 > res2:
                print("Игрок",name1,"начинаете первый!")
                rate1 = 0
                rate2 = 0
                system('cls')
                a=0
                while True:
                    a += 1

#Проверка на ввод ставки

                    while True:
                        print(name1)
                        rate1 = input("делаем ставку Вашу :")
                        try:
                            rate1 = int(rate1)
                            if rate1 < 1 or rate1 > balans1:
                                print("Ваша ставка должна быть от 1 до", balans1)
                                continue
                            break
                        except ValueError:
                            print("Хитрец, жду ввода))))))))))))))))")
                    while True:
                        print(name2)
                        rate2 = input("делаем ставку Вашу :")
                        try:
                            rate2 = int(rate2)
                            if rate2 < 1 or rate2 > balans2:
                                print("Ваша ставка должна быть от 1 до", balans2)
                                continue
                            break
                        except ValueError:
                            print("Хитрец, жду ввода))))))))))))))))")

#Игра

                    system('cls')
                    print("Cтавка игрока", name1,":", rate1, "$ ,а ставка ",name2, ":", rate2, "$")
                    print(" Игра №", a)
                    x = input("Нажмите Enter для продолжения.")

                    for i in range(1, 10):
                        init_cube1()
                        init_cube2()
                        sleep(0.2)
                        system('cls')
                    res1 = init_cube1() + init_cube2()
                    print("")
                    print("Результат игрока ",name1,":", res2)
                    print("Теперь кидает кости",name2)
                    x = input("Нажмите Enter для продолжения.")

                    system('cls')
                    for i in range(1, 10):
                        init_cube1()
                        init_cube2()
                        sleep(0.2)
                        system('cls')
                    res2 = init_cube1() + init_cube2()
                    print("")
                    print("Результат",name2,":", res2)
                    print("У игрока",name1," выпало : ", res1, ", а у игрока",name2," выпало : ", res2)
                    x = input("Нажмите Enter для продолжения.")
                    b = 0
                    if res1 > res2:
                        if rate1 > rate2:
                            balans1 += rate2
                            balans2 -= rate2
                        elif rate1 < rate2:
                            balans1 += rate1
                            balans2 -= rate1
                        else:
                            balans1 += rate1
                            balans2 -= rate2
                    elif res1 < res2:
                        if rate1 > rate2:
                            balans2 += rate2
                            balans1 -= rate2
                        elif rate1 < rate2:
                            balans2 += rate1
                            balans1 -= rate1
                        else:
                            balans2 += rate2
                            balans1 -= rate1
                    else:
                        x = input("Нажмите Enter для продолжения.")
                        continue

                    print("Ваш баланс : ", balans1, "$ ,баланс соперника =", balans2, "$")

                    if balans1 == 0:
                        print(name1, "проиграл!!! ",name2," выйграл : ", balans2, "$!")
                        x = input("Спасибо за игру!!!!Удачи и пух )))))))))))")
                        quit(1)
                    elif balans2 == 0:
                        print(name2, "Вы проиграли!!! ",name1," выйграл : ", balans1, "$!")
                        x = input("Спасибо за игру!!!!Удачи и пух )))))))))))")
                        quit(1)

# Игру начинает Ваш соперник
            elif res1 < res2:
                print("Игрок", name2, "начинаете первый!")
                rate1 = 0
                rate2 = 0
                system('cls')
                a = 0
                while True:
                    a += 1

# Проверка на ввод ставки

                    while True:
                        print(name2)
                        rate1 = input("делаем ставку Вашу :")
                        try:
                            rate1 = int(rate1)
                            if rate1 < 1 or rate1 > balans1:
                                print("Ваша ставка должна быть от 1 до", balans1)
                                continue
                            break
                        except ValueError:
                            print("Хитрец, жду ввода))))))))))))))))")
                    while True:
                        print(name1)
                        rate2 = input("делаем ставку Вашу :")
                        try:
                            rate2 = int(rate2)
                            if rate2 < 1 or rate2 > balans2:
                                print("Ваша ставка должна быть от 1 до", balans2)
                                continue
                            break
                        except ValueError:
                            print("Хитрец, жду ввода))))))))))))))))")

                            # Игра

                    system('cls')
                    print("Cтавка игрока", name2, ":", rate1, "$ ,а ставка ", name1, ":", rate2, "$")
                    print(" Игра №", a)
                    x = input("Нажмите Enter для продолжения.")

                    for i in range(1, 10):
                        init_cube1()
                        init_cube2()
                        sleep(0.2)
                        system('cls')
                    res1 = init_cube1() + init_cube2()
                    print("")
                    print("Ваш результат : ", res1)
                    print("Теперь кидает кости Ваш соперник")
                    x = input("Нажмите Enter для продолжения.")

                    system('cls')
                    for i in range(1, 10):
                        init_cube1()
                        init_cube2()
                        sleep(0.2)
                        system('cls')
                    res2 = init_cube1() + init_cube2()
                    print("")
                    print("Результат соперника : ", res2)
                    print("У игрока 1 ", res1, ", а у игрока 2", res2)
                    x = input("Нажмите Enter для продолжения.")
                    b = 0
                    if res1 > res2:
                        if rate1 > rate2:
                            balans1 += rate2
                            balans2 -= rate2
                        elif rate1 < rate2:
                            balans1 += rate1
                            balans2 -= rate1
                        else:
                            balans1 += rate1
                            balans2 -= rate2
                    elif res1 < res2:
                        if rate1 > rate2:
                            balans2 += rate2
                            balans1 -= rate2
                        elif rate1 < rate2:
                            balans2 += rate1
                            balans1 -= rate1
                        else:
                            balans2 += rate2
                            balans1 -= rate1
                    else:
                        x = input("Нажмите Enter для продолжения.")
                        continue

                    print("Ваш баланс : ", balans2, "$ ,баланс соперника =", balans1, "$")

                    if balans1 == 0:
                        print(name2, "проиграли!!!",name1," выйграл : ", balans2, "$!")
                        x = input("Спасибо за игру!!!!Удачи и пух )))))))))))")
                        quit(1)
                    elif balans2 == 0:
                        print(name1, "Вы проиграли!!!",name1," выйграл : ", balans1, "$!")
                        x = input("Спасибо за игру!!!!Удачи и пух )))))))))))")
                        quit(1)

#игра соло
        
    elif ch_mode == 2:
        balans = 0
        balansCom = 0
        print("Начнем!")
        print('Ваш выбор "Игра с комьютером" !')
        while True:
            balans = input("Введите ваш кеш :")
            try:
                balans = int(balans)
                if balans < 49 or balans > 1000:
                    print("Ваша ставка должна быть от 50 до 1000")
                    continue
                break
            except ValueError:
                print("Хитрец, жду ввода))))))))")
        balansCom = balans

# Проверка на ввод ставки


        a = 0
        while True:
            a += 1
            rate1 = 0
            while True:
                rate1 = input("Делаем ставку:")
                try:
                    rate1 = int(rate1)
                    if rate1 < 1 or rate1 > balans:
                        print("Ваша ставка должна быть от 1 до", balans)
                        continue
                    break
                except ValueError:
                    print("Хитрец, жду ввода))))))))))))))))")

            rate = rate1
            rate2=rate
            system('cls')
# Игра
            system('cls')
            print("Ваша ставка :", rate1, "$ ,а ставка комьютера :", rate2, "$")
            print(" Игра №", a)
            x = input("Нажмите Enter для продолжения.")

            for i in range(1, 10):
                init_cube1()
                init_cube2()
                sleep(0.2)
                system('cls')
            res1 = init_cube1() + init_cube2()
            print("")
            print("Ваш результат : ", res1)
            print("Теперь кидает кости комьютер")
            x = input("Нажмите Enter для продолжения.")

            system('cls')
            for i in range(1, 10):
                init_cube1()
                init_cube2()
                sleep(0.2)
                system('cls')
            res2 = init_cube1() + init_cube2()
            print("")
            print("Результат комьютера : ", res2)
            print("У Вас выпало : ", res1, ", а у комьютера :", res2)
            x = input("Нажмите Enter для продолжения.")

            if res1 > res2:
                balans += rate1
                balansCom -= rate1
            elif res1 < res2:
                balans -= rate1
                balansCom += rate1
            else:
                x = input("Нажмите Enter для продолжения.")
                continue

            print("Ваш баланс : ", balans, "$ ,баланс комьютера =", balansCom, "$")

            if balansCom == 0:
                print("Комьютер проиграл!!!А Вы выйграли : ", balans, "$!")
                x = input("Спасибо за игру!!!!Удачи и пух )))))))))))")
                quit(1)
            elif balans == 0:
                print("Вы проиграли!!!А комьютер выйграл : ", balansCom, "$!")
                x = input("Спасибо за игру!!!!Удачи и пух )))))))))))")
                quit(1)

else:
    quit(1)

    








