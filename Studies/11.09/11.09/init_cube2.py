from random import *
from os import system
from time import sleep
def init_cube2():
   # for i in range(1,20):
    cube2=randint(1,6)
    if cube2 == 1: 
        print(" _______")
        print("|       |")
        print("|       |")
        print("|   *   |")
        print("|       |")
        print("|_______|")
    elif cube2 == 2: 
        print(" _______")
        print("|       |")
        print("| *     |")
        print("|       |")
        print("|     * |")
        print("|_______|")
    elif cube2 == 3:
        print(" _______")
        print("|       |")
        print("| *     |")
        print("|   *   |")
        print("|     * |")
        print("|_______|")
    elif cube2 == 4:
        print(" _______")
        print("|       |")
        print("| *   * |")
        print("|       |")
        print("| *   * |")
        print("|_______|")
    elif cube2 == 5:
        print(" _______")
        print("|       |")
        print("| *   * |")
        print("|   *   |")
        print("| *   * |")
        print("|_______|")
    elif cube2 == 6:
        print(" _______")
        print("|       |")
        print("| *   * |")
        print("| *   * |")
        print("| *   * |")
        print("|_______|")
    return cube2
    
