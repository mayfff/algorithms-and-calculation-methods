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
    def swapRows(row1, row2):
        matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
        free[row1], free[row2] = free[row2], free[row1]

    def gauss():
        global X

        for k in range(3):
            for i in range(k + 1, 4):
                if matrix[k][k] == 0:
                    swapRows(k, i)

                M = matrix[i][k] / matrix[k][k]

                for j in range(k, 4):
                    matrix[i][j] -= M * matrix[k][j]

                free[i] -= free[k] * M

        X = [0, 0, 0, 0]
        x4 = free[3] / matrix[3][3]
        X[3] = x4
        for i in range(2, -1, -1):
            S = 0
            for j in range(i + 1, 4):
                S += matrix[i][j] * X[j]
            X[i] = (free[i] - S) / matrix[i][i]

    gauss()

    for i in range(len(matrix)):
        print(matrix[i], free[i])
    print(X)

    resultTable = Toplevel(root)
    resultTable.configure(bg=BG)
    resultTable.title("результат")
    resultTable.resizable(False, False)

    entryx1 = Entry(resultTable, width=25, justify="center")
    entryx1.config(font=("Helvetica", 12, "bold"))
    entryx1.insert(0, "X1")
    entryx1.grid(row=0, column=0)

    entryx2 = Entry(resultTable, width=25, justify="center")
    entryx2.config(font=("Helvetica", 12, "bold"))
    entryx2.insert(0, "X2")
    entryx2.grid(row=0, column=1)

    entryx3 = Entry(resultTable, width=25, justify="center")
    entryx3.config(font=("Helvetica", 12, "bold"))
    entryx3.insert(0, "X3")
    entryx3.grid(row=0, column=2)

    entryx4 = Entry(resultTable, width=25, justify="center")
    entryx4.config(font=("Helvetica", 12, "bold"))
    entryx4.insert(0, "X4")
    entryx4.grid(row=0, column=3)

    entryfree = Entry(resultTable, width=25, justify="center")
    entryfree.config(font=("Helvetica", 12, "bold"))
    entryfree.insert(0, "Вільні члени")
    entryfree.grid(row=0, column=4)

    entry11 = Entry(resultTable, width=25, justify="center")
    entry11.config(font=("Helvetica", 12, "bold"))
    entry11.insert(0, matrix[0][0])
    entry11.grid(row=1, column=0)

    entry12 = Entry(resultTable, width=25, justify="center")
    entry12.config(font=("Helvetica", 12, "bold"))
    entry12.insert(0, round(matrix[0][1], 3))
    entry12.grid(row=1, column=1)

    entry13 = Entry(resultTable, width=25, justify="center")
    entry13.config(font=("Helvetica", 12, "bold"))
    entry13.insert(0, round(matrix[0][2], 3))
    entry13.grid(row=1, column=2)

    entry14 = Entry(resultTable, width=25, justify="center")
    entry14.config(font=("Helvetica", 12, "bold"))
    entry14.insert(0, round(matrix[0][3], 3))
    entry14.grid(row=1, column=3)

    entry15 = Entry(resultTable, width=25, justify="center")
    entry15.config(font=("Helvetica", 12, "bold"))
    entry15.insert(0, round(free[0], 3))
    entry15.grid(row=1, column=4)

    entry21 = Entry(resultTable, width=25, justify="center")
    entry21.config(font=("Helvetica", 12, "bold"))
    entry21.insert(0, round(matrix[1][0], 3))
    entry21.grid(row=2, column=0)

    entry22 = Entry(resultTable, width=25, justify="center")
    entry22.config(font=("Helvetica", 12, "bold"))
    entry22.insert(0, round(matrix[1][1], 3))
    entry22.grid(row=2, column=1)

    entry23 = Entry(resultTable, width=25, justify="center")
    entry23.config(font=("Helvetica", 12, "bold"))
    entry23.insert(0, round(matrix[1][2], 3))
    entry23.grid(row=2, column=2)

    entry24 = Entry(resultTable, width=25, justify="center")
    entry24.config(font=("Helvetica", 12, "bold"))
    entry24.insert(0, round(matrix[1][3], 3))
    entry24.grid(row=2, column=3)

    entry25 = Entry(resultTable, width=25, justify="center")
    entry25.config(font=("Helvetica", 12, "bold"))
    entry25.insert(0, round(free[1], 3))
    entry25.grid(row=2, column=4)

    entry31 = Entry(resultTable, width=25, justify="center")
    entry31.config(font=("Helvetica", 12, "bold"))
    entry31.insert(0, round(matrix[2][0], 3))
    entry31.grid(row=3, column=0)

    entry32 = Entry(resultTable, width=25, justify="center")
    entry32.config(font=("Helvetica", 12, "bold"))
    entry32.insert(0, round(matrix[2][1], 3))
    entry32.grid(row=3, column=1)

    entry33 = Entry(resultTable, width=25, justify="center")
    entry33.config(font=("Helvetica", 12, "bold"))
    entry33.insert(0, round(matrix[2][2], 3))
    entry33.grid(row=3, column=2)

    entry34 = Entry(resultTable, width=25, justify="center")
    entry34.config(font=("Helvetica", 12, "bold"))
    entry34.insert(0, round(matrix[2][3], 3))
    entry34.grid(row=3, column=3)

    entry35 = Entry(resultTable, width=25, justify="center")
    entry35.config(font=("Helvetica", 12, "bold"))
    entry35.insert(0, round(free[2], 3))
    entry35.grid(row=3, column=4)

    entry41 = Entry(resultTable, width=25, justify="center")
    entry41.config(font=("Helvetica", 12, "bold"))
    entry41.insert(0, round(matrix[3][0], 3))
    entry41.grid(row=4, column=0)

    entry42 = Entry(resultTable, width=25, justify="center")
    entry42.config(font=("Helvetica", 12, "bold"))
    entry42.insert(0, round(matrix[3][1], 3))
    entry42.grid(row=4, column=1)

    entry43 = Entry(resultTable, width=25, justify="center")
    entry43.config(font=("Helvetica", 12, "bold"))
    entry43.insert(0, round(matrix[3][2], 3))
    entry43.grid(row=4, column=2)

    entry44 = Entry(resultTable, width=25, justify="center")
    entry44.config(font=("Helvetica", 12, "bold"))
    entry44.insert(0, round(matrix[3][3], 3))
    entry44.grid(row=4, column=3)

    entry45 = Entry(resultTable, width=25, justify="center")
    entry45.config(font=("Helvetica", 12, "bold"))
    entry45.insert(0, round(free[3], 3))
    entry45.grid(row=4, column=4)

    Label(resultTable, text=f"Корені: {X[0]}, {X[1]}, {X[2]}, {X[3]}", font=FONT, bg=BG, fg="white").grid(row=5,
                                                                                                          columnspan=5,
                                                                                                          pady=15)


def getMatrix():
    def enter():
        global matrix, free
        firstRow = [float(entry11.get().replace(',', '.')), float(entry12.get().replace(',', '.')),
                    float(entry13.get().replace(',', '.')), float(entry14.get().replace(',', '.'))]
        secondRow = [float(entry21.get().replace(',', '.')), float(entry22.get().replace(',', '.')),
                     float(entry23.get().replace(',', '.')), float(entry24.get().replace(',', '.'))]
        thirdRow = [float(entry31.get().replace(',', '.')), float(entry32.get().replace(',', '.')),
                    float(entry33.get().replace(',', '.')), float(entry34.get().replace(',', '.'))]
        fourthRow = [float(entry41.get().replace(',', '.')), float(entry42.get().replace(',', '.')),
                     float(entry43.get().replace(',', '.')), float(entry44.get().replace(',', '.'))]
        free = [float(entry15.get().replace(',', '.')), float(entry25.get().replace(',', '.')),
                float(entry35.get().replace(',', '.')), float(entry45.get().replace(',', '.'))]

        matrix.append(firstRow)
        matrix.append(secondRow)
        matrix.append(thirdRow)
        matrix.append(fourthRow)

    resultButton["state"] = NORMAL

    table = Toplevel(root)
    table.configure(bg=BG)
    table.title("введення матриці")
    table.resizable(False, False)

    entryx1 = Entry(table, width=25, justify="center")
    entryx1.config(font=("Helvetica", 12, "bold"))
    entryx1.insert(0, "X1")
    entryx1.grid(row=0, column=0)

    entryx2 = Entry(table, width=25, justify="center")
    entryx2.config(font=("Helvetica", 12, "bold"))
    entryx2.insert(0, "X2")
    entryx2.grid(row=0, column=1)

    entryx3 = Entry(table, width=25, justify="center")
    entryx3.config(font=("Helvetica", 12, "bold"))
    entryx3.insert(0, "X3")
    entryx3.grid(row=0, column=2)

    entryx4 = Entry(table, width=25, justify="center")
    entryx4.config(font=("Helvetica", 12, "bold"))
    entryx4.insert(0, "X4")
    entryx4.grid(row=0, column=3)

    entryfree = Entry(table, width=25, justify="center")
    entryfree.config(font=("Helvetica", 12, "bold"))
    entryfree.insert(0, "Вільні члени")
    entryfree.grid(row=0, column=4)

    entry11 = Entry(table, width=25, justify="center")
    entry11.config(font=("Helvetica", 12, "bold"))
    entry11.insert(0, "8.7")
    entry11.grid(row=1, column=0)

    entry12 = Entry(table, width=25, justify="center")
    entry12.config(font=("Helvetica", 12, "bold"))
    entry12.insert(0, "-3.1")
    entry12.grid(row=1, column=1)

    entry13 = Entry(table, width=25, justify="center")
    entry13.config(font=("Helvetica", 12, "bold"))
    entry13.insert(0, "1.8")
    entry13.grid(row=1, column=2)

    entry14 = Entry(table, width=25, justify="center")
    entry14.config(font=("Helvetica", 12, "bold"))
    entry14.insert(0, "2.2")
    entry14.grid(row=1, column=3)

    entry15 = Entry(table, width=25, justify="center")
    entry15.config(font=("Helvetica", 12, "bold"))
    entry15.insert(0, "-9.7")
    entry15.grid(row=1, column=4)

    entry21 = Entry(table, width=25, justify="center")
    entry21.config(font=("Helvetica", 12, "bold"))
    entry21.insert(0, "2.1")
    entry21.grid(row=2, column=0)

    entry22 = Entry(table, width=25, justify="center")
    entry22.config(font=("Helvetica", 12, "bold"))
    entry22.insert(0, "6.7")
    entry22.grid(row=2, column=1)

    entry23 = Entry(table, width=25, justify="center")
    entry23.config(font=("Helvetica", 12, "bold"))
    entry23.insert(0, "-2.2")
    entry23.grid(row=2, column=2)

    entry24 = Entry(table, width=25, justify="center")
    entry24.config(font=("Helvetica", 12, "bold"))
    entry24.insert(0, "0")
    entry24.grid(row=2, column=3)

    entry25 = Entry(table, width=25, justify="center")
    entry25.config(font=("Helvetica", 12, "bold"))
    entry25.insert(0, "13.1")
    entry25.grid(row=2, column=4)

    entry31 = Entry(table, width=25, justify="center")
    entry31.config(font=("Helvetica", 12, "bold"))
    entry31.insert(0, "3.2")
    entry31.grid(row=3, column=0)

    entry32 = Entry(table, width=25, justify="center")
    entry32.config(font=("Helvetica", 12, "bold"))
    entry32.insert(0, "-1.8")
    entry32.grid(row=3, column=1)

    entry33 = Entry(table, width=25, justify="center")
    entry33.config(font=("Helvetica", 12, "bold"))
    entry33.insert(0, "-9.5")
    entry33.grid(row=3, column=2)

    entry34 = Entry(table, width=25, justify="center")
    entry34.config(font=("Helvetica", 12, "bold"))
    entry34.insert(0, "-1.9")
    entry34.grid(row=3, column=3)

    entry35 = Entry(table, width=25, justify="center")
    entry35.config(font=("Helvetica", 12, "bold"))
    entry35.insert(0, "6.9")
    entry35.grid(row=3, column=4)

    entry41 = Entry(table, width=25, justify="center")
    entry41.config(font=("Helvetica", 12, "bold"))
    entry41.insert(0, "1.2")
    entry41.grid(row=4, column=0)

    entry42 = Entry(table, width=25, justify="center")
    entry42.config(font=("Helvetica", 12, "bold"))
    entry42.insert(0, "2.8")
    entry42.grid(row=4, column=1)

    entry43 = Entry(table, width=25, justify="center")
    entry43.config(font=("Helvetica", 12, "bold"))
    entry43.insert(0, "-1.4")
    entry43.grid(row=4, column=2)

    entry44 = Entry(table, width=25, justify="center")
    entry44.config(font=("Helvetica", 12, "bold"))
    entry44.insert(0, "-9.9")
    entry44.grid(row=4, column=3)

    entry45 = Entry(table, width=25, justify="center")
    entry45.config(font=("Helvetica", 12, "bold"))
    entry45.insert(0, "25.1")
    entry45.grid(row=4, column=4)

    enterButton = Button(table, text="Ввести", bg=BUTTONCOLOR, font=BUTTONFONT, command=enter, width=10, height=2)
    enterButton.grid(row=5, column=2, pady=15)


BG = "#787878"
FONT = ("Helvetica", 18, "bold")
BUTTONCOLOR = "#FFFF63"
BUTTONFONT = ("Helvetica", 20)

matrix = []

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
