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

def calculateSin():
    pass

def calculateFunction():
    pass

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
