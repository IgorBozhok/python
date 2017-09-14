from random import *
from os import system
from time import sleep
def init_cube1():
    #for i in range(1,20):
    cube1=randint(1,6)
    if cube1 == 1: 
        print(" _______")
        print("|       |")
        print("|       |")
        print("|   *   |")
        print("|       |")
        print("|_______|")
        sleep(0.25)
        system ('cls')
    elif cube1 == 2: 
        print(" _______")
        print("|       |")
        print("| *     |")
        print("|       |")
        print("|     * |")
        print("|_______|")
        sleep(0.25)
        system ('cls')
    elif cube1 == 3:
        print(" _______")
        print("|       |")
        print("| *     |")
        print("|   *   |")
        print("|     * |")
        print("|_______|")
        sleep(0.25)
        system ('cls')
    elif cube1 == 4:
        print(" _______")
        print("|       |")
        print("| *   * |")
        print("|       |")
        print("| *   * |")
        print("|_______|")
        sleep(0.25)
        system ('cls')
    elif cube1 == 5:
        print(" _______")
        print("|       |")
        print("| *   * |")
        print("|   *   |")
        print("| *   * |")
        print("|_______|")
        sleep(0.25)
        system ('cls')
    elif cube1 == 6:
        print(" _______")
        print("|       |")
        print("| *   * |")
        print("| *   * |")
        print("| *   * |")
        print("|_______|")
        sleep(0.25)
        system ('cls')
    return cube1

