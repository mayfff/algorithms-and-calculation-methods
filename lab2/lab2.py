import time
from tkinter import *
from tkinter import messagebox, filedialog
from random import randint
import re, os, sys
from PIL import ImageTk

BG = "#787878"
FONT = ("Arial", 18, "bold")
BUTTONCOLOR = "#FFFF63"
BUTTONFONT = ("Arial", 20)

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

def inputData():
    def activation():
        value = var.get()
        if value == 1:
            soloButton["state"] = "normal"
            manyButton["state"] = "disabled"

        elif value == 2:
            soloButton["state"] = "disabled"
            manyButton["state"] = "normal"

    def confirm():
        value = var.get()
        if value == 1:
            for i in range(int(soloEntry.get())):
                firstList.append(randint(-5000, 5000))
                secondList.append(randint(-5000, 5000))
                thirdList.append(randint(-5000, 5000))
                fourthList.append(randint(-5000, 5000))
                fifthList.append(randint(-5000, 5000))
                sixthList.append(randint(-5000, 5000))
                seventhList.append(randint(-5000, 5000))
                eighthList.append(randint(-5000, 5000))
                ninenthList.append(randint(-5000, 5000))
                tenthList.append(randint(-5000, 5000))

            messagebox.showinfo(title="Результат", message="Масиви заповнені")
            inputWindow.destroy()

        elif value == 2:
            for i in range(int(firstEntry.get())):
                firstList.append(randint(-5000, 5000))

            for i in range(int(secondEntry.get())):
                secondList.append(randint(-5000, 5000))

            for i in range(int(thirdEntry.get())):
                thirdList.append(randint(-5000, 5000))

            for i in range(int(fourthEntry.get())):
                fourthList.append(randint(-5000, 5000))

            for i in range(int(fifthEntry.get())):
                fifthList.append(randint(-5000, 5000))

            for i in range(int(sixthEntry.get())):
                sixthList.append(randint(-5000, 5000))

            for i in range(int(seventhEntry.get())):
                seventhList.append(randint(-5000, 5000))

            for i in range(int(eighthEntry.get())):
                eighthList.append(randint(-5000, 5000))

            for i in range(int(ninethEntry.get())):
                ninethList.append(randint(-5000, 5000))

            for i in range(int(tenthEntry.get())):
                tenthList.append(randint(-5000, 5000))

            messagebox.showinfo(title="Результат", message="Масиви заповнені")
            inputWindow.destroy()

    def manyInput():
        filepath = filedialog.askopenfilename(initialdir='/',
                                              title="Відкриття файлу",
                                              filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        with open(filepath, 'r') as file:
            values = re.split(r'\s+', file.read())
            if len(values) != 10:
                messagebox.showerror(title="Помилка", message="В файлі має бути 10 значень")
            else:
                firstEntry.delete(0, END)
                secondEntry.delete(0, END)
                thirdEntry.delete(0, END)
                fourthEntry.delete(0, END)
                fifthEntry.delete(0, END)
                sixthEntry.delete(0, END)
                seventhEntry.delete(0, END)
                eighthEntry.delete(0, END)
                ninethEntry.delete(0, END)
                tenthEntry.delete(0, END)

                firstEntry.insert(0, int(values[0]))
                secondEntry.insert(0, int(values[1]))
                thirdEntry.insert(0, int(values[2]))
                fourthEntry.insert(0, int(values[3]))
                fifthEntry.insert(0, int(values[4]))
                sixthEntry.insert(0, int(values[5]))
                seventhEntry.insert(0, int(values[6]))
                eighthEntry.insert(0, int(values[7]))
                ninethEntry.insert(0, int(values[8]))
                tenthEntry.insert(0, int(values[9]))

    def soloInput():
        filepath = filedialog.askopenfilename(initialdir='/',
                                              title="Відкриття файлу",
                                              filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        with open(filepath, 'r') as file:
            value = file.read()
            soloEntry.delete(0, END)
            soloEntry.insert(0, value)

    inputWindow = Toplevel(root)
    inputWindow.title("Введення даних")
    inputWindow.geometry("800x800")
    inputWindow.resizable(False, False)
    inputWindow.configure(bg=BG)

    Grid.columnconfigure(inputWindow, 0, weight=1)
    Grid.columnconfigure(inputWindow, 1, weight=1)

    Label(inputWindow, text=" ", bg=BG, font=FONT).grid(row=0, columnspan=2, pady=5)
    Label(inputWindow, text="Введення довжини масивів", bg=BG, font=FONT).grid(row=1, columnspan=2)
    Label(inputWindow, text="___" * 1000, bg=BG, font=FONT).grid(row=2, columnspan=2, pady=10)

    Radiobutton(inputWindow, variable=var, value=1, command=activation, text="Масиви однакової довжини", bg=BG,
                font=FONT).grid(row=3, column=0, sticky="w", padx=10)

    soloEntry = Entry(inputWindow, width=20)
    soloEntry.grid(row=4, column=0, sticky="e", padx=(0, 40), pady=5)
    Label(inputWindow, text="Введіть довжину:", bg=BG, font=FONT).grid(row=4, column=0, sticky="w", padx=15, pady=5)

    soloButton = Button(inputWindow, text="Ввести з файлу", font=BUTTONFONT, bg=BUTTONCOLOR, command=soloInput,
                        state="disabled")
    soloButton.grid(row=5, column=0, pady=5)

    Radiobutton(inputWindow, variable=var, value=2, command=activation, text="Масиви різної довжини", bg=BG,
                font=FONT).grid(row=3, column=1, sticky="w", padx=10)

    firstEntry = Entry(inputWindow, width=20)
    firstEntry.grid(row=4, column=1, sticky="e", padx=(0, 40), pady=5)
    Label(inputWindow, text="1-ий масив:", bg=BG, font=FONT).grid(row=4, column=1, sticky="w", padx=15, pady=5)

    secondEntry = Entry(inputWindow, width=20)
    secondEntry.grid(row=5, column=1, sticky="e", padx=(0, 40), pady=5)
    Label(inputWindow, text="2-ий масив:", bg=BG, font=FONT).grid(row=5, column=1, sticky="w", padx=15, pady=5)

    thirdEntry = Entry(inputWindow, width=20)
    thirdEntry.grid(row=6, column=1, sticky="e", padx=(0, 40), pady=5)
    Label(inputWindow, text="3-ій масив:", bg=BG, font=FONT).grid(row=6, column=1, sticky="w", padx=15, pady=5)

    fourthEntry = Entry(inputWindow, width=20)
    fourthEntry.grid(row=7, column=1, sticky="e", padx=(0, 40), pady=5)
    Label(inputWindow, text="4-ий масив:", bg=BG, font=FONT).grid(row=7, column=1, sticky="w", padx=15, pady=5)

    fifthEntry = Entry(inputWindow, width=20)
    fifthEntry.grid(row=8, column=1, sticky="e", padx=(0, 40), pady=5)
    Label(inputWindow, text="5-ий масив:", bg=BG, font=FONT).grid(row=8, column=1, sticky="w", padx=15, pady=5)

    sixthEntry = Entry(inputWindow, width=20)
    sixthEntry.grid(row=9, column=1, sticky="e", padx=(0, 40), pady=5)
    Label(inputWindow, text="6-ий масив:", bg=BG, font=FONT).grid(row=9, column=1, sticky="w", padx=15, pady=5)

    seventhEntry = Entry(inputWindow, width=20)
    seventhEntry.grid(row=10, column=1, sticky="e", padx=(0, 40), pady=5)
    Label(inputWindow, text="7-ий масив:", bg=BG, font=FONT).grid(row=10, column=1, sticky="w", padx=15, pady=5)

    eighthEntry = Entry(inputWindow, width=20)
    eighthEntry.grid(row=11, column=1, sticky="e", padx=(0, 40), pady=5)
    Label(inputWindow, text="8-ий масив:", bg=BG, font=FONT).grid(row=11, column=1, sticky="w", padx=15, pady=5)

    ninethEntry = Entry(inputWindow, width=20)
    ninethEntry.grid(row=12, column=1, sticky="e", padx=(0, 40), pady=5)
    Label(inputWindow, text="9-ий масив:", bg=BG, font=FONT).grid(row=12, column=1, sticky="w", padx=15, pady=5)

    tenthEntry = Entry(inputWindow, width=20)
    tenthEntry.grid(row=13, column=1, sticky="e", padx=(0, 40), pady=5)
    Label(inputWindow, text="10-ий масив:", bg=BG, font=FONT).grid(row=13, column=1, sticky="w", padx=15, pady=5)

    manyButton = Button(inputWindow, text="Ввести з файлу", font=BUTTONFONT, bg=BUTTONCOLOR, command=manyInput,
                        state="disabled")
    manyButton.grid(row=14, column=1, pady=5)

    confirmButton = Button(inputWindow, text="Заповнити масиви", bg=BUTTONCOLOR, font=BUTTONFONT, command=confirm)
    confirmButton.grid(row=15, columnspan=2, sticky="NS", pady=5)

def draw():
    pass

firstList = []
secondList = []
thirdList = []
fourthList = []
fifthList = []
sixthList = []
seventhList = []
eighthList = []
ninethList = []
tenthList = []

root = Tk()
var = IntVar()
root.title("Головне вікно. Лабораторна №2")
root.geometry("1200x600")
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
path = resource_path('files/task.png')
img = ImageTk.PhotoImage(file=path)
Label(root, image=img).grid(row=5, columnspan=2, pady=5)
Label(root, text="___" * 1000, bg=BG, fg="white", font=FONT).grid(row=6, columnspan=2, pady=10)

inputButton = Button(root, text="Введення даних", bg=BUTTONCOLOR, font=BUTTONFONT, command=inputData, height=7,
                     width=20)
inputButton.grid(row=7, column=0)

drawButton = Button(root, text="Будування графіків", bg=BUTTONCOLOR, font=BUTTONFONT, command=draw, height=7, width=20)
drawButton.grid(row=7, column=1)

root.mainloop()
