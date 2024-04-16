from tkinter import *
from tkinter import messagebox
import re, os, sys
from PIL import ImageTk
import matplotlib.pyplot as plt


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


BG = "#787878"
FONT = ("Helvetica", 18, "bold")
BUTTONCOLOR = "#FFFF63"
BUTTONFONT = ("Helvetica", 20)


def method(A, B, epsilon):
    arrayA.append(min(A, B))
    arrayB.append(max(A, B))

    if abs(B - A) < epsilon:
        return (A + B) / 2

    if f(B) * secondDerivativeF(B) < 0:
        A, B = B, A

    x = B - f(B) / derivativeF(B)
    arrayX.append(x)

    if abs(x - B) < epsilon:
        return x

    return method(A, x, epsilon)

def secondDerivativeF(x):
    return 6 * x

def derivativeF(x):
    return 3 * (x ** 2) + 10

def f(x):
    return x ** 3 + 10 * x - 9

def buildGraph():
    coordX = []
    coordY = []
    i = a
    while i <= b:
        coordX.append(i)
        coordY.append(f(i))
        i += 0.0001

    plt.figure()

    plt.plot(coordX, coordY)
    plt.axhline(0, color='black')
    plt.title('Графік функції')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.show()



def buildTable():
    answer = method(a, b, e)

    table = Toplevel(root)
    table.configure(bg=BG)
    table.title("table")
    table.resizable(False, False)

    entries = []
    tableWidth = 3
    tableHeight = len(arrayA) + 1
    counter = 0
    for row in range(tableHeight):
        for column in range(tableWidth):
            entries.append(Entry(table, width=25, justify="center"))
            entries[counter].grid(row=row, column=column)
            entries[counter].config(font=("Helvetica", 12, "bold"))
            counter += 1

    entries[0].insert(0, 'А')
    j = 0
    for i in range(3, counter, 3):
        entries[i].config(font=("Helvetica", 12))
        entries[i].insert(0, arrayA[j])
        j += 1

    entries[1].insert(0, 'X')
    j = 0
    for i in range(4, counter, 3):
        entries[i].config(font=("Helvetica", 12))
        entries[i].insert(0, arrayX[j])
        j += 1

    entries[2].insert(0, 'B')
    j = 0
    for i in range(5, counter, 3):
        entries[i].config(font=("Helvetica", 12))
        entries[i].insert(0, arrayB[j])
        j += 1

    Label(table, text=f"Корінь - {round(answer, 5)}", font=FONT, bg=BG, fg="white").grid(row=tableHeight, column=1,
                                                                                         pady=20)

def enter():
    global a, b, e
    try:
        a = float(aEntry.get().replace(',', '.'))
        b = float(bEntry.get().replace(',', '.'))
        e = float(eEntry.get().replace(',', '.'))
    except ValueError:
        messagebox.showerror("Помилка", "Введіть правильні значення")
        return

    if b <= a:
        messagebox.showerror("Помилка", "b < a")
        return

    if f(a) * f(b) > 0:
        messagebox.showerror("Помилка", "Неправильні межі")
        return

    tableButton["state"] = "normal"
    graphButton["state"] = "normal"

arrayA = []
arrayB = []
arrayX = []

root = Tk()
root.title("Головне вікно. Лабораторна №4")
root.geometry("900x1200")
root.resizable(False, False)
root.configure(bg=BG)

Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)

Label(root, text=" ", bg=BG, font=FONT).grid(row=0, columnspan=2, pady=5)
Label(root, text="Інформація про студента", bg=BG, fg="white", font=FONT).grid(row=1, columnspan=2)
Label(root, text="ПІБ: Закревський Данило Сергійович", bg=BG, fg="white", font=FONT).grid(row=2, columnspan=2)
Label(root, text="Група: ІО-24", bg=BG, fg="white", font=FONT).grid(row=3, columnspan=2)
Label(root, text="Варіант: 11", bg=BG, fg="white", font=FONT).grid(row=4, columnspan=2)

global img
path = resource_path('task.png')
img = ImageTk.PhotoImage(file=path)
Label(root, image=img).grid(row=5, columnspan=2)
Label(root, text="___" * 1000, bg=BG, fg="white", font=FONT).grid(row=6, columnspan=2, pady=10)

aEntry = Entry(root, width=20)
aEntry.grid(row=7, column=1, padx=10, pady=5, sticky="w")
Label(root, text="Введіть A:", bg=BG, font=FONT, fg="white").grid(row=7, column=0, padx=(0, 10), pady=5, sticky="e")
bEntry = Entry(root, width=20)
bEntry.grid(row=8, column=1, padx=10, pady=5, sticky="w")
Label(root, text="Введіть B:", bg=BG, font=FONT, fg="white").grid(row=8, column=0, padx=(0, 10), pady=5, sticky="e")
eEntry = Entry(root, width=20)
eEntry.grid(row=9, column=1, padx=10, pady=5, sticky="w")
Label(root, text="Введіть ε:", bg=BG, font=FONT, fg="white").grid(row=9, column=0, padx=(0, 10), pady=5, sticky="e")

enterButton = Button(root, text="Ввести", bg=BUTTONCOLOR, font=BUTTONFONT, command=enter)
enterButton.grid(row=10, columnspan=2, padx=10)

tableButton = Button(root, text="Знайти корінь", bg=BUTTONCOLOR, font=BUTTONFONT, command=buildTable, height=7,
                     width=20, state="disabled")
tableButton.grid(row=11, columnspan=2, pady=10)

graphButton = Button(root, text="Побудувати графік", bg=BUTTONCOLOR, font=BUTTONFONT, command=buildGraph, height=7,
                     width=20, state="disabled")
graphButton.grid(row=12, columnspan=2, pady=10)

root.mainloop()
