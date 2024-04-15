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
FONT = ("Arial", 18, "bold")
BUTTONCOLOR = "#FFFF63"
BUTTONFONT = ("Arial", 20)

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

arrayA = []
arrayB = []
arrayX = []

root = Tk()
root.title("Головне вікно. Лабораторна №4")
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

root.mainloop()
