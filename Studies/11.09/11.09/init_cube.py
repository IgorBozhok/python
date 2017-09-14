from random import *
from os import system
from time import sleep
def init_cube():
    for i in range(1,100):
        cube1=randint(1,6)
        if cube1 == 1: 
            print(" _______")
            print("|       |")
            print("|       |")
            print("|   *   |")
            print("|       |")
            print("|_______|")
            sleep(0.3)
            system ('cls')
        elif cube1 == 2: 
            print(" _______")
            print("|       |")
            print("| *     |")
            print("|       |")
            print("|     * |")
            print("|_______|")
            sleep(0.3)
            system ('cls')
        elif cube1 == 3:
            print(" _______")
            print("|       |")
            print("| *     |")
            print("|   *   |")
            print("|     * |")
            print("|_______|")
            sleep(0.3)
            system ('cls')
        elif cube1 == 4:
            print(" _______")
            print("|       |")
            print("| *   * |")
            print("|       |")
            print("| *   * |")
            print("|_______|")
            sleep(0.3)
            system ('cls')
        elif cube1 == 5:
            print(" _______")
            print("|       |")
            print("| *   * |")
            print("|   *   |")
            print("| *   * |")
            print("|_______|")
            sleep(0.3)
            system ('cls')
        elif cube1 == 6:
            print(" _______")
            print("|       |")
            print("| *   * |")
            print("| *   * |")
            print("| *   * |")
            print("|_______|")
            sleep(0.3)
            system ('cls')
    return cube1
init_cube ()
