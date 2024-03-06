from tkinter import *
from tkinter import messagebox, filedialog
import re, os, sys
from math import sqrt, sin, cos, log
from PIL import ImageTk


BG = "#787878"
FONT = ("Arial", 18, "bold")
BUTTONCOLOR = "#FFFF63"
BUTTONFONT = ("Arial", 20)

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def firstTask():
    def inputWindow():
        def success():
            try:
                global a, b
                a = float(entryA.get().replace(',', '.'))
                b = float(entryB.get().replace(',', '.'))
            except ValueError:
                messagebox.showerror(title="Помилка", message="Помилка введення")

            try:
                global y
                y = sqrt(sin(a / 6) + cos(b / 6)) + sqrt(2 * sin(a / 6) * cos(b / 6))

                messagebox.showinfo(title="Успіх", message="Значення введено")
                firstInputWindow.destroy()
            except ValueError:
                messagebox.showerror(title="Помилка", message="Підкореневий вираз менше нуля")

        def deny():
            messagebox.showinfo(title="Скасовано", message="Введення скасовано")
            firstInputWindow.destroy()

        def fileInput():
            filepath = filedialog.askopenfilename(initialdir='/',
                                                  title="Відкриття файлу",
                                                  filetypes=(("text files", "*.txt"), ("all files", "*.*")))

            with open(filepath, 'r') as file:
                values = re.split(r'\s+', file.read())
                if len(values) != 2:
                    messagebox.showerror(title="Помилка", message="В файлі має бути 2 значення")
                else:
                    try:
                        entryA.delete(0, END)
                        entryB.delete(0, END)
                        entryA.insert(0, float(values[0].replace(',', '.')))
                        entryB.insert(0, float(values[1].replace(',', '.')))
                    except ValueError:
                        messagebox.showerror(title="Помилка", message="Помилка введення\nВ файлі мають бути лише числа")

        firstInputWindow = Toplevel(firstTaskWindow)
        firstInputWindow.title("Введення даних")
        firstInputWindow.resizable(False, False)
        firstInputWindow.geometry("400x200")
        firstInputWindow.configure(bg=BG)

        Grid.columnconfigure(firstInputWindow, 0, weight=1)
        Grid.columnconfigure(firstInputWindow, 1, weight=1)

        Label(firstInputWindow, text="Значення А: ", bg=BG, fg="white", font=FONT).grid(row=0, column=0, pady=5)
        Label(firstInputWindow, text="Значення B: ", bg=BG, fg="white", font=FONT).grid(row=0, column=1, pady=5)

        global entryA, entryB
        entryA = Entry(firstInputWindow, width=30)
        entryA.grid(row=1, column=0, sticky="w", padx=5)
        entryB = Entry(firstInputWindow, width=30)
        entryB.grid(row=1, column=1, sticky="e", padx=5)

        successButton = Button(firstInputWindow, text="Ввести", bg=BUTTONCOLOR, font=BUTTONFONT, command=success)
        successButton.grid(row=2, column=0, sticky="w", padx=40, pady=20)

        denyButton = Button(firstInputWindow, text="Скасувати", bg=BUTTONCOLOR, font=BUTTONFONT, command=deny)
        denyButton.grid(row=2, column=1, sticky="e", padx=20, pady=20)

        fileButton = Button(firstInputWindow, text="Ввести з файлу", bg=BUTTONCOLOR, command=fileInput)
        fileButton.grid(row=3, column=0, sticky="w", padx=40)

    def outputWindow():
        firstOutputWindow = Toplevel(firstTaskWindow)
        firstOutputWindow.title("Результат обчислення")
        firstOutputWindow.resizable(False, False)
        firstOutputWindow.geometry("400x200")
        firstOutputWindow.configure(bg=BG)

        Grid.columnconfigure(firstOutputWindow, 0, weight=1)
        Grid.columnconfigure(firstOutputWindow, 1, weight=1)

        Label(firstOutputWindow, text=f"Значення А: {a}", bg=BG, fg="white", font=FONT).grid(row=0, column=0, pady=5)
        Label(firstOutputWindow, text=f"Значення B: {b}", bg=BG, fg="white", font=FONT).grid(row=1, column=0, pady=5)
        Label(firstOutputWindow, text=f"Значення Y1: {y:.2f}", bg=BG, fg="white", font=FONT).grid(row=2, column=0,
                                                                                                  pady=5)

    global img
    path = resource_path('first.png')
    img = ImageTk.PhotoImage(file=path)

    firstTaskWindow = Toplevel(root)
    firstTaskWindow.title("Вираз №1")
    firstTaskWindow.resizable(True, True)
    firstTaskWindow.geometry("800x600")
    firstTaskWindow.configure(bg=BG)

    Grid.columnconfigure(firstTaskWindow, 0, weight=1)
    Grid.columnconfigure(firstTaskWindow, 1, weight=1)

    Label(firstTaskWindow, text=" ", bg=BG, fg="white", font=FONT).grid(row=0, columnspan=2, pady=5)
    Label(firstTaskWindow, text="Лінійний алгоритм", bg=BG, font=FONT, fg="white").grid(row=1, columnspan=2)
    Label(firstTaskWindow, image=img).grid(row=2, columnspan=2)

    inputButton = Button(firstTaskWindow, text="Введення даних", bg=BUTTONCOLOR, font=BUTTONFONT, command=inputWindow)
    inputButton.grid(row=3, column=0, sticky="w", padx=30, pady=40)

    outputButton = Button(firstTaskWindow, text="Результат обчислення", bg=BUTTONCOLOR, font=BUTTONFONT,
                          command=outputWindow)
    outputButton.grid(row=3, column=1, sticky="e", padx=25, pady=40)


def secondTask():
    def inputWindow():
        def success():
            try:
                global k, x
                k = float(entryK.get().replace(',', '.'))
                x = float(entryX.get().replace(',', '.'))
            except ValueError:
                messagebox.showerror(title="Помилка", message="Помилка введення")

            if k * x <= 0:
                messagebox.showerror(title="Помилка", message="Значення під знаком логарифма має бути > 0")
                return

            try:
                global y
                y = k * x * x * log(k * x, 10) + sqrt(x)

                messagebox.showinfo(title="Успіх", message="Значення введено")
                secondInputWindow.destroy()
            except ValueError:
                messagebox.showerror(title="Помилка", message="Підкореневий вираз менше нуля")

        def deny():
            messagebox.showinfo(title="Скасовано", message="Введення скасовано")
            secondInputWindow.destroy()

        def fileInput():
            filepath = filedialog.askopenfilename(initialdir='/',
                                                  title="Відкриття файлу",
                                                  filetypes=(("text files", "*.txt"), ("all files", "*.*")))

            with open(filepath, 'r') as file:
                values = re.split(r'\s+', file.read())
                if len(values) != 2:
                    messagebox.showerror(title="Помилка", message="В файлі має бути 2 значення")
                else:
                    try:
                        entryK.delete(0, END)
                        entryX.delete(0, END)
                        entryK.insert(0, float(values[0].replace(',', '.')))
                        entryX.insert(0, float(values[1].replace(',', '.')))
                    except ValueError:
                        messagebox.showerror(title="Помилка", message="Помилка введення\nВ файлі мають бути лише числа")

        secondInputWindow = Toplevel(secondTaskWindow)
        secondInputWindow.title("Введення даних")
        secondInputWindow.resizable(False, False)
        secondInputWindow.geometry("400x200")
        secondInputWindow.configure(bg=BG)

        Grid.columnconfigure(secondInputWindow, 0, weight=1)
        Grid.columnconfigure(secondInputWindow, 1, weight=1)

        Label(secondInputWindow, text="Значення k: ", bg=BG, fg="white", font=FONT).grid(row=0, column=0, pady=5)
        Label(secondInputWindow, text="Значення x: ", bg=BG, fg="white", font=FONT).grid(row=0, column=1, pady=5)

        global entryK, entryX
        entryK = Entry(secondInputWindow, width=30)
        entryK.grid(row=1, column=0, sticky="w", padx=5)
        entryX = Entry(secondInputWindow, width=30)
        entryX.grid(row=1, column=1, sticky="e", padx=5)

        successButton = Button(secondInputWindow, text="Ввести", bg=BUTTONCOLOR, font=BUTTONFONT, command=success)
        successButton.grid(row=2, column=0, sticky="w", padx=40, pady=20)

        denyButton = Button(secondInputWindow, text="Скасувати", bg=BUTTONCOLOR, font=BUTTONFONT, command=deny)
        denyButton.grid(row=2, column=1, sticky="e", padx=20, pady=20)

        fileButton = Button(secondInputWindow, text="Ввести з файлу", bg=BUTTONCOLOR, command=fileInput)
        fileButton.grid(row=3, column=0, sticky="w", padx=40)

    def outputWindow():
        secondOutputWindow = Toplevel(secondTaskWindow)
        secondOutputWindow.title("Результат обчислення")
        secondOutputWindow.resizable(False, False)
        secondOutputWindow.geometry("400x200")
        secondOutputWindow.configure(bg=BG)

        Grid.columnconfigure(secondOutputWindow, 0, weight=1)
        Grid.columnconfigure(secondOutputWindow, 1, weight=1)

        Label(secondOutputWindow, text=f"Значення k: {k}", bg=BG, fg="white", font=FONT).grid(row=0, column=0, pady=5)
        Label(secondOutputWindow, text=f"Значення x: {x}", bg=BG, fg="white", font=FONT).grid(row=1, column=0, pady=5)
        Label(secondOutputWindow, text=f"Значення y: {y:.2f}", bg=BG, fg="white", font=FONT).grid(row=2, column=0,
                                                                                                  pady=5)

    global img
    path = resource_path('second.png')
    img = ImageTk.PhotoImage(file=path)

    secondTaskWindow = Toplevel(root)
    secondTaskWindow.title("Вираз №2")
    secondTaskWindow.resizable(True, True)
    secondTaskWindow.geometry("800x600")
    secondTaskWindow.configure(bg=BG)

    Grid.columnconfigure(secondTaskWindow, 0, weight=1)
    Grid.columnconfigure(secondTaskWindow, 1, weight=1)

    Label(secondTaskWindow, text=" ", bg=BG, fg="white", font=FONT).grid(row=0, columnspan=2, pady=5)
    Label(secondTaskWindow, text="Алгоритм з розгалуженням", bg=BG, font=FONT, fg="white").grid(row=1, columnspan=2)
    Label(secondTaskWindow, image=img).grid(row=2, columnspan=2)

    inputButton = Button(secondTaskWindow, text="Введення даних", bg=BUTTONCOLOR, font=BUTTONFONT, command=inputWindow)
    inputButton.grid(row=3, column=0, sticky="w", padx=30, pady=40)

    outputButton = Button(secondTaskWindow, text="Результат обчислення", bg=BUTTONCOLOR, font=BUTTONFONT,
                          command=outputWindow)
    outputButton.grid(row=3, column=1, sticky="e", padx=25, pady=40)


def thirdTask():
    def inputWindow():
        def success():
            try:
                global n, b
                n = int(entryN.get())
                b = float(entryB.get().replace(',', '.'))
            except ValueError:
                messagebox.showerror(title="Помилка", message="Помилка введення")

            global f, a, k
            f = 1
            a = 1
            while a <= n:
                k = 1
                summa = 0
                while k <= a:
                    summa += (a ** k + b / k)
                    k += 1
                f *= summa
                a += 1

            messagebox.showinfo(title="Успіх", message="Значення введено")
            thirdInputWindow.destroy()

        def deny():
            messagebox.showinfo(title="Скасовано", message="Введення скасовано")
            thirdInputWindow.destroy()

        def fileInput():
            filepath = filedialog.askopenfilename(initialdir='/',
                                                  title="Відкриття файлу",
                                                  filetypes=(("text files", "*.txt"), ("all files", "*.*")))

            with open(filepath, 'r') as file:
                values = re.split(r'\s+', file.read())
                if len(values) != 2:
                    messagebox.showerror(title="Помилка", message="В файлі має бути 2 значення")
                else:
                    try:
                        entryK.delete(0, END)
                        entryX.delete(0, END)
                        entryK.insert(0, float(values[0].replace(',', '.')))
                        entryX.insert(0, float(values[1].replace(',', '.')))
                    except ValueError:
                        messagebox.showerror(title="Помилка", message="Помилка введення\nВ файлі мають бути лише числа")

        thirdInputWindow = Toplevel(thirdTaskWindow)
        thirdInputWindow.title("Введення даних")
        thirdInputWindow.resizable(False, False)
        thirdInputWindow.geometry("400x200")
        thirdInputWindow.configure(bg=BG)

        Grid.columnconfigure(thirdInputWindow, 0, weight=1)
        Grid.columnconfigure(thirdInputWindow, 1, weight=1)

        Label(thirdInputWindow, text="Значення n: ", bg=BG, fg="white", font=FONT).grid(row=0, column=0, pady=5)
        Label(thirdInputWindow, text="Значення b: ", bg=BG, fg="white", font=FONT).grid(row=0, column=1, pady=5)

        global entryN, entryB
        entryN = Entry(thirdInputWindow, width=30)
        entryN.grid(row=1, column=0, sticky="w", padx=5)
        entryB = Entry(thirdInputWindow, width=30)
        entryB.grid(row=1, column=1, sticky="e", padx=5)

        successButton = Button(thirdInputWindow, text="Ввести", bg=BUTTONCOLOR, font=BUTTONFONT, command=success)
        successButton.grid(row=2, column=0, sticky="w", padx=40, pady=20)

        denyButton = Button(thirdInputWindow, text="Скасувати", bg=BUTTONCOLOR, font=BUTTONFONT, command=deny)
        denyButton.grid(row=2, column=1, sticky="e", padx=20, pady=20)

        fileButton = Button(thirdInputWindow, text="Ввести з файлу", bg=BUTTONCOLOR, command=fileInput)
        fileButton.grid(row=3, column=0, sticky="w", padx=40)

    def outputWindow():
        thirdOutputWindow = Toplevel(thirdTaskWindow)
        thirdOutputWindow.title("Результат обчислення")
        thirdOutputWindow.resizable(False, False)
        thirdOutputWindow.geometry("400x200")
        thirdOutputWindow.configure(bg=BG)

        Grid.columnconfigure(thirdOutputWindow, 0, weight=1)
        Grid.columnconfigure(thirdOutputWindow, 1, weight=1)

        Label(thirdOutputWindow, text=f"Значення n: {n}", bg=BG, fg="white", font=FONT).grid(row=0, column=0, pady=5)
        Label(thirdOutputWindow, text=f"Значення b: {b}", bg=BG, fg="white", font=FONT).grid(row=1, column=0, pady=5)
        Label(thirdOutputWindow, text=f"Значення f: {f:.2f}", bg=BG, fg="white", font=FONT).grid(row=2, column=0,
                                                                                                 pady=5)

    global img
    path = resource_path('third.png')
    img = ImageTk.PhotoImage(file=path)

    thirdTaskWindow = Toplevel(root)
    thirdTaskWindow.title("Вираз №3")
    thirdTaskWindow.resizable(True, True)
    thirdTaskWindow.geometry("800x600")
    thirdTaskWindow.configure(bg=BG)

    Grid.columnconfigure(thirdTaskWindow, 0, weight=1)
    Grid.columnconfigure(thirdTaskWindow, 1, weight=1)

    Label(thirdTaskWindow, text=" ", bg=BG, fg="white", font=FONT).grid(row=0, columnspan=2, pady=5)
    Label(thirdTaskWindow, text="Циклічний алгоритм", bg=BG, font=FONT, fg="white").grid(row=1, columnspan=2)
    Label(thirdTaskWindow, image=img).grid(row=2, columnspan=2)

    inputButton = Button(thirdTaskWindow, text="Введення даних", bg=BUTTONCOLOR, font=BUTTONFONT, command=inputWindow)
    inputButton.grid(row=3, column=0, sticky="w", padx=30, pady=40)

    outputButton = Button(thirdTaskWindow, text="Результат обчислення", bg=BUTTONCOLOR, font=BUTTONFONT,
                          command=outputWindow)
    outputButton.grid(row=3, column=1, sticky="e", padx=25, pady=40)


root = Tk()
root.title("Головне вікно. Лабораторна №1")
root.geometry("1600x900")
root.resizable(True, True)
root.configure(bg=BG)

Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)

Label(root, text=" ", bg=BG, font=FONT).grid(row=0, columnspan=3, pady=5)
Label(root, text="Інформація про студента", bg=BG, fg="white", font=FONT).grid(row=1, columnspan=3)
Label(root, text="ПІБ: Закревський Данило Сергійович", bg=BG, fg="white", font=FONT).grid(row=2, columnspan=3)
Label(root, text="Група: ІО-24", bg=BG, fg="white", font=FONT).grid(row=3, columnspan=3)
Label(root, text="Варіант: 11", bg=BG, fg="white", font=FONT).grid(row=4, columnspan=3)

Label(root, text="___" * 1000, bg=BG, fg="white", font=FONT).grid(row=5, columnspan=3, ipady=20)

firstTaskButton = Button(root, text="Вираз 1", bg=BUTTONCOLOR, font=BUTTONFONT, command=firstTask, width=22, height=5)
firstTaskButton.grid(row=6, column=0, sticky="w", padx=20)

secondTaskButton = Button(root, text="Вираз 2", bg=BUTTONCOLOR, font=BUTTONFONT, command=secondTask, width=22, height=5)
secondTaskButton.grid(row=6, column=1)

thirdTaskButton = Button(root, text="Вираз 3", bg=BUTTONCOLOR, font=BUTTONFONT, command=thirdTask, width=22, height=5)
thirdTaskButton.grid(row=6, column=2, sticky="e", padx=25)
root.mainloop()
