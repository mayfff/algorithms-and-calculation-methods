from tkinter import *
from tkinter import messagebox
import re, os, sys
from PIL import ImageTk
import matplotlib.pyplot as plt


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def result():
    pass

def getMatrix():
    resultButton["state"] = NORMAL


BG = "#787878"
FONT = ("Helvetica", 18, "bold")
BUTTONCOLOR = "#FFFF63"
BUTTONFONT = ("Helvetica", 20)

root = Tk()
root.title("Головне вікно. Лабораторна №5")
root.geometry("900x900")
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

matrixButton = Button(root, text="Введення матриці", bg=BUTTONCOLOR, font=BUTTONFONT, command=getMatrix, height=7,
                      width=20)
matrixButton.grid(row=7, column=0)

resultButton = Button(root, text="Кінцева матриця \nта результат", bg=BUTTONCOLOR, font=BUTTONFONT, command=result,
                      height=7, width=20, state="disabled")
resultButton.grid(row=7, column=1)

root.mainloop()
