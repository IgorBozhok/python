
choice=0
ch_mode=0
while choice!=1 and choice!=2:
    while True:
        choice = input("Ваш выбор : ")
        try:
            choice = int(choice)
            break
        except ValueError:
            print("Ваш выбор : ")
if choice==1:
    print("Начнем!")
    print("И так ты азартный человек ;-)")
    print("1) Игра в 2-ем")
    print("2) Игра с комьютером")
    while ch_mode!=1 and ch_mode!=2:
        while True:
            ch_mode = input("Ваш выбор : ")
            try:
                ch_mode = int(ch_mode)
                break
            except ValueError:
                print("Ваш выбор : ")
    if ch_mode==1:
        print("Начнем!")
        print('Ваш выбор "Игра в 2-ем" !')
    elif ch_mode==2:
        print("Начнем!")
        print('Ваш выбор "Игра с комьютером" !')
    print(ch_mode) 
elif choice==2:
    print("Удачки ;-)")
    print(choice)
    
    
    


