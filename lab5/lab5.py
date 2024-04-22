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

root.mainloop()