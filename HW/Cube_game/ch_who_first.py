from init_cube1 import *
from init_cube2 import *
from os import system
from time import sleep

def ch_who_first():
    system('cls')
    res1=0
    res2=0
    for i in range (1,10):
        init_cube1()
        init_cube2() 
        sleep(0.2)
        system('cls')
    res1=init_cube1()+init_cube2()
    print("")
    print("Ваш результат : ",res1)
    print("Теперь кидает кости Ваш соперник")
    x=input("Нажимаем что Вам угодно и начинаем ;-)")

    system('cls')
    for i in range (1,10):
        init_cube1()
        init_cube2() 
        sleep(0.2)
        system('cls')
    res2=init_cube1()+init_cube2()
    print("")
    print("Результат соперника : ",res2)
    print("У игрока 1 ",res1,", а у игрока 2",res2)
    x=input("Нажимаем что Вам угодно и начинаем ;-)")
        
    if res1>res2:
        x=input("Вы начинаете первый!! Нажимаем что Вам угодно ;-)")
        return 1
    
    elif res1<res2:
        x=input("Ваш соперник начинает первым!! Нажимаем что Вам угодно ;-)")
        return 2

    elif res1==res2:
        x=input("Начнем заново!! Нажимаем что Вам угодно ;-)")
        ch_who_first()

