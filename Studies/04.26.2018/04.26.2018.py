import random
import os

class Food():
    def __init__(self, meat=10, water=5, fish=8):
        self.meat = meat
        self.water = water
        self.fish = fish


class Critter():
    def __init__(self, name, hunger=100, boredom=100, sleep=100):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.sleep = sleep

    def __str__(self):
        print(self.hunger, '%')
        print(self.boredom, '%')
        print(self.sleep, '%')



    def __pass_hunger(self):
        self.hunger -= random.randint(1, 11)

    def __pass_boredom(self):
        self.boredom -= random.randint(1, 11)

    def __pass_sleep(self):
        self.sleep -= random.randint(1, 11)



    def mood(self):
        happy = self.hunger + self.boredom
        res = ''
        if happy > 200:
            res = 'i am crazy happiness'
        elif 150 < happy <= 200:
            res = 'i am so happy'
        elif 100 < happy <= 150:
            res = 'i am ok'
        elif 50 < happy <= 100:
            res = 'i am bad'
        elif 0 < happy <= 50:
            res = 'i am mad'
        elif happy < 0:
            res = 'I AM DEAD!!!'
        return res

    def talk(self):
        print('I am', self.name, 'and', self.mood())
        self.__pass_boredom()
        self.__pass_hunger()
        self. __pass_sleep()


    def eat(self, food):
        print('Om-nom-nom...')
        self.hunger += food
        self.__pass_boredom()
        self.__pass_sleep()


    def play(self, fun=random.randint(10, 21)):
        print('Wheeeeeee!')
        self.boredom += fun
        self.__pass_hunger()
        self.__pass_sleep()


    def m_sleep(self, sleep=random.randint(10, 21)):
        print('Zzzzzz')
        self.sleep += sleep
        self.__pass_hunger()
        self.__pass_boredom()



    def crit_helth(self):
        if self.hunger < 0 or self.boredom < 0:
            exit()

def main():
    name = input('What name of your critter? \n')
    crit = Critter(name)
    food = Food()
    while True:
        print("""\r
0 - exit game;
1 - talk with {};
2 - eat to {};
3 - play to {};
4 - sleep to {};
        """.format(name, name, name, name))
        choice = input('Choice game mode: \n')
        if choice == '0':
            break
        elif choice == '1':
            os.system('cls')
            crit.talk()
            crit.crit_helth()
        elif choice == '2':
            os.system('cls')
            print("""
1 - give meat to {};
2 - give water to {}
3 - give fish to {}
                   """.format(name, name, name))
            choiceFood = input('Choice food mode: \n')
            if choiceFood == '1':
                os.system('cls')
                crit.eat(food.meat)
                crit.crit_helth()
            elif choiceFood == '2':
                os.system('cls')
                crit.eat(food.water)
                crit.crit_helth()
            elif choiceFood == '3':
                os.system('cls')
                crit.eat(food.fish)
                crit.crit_helth()
        elif choice == '3':
            os.system('cls')
            crit.play()
            crit.crit_helth()
        elif choice == '4':
            os.system('cls')
            crit.m_sleep()
            crit.crit_helth()
        elif choice == '5':
            os.system('cls')
            crit.__str__()
        else:
            print('Wrong choice')


if __name__ == '__main__':
    print('Welcome to game "Critter"')
    main()
