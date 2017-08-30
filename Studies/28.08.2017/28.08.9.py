x1=int(input("Введите число от 1 до 8"))
y1=int(input("Введите число от 1 до 8"))
x2=int(input("Введите число от 1 до 8"))
y2=int(input("Введите число от 1 до 8"))
if abs (x1-x2)==1 and abs (y1-y2)==2 or abs (x1-x2)==2 or abs (y1-y2)==1:
    print("yes")
else:
    print ("no")
