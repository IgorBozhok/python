#computer set a random number
from random import *
from os import system
from time import sleep
def choice_play():
    for i in range(1,15):
        cube1 =randint(1,6)
        cube2 =randint(1,6)
        print(cube1," ",cube2)
        sleep(0.2)
        system ('cls')
    res1=cube1+cube2
    print(res1)

choice_play()
