from tkinter import *
from tkinter import messagebox, filedialog
from random import randint
import re, os, sys
from PIL import ImageTk
import matplotlib.pyplot as plt
import numpy as np

BG = "#787878"
FONT = ("Arial", 18, "bold")
BUTTONCOLOR = "#FFFF63"
BUTTONFONT = ("Arial", 20)


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def enter():
    global a, b, n, x
    a = int(entryA.get())
    b = int(entryB.get())
    n = int(entryN.get())
    x = int(entryX.get())


def calculateSin():
    sinWindow = Toplevel(root)
    sinWindow.title("sin(x)")
    sinWindow.geometry("900x900")
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

    defaultGraphic = Button(sinWindow, text="Графік", bg=BUTTONCOLOR, font=BUTTONFONT, command=enter,
                            height=7, width=20)
    defaultGraphic.grid(row=5, column=0, pady=20)

    interpolationGraphic = Button(sinWindow, text="Графік Інтерполяції", bg=BUTTONCOLOR, font=BUTTONFONT,
                                  command=enter, height=7, width=20)
    interpolationGraphic.grid(row=6, column=0)

    divergenceGraphic = Button(sinWindow, text="Графік Похибки", bg=BUTTONCOLOR, font=BUTTONFONT, command=enter, height=7,
                               width=20)
    divergenceGraphic.grid(row=5, column=1, pady=20)

    divergenceTable = Button(sinWindow, text="Таблиця похибок", bg=BUTTONCOLOR, font=BUTTONFONT, command=enter, height=7,
                             width=20)
    divergenceTable.grid(row=6, column=1)

def calculateFunction():
    funcWindow = Toplevel(root)
    funcWindow.title("Задана функція")
    funcWindow.geometry("900x900")
    funcWindow.resizable(False, False)
    funcWindow.configure(bg=BG)

    Grid.columnconfigure(funcWindow, 0, weight=1)
    Grid.columnconfigure(funcWindow, 1, weight=1)

    Label(funcWindow, text="Введіть межу А: ", font=FONT, bg=BG, fg="white").grid(row=0, column=0, pady=10, sticky="e")
    Label(funcWindow, text="Введіть межу B: ", font=FONT, bg=BG, fg="white").grid(row=1, column=0, pady=10, sticky="e")
    Label(funcWindow, text="Введіть кількість точок n: ", font=FONT, bg=BG, fg="white").grid(row=2, column=0, pady=10,
                                                                                        sticky="e")
    Label(funcWindow, text="Введіть точку x: ", font=FONT, bg=BG, fg="white").grid(row=3, column=0, pady=10, sticky="e")

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

    defaultGraphic = Button(funcWindow, text="Графік", bg=BUTTONCOLOR, font=BUTTONFONT, command=enter,
                            height=7, width=20)
    defaultGraphic.grid(row=5, column=0, pady=20)

    interpolationGraphic = Button(funcWindow, text="Графік Інтерполяції", bg=BUTTONCOLOR, font=BUTTONFONT,
                                  command=enter, height=7, width=20)
    interpolationGraphic.grid(row=6, column=0)

    divergenceGraphic = Button(funcWindow, text="Графік Похибки", bg=BUTTONCOLOR, font=BUTTONFONT, command=enter,
                               height=7,
                               width=20)
    divergenceGraphic.grid(row=5, column=1, pady=20)

    divergenceTable = Button(funcWindow, text="Таблиця похибок", bg=BUTTONCOLOR, font=BUTTONFONT, command=enter,
                             height=7,
                             width=20)
    divergenceTable.grid(row=6, column=1)


a, b = 0, 4
n = 11

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

inputButton = Button(root, text="Задана функція", bg=BUTTONCOLOR, font=BUTTONFONT, command=calculateFunction, height=7,
                     width=20)
inputButton.grid(row=7, column=0)

drawButton = Button(root, text="sin(x)", bg=BUTTONCOLOR, font=BUTTONFONT, command=calculateSin, height=7, width=20)
drawButton.grid(row=7, column=1)

root.mainloop()
