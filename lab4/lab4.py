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

a, b, e = 0, 0, 0

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
Label(root, text="Введіть A:", bg=BG, font=FONT).grid(row=7, column=0, padx=(0, 10), pady=5, sticky="e")
bEntry = Entry(root, width=20)
bEntry.grid(row=8, column=1, padx=10, pady=5, sticky="w")
Label(root, text="Введіть B:", bg=BG, font=FONT).grid(row=8, column=0, padx=(0, 10), pady=5, sticky="e")
eEntry = Entry(root, width=20)
eEntry.grid(row=9, column=1, padx=10, pady=5, sticky="w")
Label(root, text="Введіть ε:", bg=BG, font=FONT).grid(row=9, column=0, padx=(0, 10), pady=5, sticky="e")

root.mainloop()
