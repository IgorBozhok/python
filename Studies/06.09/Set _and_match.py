#game 'Set and match'
from random import *
print ('Привет, это игра "Угадай число!"')
print ("Я загадал число от 1 до 100 ")
print ("Попробуй угадать это число")

#main

#computer set a random number
q = ''
while q != 'no':
    num =randint(1,101)
    print(num)
    #modul for player
    i=1
    while True:
        while 1:
            print("Попытка №",i)
            s = input("Введите ваше число: ")
            try:
                s = int(s)
                break
            except ValueError:
                print('Вводите число:')
        if s > 1 or s > 100:
            print("okay let's go")
        else:
            print("Error")
            continue
        if str() == str(int()):
            print("Error")
            continue
        if num > s:
            print("Неа, мое число больше!")
            i+=1
        elif num < s:
            print("Неа, мое число меньше!")
            i+=1
        else:
            print('Да' , num,'это мое число')
            break
    print("Вы угадали число с",i,"раза!")
    q = input("Сыграем еще?(yes/no)")

input("Ага")
