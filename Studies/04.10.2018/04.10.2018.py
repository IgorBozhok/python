# game 'Black jack'

from os import system
from time import sleep
from random import *
from random import shuffle


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
    elif karta == 'J' or karta == 'Q' or karta == 'K':
        return 10
    else:
        return int(karta)
def sum(sum1,karta):
    return int(sum1 + karta)

# main
sum1 = 0
sum2 = 0
print('                 Привет! Сейчас поиграем в игру "Black jack "!')
name1 = str(input("Введите Ваше имя : "))
print("")
print("1) Начать игру.")
print("2) Если ты не азартный человек, лучше и не начинай ;-)")
print("")

# Начало

choice = ""
while choice != '1' and choice != '2':
    choice = input("Ваш выбор :")



#Вводим имя.
if choice == '1':


    print("Начинаем",name1)
    system('cls')
    koloda = [6,7,8,9,10,'J','Q','K','A']*4
    shuffle(koloda)
    KarPlayer = []
    KarDiler = []
# 1 Ход

    for q in range (0,2):
        karta=koloda.pop()
        KarPlayer.append(karta)
        sum1 =sum(sum1,test1(karta))
    if sum1==22:
        print("Ваши карты", name1)
        print(KarPlayer, "Black jack")
    else:
        print("Ваши карты", name1)
        print(KarPlayer, " = ", sum1)

    for q in range (0,2):
        karta=koloda.pop()
        KarDiler.append(karta)
        sum2 = sum(sum2, test1(karta))
    if sum2 == 22:
        print("Карты Diler")
        print(KarDiler, " = ", sum2)
    else:
        print("Карты Diler")
        print(KarDiler, " = ", sum2)
    print (name1, ", если берем карту, то жмем 1")
    print("Если нет, то жмем 0")
    choice1 = ""
    while choice1 != '1' and choice1 != '0':
        choice1 = input("Ваш выбор :")
    flag = 0
    while choice1 == '1' and flag == 0:
        karta = koloda.pop()
        KarPlayer.append(karta)
        sum1 = sum(sum1, test1(karta))
        print("Ваши карты", name1)
        print(KarPlayer, " = ", sum1)

        karta = koloda.pop()
        KarDiler.append(karta)
        sum2 = sum(sum2, test1(karta))
        print("Карты Diler")
        print(KarDiler, " = ", sum2)
        print(name1, ", если берем карту, то жмем 1")
        print("Если нет, то жмем 0")
        choice2 = ""
        while choice2 != '1' and choice2 != '0':
            choice2 = input("Ваш выбор :")
            if choice2 == '1':
                print("Играем дальше")
            elif choice2 == '0':
                flag = 1
                break
        if flag == 1:
            break



# elif choice == 0:
#     if sum1>sum2:
#     print (name1, "Вы выйграли!")
elif choice == '0':
    quit(1)