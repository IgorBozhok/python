#game 'Black jack'

from os import system
from time import sleep
from random import *
#from random import shuffle


def test(choice):
    while True:
        choice = input("Ваш выбор : ")
        try:
            choice = int(choice)
            break
        except ValueError:
            print("Хитрец, жду ввода))))))))")
    return choice

def test1(karta):

    if karta == 'A':
        return 11
    elif karta == 'J' or karta == 'D' or karta == 'K':
        return 10
    else:
        return karta


#main
print('                 Привет! Сейчас поиграем в игру "Black jack "!')
print("")
print("1) Начать игру.")
print("2) Если ты не азартный человек, лучше и не начинай ;-)")
print("")

#Начало
while choice != 1 and choice != 2:
    choice = test(choice)


#Вводим имя.

if choice == 1:

    name1 = str(input("Введите Ваше имя : "))
    print("Начинаем",name1)
    system('cls')
    koloda = [6,7,8,9,10,'J','Q','K','A']*4
    shuffle(koloda)
    sum1=0
    sum2=0
    KarPlayer = []
    KarDiler = []
# 1 Ход
    for q in range (0,2):
        karta=koloda.pop()
        KarPlayer.append(karta)
        karta1=test1(karta)
        sum1 +=karta1
    if sum1==22:
        print("Ваши карты", name1)
        print(KarPlayer, "Black jack")
    else:
        print("Ваши карты", name1)
        print(KarPlayer, " = ", sum1)

    for q in range (0,2):
        karta=koloda.pop()
        KarDiler.append(karta)
        karta2=test1(karta)
        sum2 +=karta2
    if sum2 == 22:
        print("Карты Diler")
        print(KarDiler, " = ", sum2)
    else:
        print("Карты Diler")
        print(KarDiler, " = ", sum2)
    print (name1, ", если берем карту, то жмем 1")
    print("Если нет, то жмем 2")

# играем дальше
    choice
    while choice !=2:
        while choice != 1 and choice != 2:
            choice = test(choice)
        if choice == 1:
            karta = koloda.pop()
            KarPlayer.append(karta)
            karta1 = test1(karta)
            sum1 += karta1
            if sum1 == 22:
                print("Ваши карты", name1)
                print(KarPlayer, "Black jack")
            else:
                print("Ваши карты", name1)
                print(KarPlayer, " = ", sum1)
            karta = koloda.pop()
            KarDiler.append(karta)
            karta2 = test1(karta)
            sum2 += karta2
            if sum2 == 22:
                print("Карты Diler")
                print(KarDiler, " = ", sum2)
            else:
                print("Карты Diler")
                print(KarDiler, " = ", sum2)
        print(name1, ", если берем карту, то жмем 1")
        print("Если нет, то жмем 2")
        while choice != 1 and choice != 2:
            choice = test(choice)

        else:
             quit(1)




##     print(koloda)

# shuffle(koloda)
# print(koloda)
# karta = koloda.pop()
# print(karta)

else:
    quit(1)