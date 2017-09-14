#game 'cube game'
from os import system
from time import sleep
from init_cube1 import *
from init_cube2 import *
#main

print('        Привет! Сейчас поиграем в игру "Кости"!')
print("1) Начать игру.")
print("2) Если ты не азартный человек, лучше и не начинай ;-)")

#Выбор режима игры

for i in range (1,20):
    init_cube1()
    init_cube2() 
    sleep(0.2)
    system('cls')
    

