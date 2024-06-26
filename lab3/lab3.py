from tkinter import *
from tkinter import messagebox
from random import uniform
import re, os, sys
from PIL import ImageTk
import matplotlib.pyplot as plt
from math import sin, exp

BG = "#787878"
FONT = ("Arial", 18, "bold")
BUTTONCOLOR = "#FFFF63"
BUTTONFONT = ("Arial", 20)

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

def buildTable(funcList):
    listOfK = []
    diff = []
    l = len(interpolationList)
    for i in range(l):
        diff.append(interpolationList[i] - funcList[i])
        listOfK.append(1 - diff[i] / interpolationDiff[i])

    table = Toplevel(root)
    table.configure(bg=BG)
    table.title("table")
    table.resizable(False, False)

    entries = []
    tableWidth = 4
    tableHeight = n + 1
    counter = 0
    for row in range(tableHeight):
        for column in range(tableWidth):
            entries.append(Entry(table, width=25, justify="center"))
            entries[counter].grid(row=row, column=column)
            entries[counter].config(font=("Helvetica", 12, "bold"))
            counter += 1

    entries[0].insert(0, 'n')
    j = 1
    for i in range(4, counter, 4):
        entries[i].config(font=("Helvetica", 12))
        entries[i].insert(0, j)
        j += 1

    entries[1].insert(0, 'Похибка')
    j = 0
    for i in range(5, counter, 4):
        entries[i].config(font=("Helvetica", 12))
        entries[i].insert(0, interpolationDiff[j])
        j += 1

    entries[2].insert(0, 'Різниця')
    j = 0
    for i in range(6, counter, 4):
        entries[i].config(font=("Helvetica", 12))
        entries[i].insert(0, diff[j])
        j += 1

    entries[3].insert(0, 'Коефіцієнт k')
    j = 0
    for i in range(7, counter, 4):
        entries[i].config(font=("Helvetica", 12))
        entries[i].insert(0, listOfK[j])
        j += 1


def aitkenInterpolation(x0_point, xArray, yArray):
    n_count = len(xArray)
    p = [0.0] * n_count

    for k in range(n_count):
        some = n_count - k
        for i in range(some):
            if k == 0:
                p[i] = yArray[i]
            else:
                p[i] = ((x0_point - xArray[i + k]) * p[i] + (xArray[i] - x0_point) * p[i + 1]) / (
                        xArray[i] - xArray[i + k])

    return p[0]


def enter():
    global a, b, n, x
    try:
        a = int(entryA.get())
        b = int(entryB.get())
        n = int(entryN.get())
        x = float(entryX.get().replace(',', '.'))
    except ValueError:
        messagebox.showerror(title="Помилка", message="Перевірте вхідні дані")
    if a > x or x > b:
        messagebox.showerror(title="Помилка", message="x має бути в межах від А до B")

def calculateSin():
    def callTable():
        buildTable(allSin)

    def divergenceX():
        divergenceXButton.destroy()
        interpolation = aitkenInterpolation(x, xKnown, yKnown)

        Label(sinWindow, text=f"Значення x: {x}", bg=BG, font=FONT, fg="white").grid(row=6, columnspan=2, pady=15)
        Label(sinWindow, text=f"Значення sin(x): {sin(x)}", bg=BG, font=FONT, fg="white").grid(row=7, columnspan=2,
                                                                                               pady=15)
        Label(sinWindow, text=f"Інтерполяція sin(x): {interpolation}", bg=BG, font=FONT, fg="white").grid(
            row=8, columnspan=2, pady=15)

        for i in range(len(xKnown)):
            if xKnown[i] > x:
                xKnown.insert(i - 1, (xKnown[i] + x) / 2)
                yKnown.insert(i - 1, sin((xKnown[i] + x) / 2))
                break

        nextInterpolation = aitkenInterpolation(x, xKnown, yKnown)
        Label(sinWindow, text=f"Похибка інтерполяції: {interpolation - nextInterpolation}", bg=BG, font=FONT,
              fg="white").grid(row=9, columnspan=2, pady=15)
        Label(sinWindow, text=f"Різниця між інтерполяцією і точним значенням: {interpolation - sin(x)}", bg=BG,
              font=FONT, fg="white").grid(row=10, columnspan=2, pady=15)

        k = 1 - (interpolation - sin(x)) / (interpolation - nextInterpolation)
        Label(sinWindow, text=f"розмитість оцінки: {k}", bg=BG, font=FONT, fg="white").grid(row=11, columnspan=2,
                                                                                            pady=15)

    def divergenceGraphic():
        global interpolationList, interpolationDiff
        interpolationList = [aitkenInterpolation(i, xKnown, yKnown) for i in xUnknown]

        while True:
            additionalNode = uniform(a, b)
            if additionalNode not in xKnown:
                for i in range(len(xKnown)):
                    if xKnown[i] > additionalNode:
                        xKnown.insert(i - 1, additionalNode)
                        yKnown.insert(i - 1, sin(additionalNode))
                        break
                break

        nextInterpolationList = [aitkenInterpolation(i, xKnown, yKnown) for i in xUnknown]

        interpolationDiff = []
        for i in range(len(interpolationList)):
            if interpolationList[i] - nextInterpolationList[i] != 0:
                interpolationDiff.append(interpolationList[i] - nextInterpolationList[i])
            else:
                interpolationDiff.append(0.0000001)

        plt.figure()

        plt.plot(xUnknown, interpolationDiff)
        plt.title('Похибка')
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.show()

    def defaultGraphic():
        global allSin, yUnknown, xUnknown, xKnown, yKnown
        h = (b - a) / 10
        hSin = (b - a) / 100
        xKnown = []
        xSin = []
        for i in range(11):
            xKnown.append(a + h * i)
        for i in range(101):
            xSin.append(a + hSin * i)
        yKnown = [sin(i) for i in xKnown]
        ySin = [sin(i) for i in xSin]

        h = (b - a) / (n - 1)
        xUnknown = []
        xUnknownGraph = []
        for i in range(n):
            xUnknown.append(a + h * i)

        for i in range(n * 10):
            xUnknownGraph.append((a + h * i) / 10)

        yUnknown = [aitkenInterpolation(i, xKnown, yKnown) for i in xUnknown]
        yUnknownGraph = [aitkenInterpolation(i, xKnown, yKnown) for i in xUnknownGraph]
        allSin = [sin(i) for i in xUnknown]

        plt.plot(xSin, ySin)
        plt.title('Графік sin(x)')
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.figure()

        plt.plot(xUnknownGraph, yUnknownGraph)
        plt.title('Інтерполяція sin(x)')
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.show()

    sinWindow = Toplevel(root)
    sinWindow.title("sin(x)")
    sinWindow.geometry("900x1000")
    sinWindow.resizable(False, False)
    sinWindow.configure(bg=BG)

    Grid.columnconfigure(sinWindow, 0, weight=1)
    Grid.columnconfigure(sinWindow, 1, weight=1)

    Label(sinWindow, text="Введіть межу А: ", font=FONT, bg=BG, fg="white").grid(row=0, column=0, pady=10, sticky="e")
    Label(sinWindow, text="Введіть межу B: ", font=FONT, bg=BG, fg="white").grid(row=1, column=0, pady=10, sticky="e")
    Label(sinWindow, text="Введіть кількість точок n: ", font=FONT, bg=BG, fg="white").grid(row=2, column=0, pady=10,
                                                                                            sticky="e")
    Label(sinWindow, text="Введіть точку x: ", font=FONT, bg=BG, fg="white").grid(row=3, column=0, pady=10, sticky="e")

    global entryA, entryB, entryN, entryX
    entryA = Entry(sinWindow, width=20)
    entryA.grid(row=0, column=1, padx=10, sticky="w")
    entryB = Entry(sinWindow, width=20)
    entryB.grid(row=1, column=1, padx=10, sticky="w")
    entryN = Entry(sinWindow, width=20)
    entryN.grid(row=2, column=1, padx=10, sticky="w")
    entryX = Entry(sinWindow, width=20)
    entryX.grid(row=3, column=1, padx=10, sticky="w")

    enterButton = Button(sinWindow, text="Ввести", bg=BUTTONCOLOR, font=BUTTONFONT, command=enter)
    enterButton.grid(row=4, columnspan=2, padx=10)

    defaultGraphicButton = Button(sinWindow, text="Графік", bg=BUTTONCOLOR, font=BUTTONFONT, command=defaultGraphic,
                                  height=7, width=20)
    defaultGraphicButton.grid(row=5, column=0, pady=20)

    divergenceGraphicButton = Button(sinWindow, text="Графік Похибки", bg=BUTTONCOLOR, font=BUTTONFONT,
                                     command=divergenceGraphic, height=7, width=20)
    divergenceGraphicButton.grid(row=5, column=1, pady=20)

    divergenceXButton = Button(sinWindow, text="Похибка значення х", bg=BUTTONCOLOR, font=BUTTONFONT,
                               command=divergenceX)
    divergenceXButton.grid(row=6, columnspan=2)

    tableButton = Button(sinWindow, text="Таблиця похибок", bg=BUTTONCOLOR, font=BUTTONFONT, command=callTable)
    tableButton.grid(row=12, columnspan=2)

def calculateFunction():
    def myFunc(num):
        return 1 / (1 + exp(-1 * num))

    def callTable():
        buildTable(allFunc)

    def divergenceX():

        divergenceXButton.destroy()
        interpolation = aitkenInterpolation(x, xKnown, yKnown)

        Label(funcWindow, text=f"Значення x: {x}", bg=BG, font=FONT, fg="white").grid(row=6, columnspan=2, pady=15)
        Label(funcWindow, text=f"Значення f(x): {myFunc(x)}", bg=BG, font=FONT, fg="white").grid(row=7, columnspan=2,
                                                                                              pady=15)
        Label(funcWindow, text=f"Інтерполяція f(x): {interpolation}", bg=BG, font=FONT, fg="white").grid(
            row=8, columnspan=2, pady=15)

        for i in range(len(xKnown)):
            if x > xKnown[i]:
                xKnown.insert(i + 1, (xKnown[i] + x) / 2)
                yKnown.insert(i + 1, myFunc(x))
                break

        nextInterpolation = aitkenInterpolation(x, xKnown, yKnown)
        Label(funcWindow, text=f"Похибка інтерполяції: {interpolation - nextInterpolation}", bg=BG, font=FONT,
              fg="white").grid(row=9, columnspan=2, pady=15)
        Label(funcWindow, text=f"Різниця між інтерполяцією і точним значенням: {interpolation - myFunc(x)}", bg=BG,
              font=FONT, fg="white").grid(row=10, columnspan=2, pady=15)

        k = 1 - (interpolation - myFunc(x)) / (interpolation - nextInterpolation)
        Label(funcWindow, text=f"розмитість оцінки: {k}", bg=BG, font=FONT, fg="white").grid(row=11, columnspan=2,
                                                                                             pady=15)

    def divergenceGraphic():
        global interpolationList, interpolationDiff
        interpolationList = [aitkenInterpolation(i, xKnown, yKnown) for i in xUnknown]

        while True:
            additionalNode = uniform(a, b)
            if additionalNode not in xKnown:
                for i in range(len(xKnown)):
                    if xKnown[i] > additionalNode:
                        xKnown.insert(i - 1, additionalNode)
                        yKnown.insert(i - 1, myFunc(x))
                        break
                break

        nextInterpolationList = [aitkenInterpolation(i, xKnown, yKnown) for i in xUnknown]

        interpolationDiff = []
        for i in range(len(interpolationList)):
            if interpolationList[i] - nextInterpolationList[i] != 0:
                interpolationDiff.append(interpolationList[i] - nextInterpolationList[i])
            else:
                interpolationDiff.append(0.000000001)


        plt.figure()

        plt.plot(xUnknown, interpolationDiff)
        plt.title('Похибка')
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.show()

    def defaultGraphic():
        global allFunc, yUnknown, xUnknown, xKnown, yKnown
        h = (b - a) / 10
        hFunc = (b - a) / 100
        xKnown = []
        xFunc = []
        for i in range(11):
            xKnown.append(a + h * i)
        for i in range(101):
            xFunc.append(a + hFunc * i)
        yKnown = [myFunc(i) for i in xKnown]
        yFunc = [myFunc(i) for i in xFunc]

        h = (b - a) / (n - 1)
        xUnknown = []
        xUnknownGraph = []
        for i in range(n):
            xUnknown.append(a + h * i)

        for i in range(n * 10):
            xUnknownGraph.append(round((a + h * i) / 10, 2))

        yUnknown = [aitkenInterpolation(i, xKnown, yKnown) for i in xUnknown]
        yUnknownGraph = [aitkenInterpolation(i, xKnown, yKnown) for i in xUnknownGraph]
        allFunc = [myFunc(i) for i in xUnknown]

        plt.plot(xFunc, yFunc)
        plt.title('Графік f(x)')
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.figure()

        plt.plot(xUnknownGraph, yUnknownGraph)
        plt.title('Інтерполяція f(x)')
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.show()

    funcWindow = Toplevel(root)
    funcWindow.title("Задана функція")
    funcWindow.geometry("900x1000")
    funcWindow.resizable(False, False)
    funcWindow.configure(bg=BG)

    Grid.columnconfigure(funcWindow, 0, weight=1)
    Grid.columnconfigure(funcWindow, 1, weight=1)

    Label(funcWindow, text="Введіть межу А: ", font=FONT, bg=BG, fg="white").grid(row=0, column=0, pady=10,
                                                                                  sticky="e")
    Label(funcWindow, text="Введіть межу B: ", font=FONT, bg=BG, fg="white").grid(row=1, column=0, pady=10,
                                                                                  sticky="e")
    Label(funcWindow, text="Введіть кількість точок n: ", font=FONT, bg=BG, fg="white").grid(row=2, column=0,
                                                                                             pady=10,
                                                                                             sticky="e")
    Label(funcWindow, text="Введіть точку x: ", font=FONT, bg=BG, fg="white").grid(row=3, column=0, pady=10,
                                                                                   sticky="e")

    global entryA, entryB, entryN, entryX
    entryA = Entry(funcWindow, width=20)
    entryA.grid(row=0, column=1, padx=10, sticky="w")
    entryB = Entry(funcWindow, width=20)
    entryB.grid(row=1, column=1, padx=10, sticky="w")
    entryN = Entry(funcWindow, width=20)
    entryN.grid(row=2, column=1, padx=10, sticky="w")
    entryX = Entry(funcWindow, width=20)
    entryX.grid(row=3, column=1, padx=10, sticky="w")

    enterButton = Button(funcWindow, text="Ввести", bg=BUTTONCOLOR, font=BUTTONFONT, command=enter)
    enterButton.grid(row=4, columnspan=2, padx=10)

    defaultGraphic = Button(funcWindow, text="Графік", bg=BUTTONCOLOR, font=BUTTONFONT, command=defaultGraphic,
                            height=7, width=20)
    defaultGraphic.grid(row=5, column=0, pady=20)

    divergenceGraphic = Button(funcWindow, text="Графік Похибки", bg=BUTTONCOLOR, font=BUTTONFONT,
                               command=divergenceGraphic, height=7, width=20)
    divergenceGraphic.grid(row=5, column=1, pady=20)

    divergenceXButton = Button(funcWindow, text="Похибка х", bg=BUTTONCOLOR, font=BUTTONFONT, command=divergenceX)
    divergenceXButton.grid(row=6, columnspan=2)

    tableButton = Button(funcWindow, text="Таблиця похибок", bg=BUTTONCOLOR, font=BUTTONFONT, command=callTable)
    tableButton.grid(row=12, columnspan=2)

a, b, n, x = 0, 4, 11, 0

root = Tk()
root.title("Головне вікно. Лабораторна №3")
root.geometry("900x600")
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
Label(root, image=img).grid(row=5, columnspan=2, pady=5)
Label(root, text="___" * 1000, bg=BG, fg="white", font=FONT).grid(row=6, columnspan=2, pady=10)

inputButton = Button(root, text="Задана функція", bg=BUTTONCOLOR, font=BUTTONFONT, command=calculateFunction,
                     height=7, width=20)
inputButton.grid(row=7, column=0)

drawButton = Button(root, text="sin(x)", bg=BUTTONCOLOR, font=BUTTONFONT, command=calculateSin, height=7, width=20)
drawButton.grid(row=7, column=1)

root.mainloop()
