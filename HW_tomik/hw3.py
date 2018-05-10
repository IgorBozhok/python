import random
import os

class Food():
    def __init__(self, meat=15, water=10, fish=5):
        self.meat = meat
        self.water = water
        self.fish = fish

class Play():
    def __init__(self, ball=15, bone=10, walk=5):
        self.ball = ball
        self.bone = bone
        self.walk = walk

class Critter():
    def __init__(self, name, hunger=100, boredom=100, sleep=100):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.sleep = sleep

    def __str__(self):
        print('hunger ', self.hunger, '%')
        print('boredom ', self.boredom, '%')
        print('sleep ', self.sleep, '%')



    def __pass_hunger(self):
        self.hunger -= random.randint(1, 11)

    def __pass_boredom(self):
        self.boredom -= random.randint(1, 11)

    def __pass_sleep(self):
        self.sleep -= random.randint(1, 11)



    def mood(self):
        happy = self.hunger + self.boredom + self.sleep
        res = ''
        if happy >= 270:
            res = 'i am crazy happiness '
        elif 200 < happy <= 269:
            res = 'i am so happy'
        elif 150 < happy <= 200:
            res = 'i am ok'
        elif 100 < happy <= 150:
            res = 'i am bad'
        elif 0 < happy <= 100:
            res = 'i am mad'
        elif happy < 0:
            res = 'I AM DEAD!!!'
        return res

    def smile(self):
        happy = self.hunger + self.boredom + self.sleep
        res = ''
        if happy >= 270:
            res = ' /人◕ ‿‿ ◕人\ '
        elif 200 < happy <= 269:
            res = ' ≧◔◡◔≦ '
        elif 150 < happy <= 200:
            res = '٩(◕‿◕｡)۶'
        elif 100 < happy <= 150:
            res = '◕ ᴥ ◕'
        elif 0 < happy <= 100:
            res = '（︶︿︶）'
        elif happy < 0:
            res = '(╥﹏╥)'
        return res

    def talk(self):
        print('I am', self.name, 'and', self.mood(), self.smile())
        self.__pass_boredom()
        self.__pass_hunger()
        self. __pass_sleep()


    def eat(self, food):
        print('Om-nom-nom... ', self.smile())
        self.hunger += food
        if self.hunger > 100:
            self.hunger = 100
        self.__pass_boredom()
        self.__pass_sleep()


    def play(self, _play):
        print('Wheeeeeee!', self.smile())
        self.boredom += _play
        if self.boredom > 100:
            self.boredom = 100
        self.__pass_hunger()
        self.__pass_sleep()


    def m_sleep(self, sleep=random.randint(10, 21)):
        print('Zzzzzz', self.smile())
        self.sleep += sleep
        if self.sleep > 100:
            self.sleep = 100
        self.__pass_hunger()
        self.__pass_boredom()



    def crit_helth(self):
        if self.hunger < 0 or self.boredom < 0:
            exit()

def main():
    name = input('What name of your critter? \n')
    crit = Critter(name)
    food = Food()
    _play = Play()
    while True:
        print("""\r
0 - Exit game;
1 - Talk with {};
2 - Eat to {};
3 - Play to {};
4 - Sleep to {};
        """.format(name, name, name, name))
        choice = ""
        while choice != '0' and choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
            choice = input("Choice game mode: \n")
        if choice == '0':
            break
        elif choice == '1':
            os.system('cls')
            crit.talk()
            crit.crit_helth()
        elif choice == '2':
            os.system('cls')
            print("""
1 - Give meat to {};
2 - Give water to {};
3 - Give fish to {};
                   """.format(name, name, name))
            choiceFood = ""
            while choiceFood != '1' and choiceFood != '2' and choiceFood != '3':
                choiceFood = input("Choice game mode: \n")

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
            print("""
1 - Play with the ball {};
2 - Play with the bone {};
3 - Go for a walk {};
                               """.format(name, name, name))
            choicePlay = ""
            while choicePlay != '1' and choicePlay != '2' and choicePlay != '3':
                choicePlay = input("Choice game mode: \n")

            if choicePlay == '1':
                os.system('cls')
                crit.play(_play.ball)
                crit.crit_helth()
            elif choicePlay == '2':
                os.system('cls')
                crit.play(_play.bone)
                crit.crit_helth()
            elif choicePlay == '3':
                os.system('cls')
                crit.play(_play.walk)
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