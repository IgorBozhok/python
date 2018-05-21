from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")


# ф-ия блокировки определенных символов
def _try(x):
    try:
        if data_out.get()[len(data_out.get()) - 1] == ".":
            data_out.delete(len(data_out.get()), END)
        elif data_out.get()[len(data_out.get()) - 1] == "/":
            data_out.delete(len(data_out.get()), END)
        elif data_out.get()[len(data_out.get()) - 1] == "*":
            data_out.delete(len(data_out.get()), END)
        elif data_out.get()[len(data_out.get()) - 1] == "-":
            data_out.delete(len(data_out.get()), END)
        elif data_out.get()[len(data_out.get()) - 1] == "+":
            data_out.delete(len(data_out.get()), END)
        else:
            data_out.insert(END, x)
    except IndexError:
        pass

# логика
def _calc(bttn):
    global memory

# Ввывод ошбки
    if bttn == "=":
        str1 = "./*-+1234567890"
        if data_out.get()[0] not in str1:
            data_out.insert(END, "Символ не число!")
        try:
            result = eval(data_out.get())
            data_out.insert(END, "=" + str(result))
        except:
            data_out.delete(0, END)
            data_out.insert(END, "Ошибка!")

# Очистка поля
    elif bttn == "C":
        data_out.delete(0, END)
# Плюс/минус
    elif bttn == "-/+":
        if "=" in data_out.get():
            data_out.delete(0,END)
        try:
            if data_out.get()[0] == "-":
                data_out.delete(0)
            else:
                data_out.insert(0, "-")
        except IndexError:
            pass
# Удаление 1 символа
    elif bttn == "CE":
        data_out.delete(len(data_out.get())-1)

# Блокировка символов
    elif bttn == ".":
        _try(bttn)

    elif bttn == "/":
        _try(bttn)

    elif bttn == "*":
        _try(bttn)

    elif bttn == "-":
        _try(bttn)

    elif bttn == "+":
        _try(bttn)

    else:
        if "=" in data_out.get():
            data_out.delete(0, END)
        data_out.insert(END, bttn)

# Список кнопок
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    " ", "0", "-/+", "+",
    ".", "=", "C", "CE"
]

# Экран ввода
data_out = Entry(root, width=50)
data_out.grid(columnspan=4)

# Создание кнопок через цикл for
a = 1
b = 0
for i in buttons:
    cmd = lambda x=i: _calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=a, column=b)
    b += 1
    if b > 3:
        b = 0
        a += 1

root.mainloop()