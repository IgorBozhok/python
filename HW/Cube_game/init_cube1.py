from random import *


def init_cube1():
    cube1=randint(1,6)
    if cube1 == 1: 
        print(" _______")
        print("|       |")
        print("|       |")
        print("|   *   |")
        print("|       |")
        print("|_______|")
    elif cube1 == 2: 
        print(" _______")
        print("|       |")
        print("| *     |")
        print("|       |")
        print("|     * |")
        print("|_______|")
    elif cube1 == 3:
        print(" _______")
        print("|       |")
        print("| *     |")
        print("|   *   |")
        print("|     * |")
        print("|_______|")
    elif cube1 == 4:
        print(" _______")
        print("|       |")
        print("| *   * |")
        print("|       |")
        print("| *   * |")
        print("|_______|")
    elif cube1 == 5:
        print(" _______")
        print("|       |")
        print("| *   * |")
        print("|   *   |")
        print("| *   * |")
        print("|_______|")
    elif cube1 == 6:
        print(" _______")
        print("|       |")
        print("| *   * |")
        print("| *   * |")
        print("| *   * |")
        print("|_______|")
    return cube1

