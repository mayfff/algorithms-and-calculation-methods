from tkinter import *
import pylab
import matplotlib.pyplot as plt
import numpy as np


class Interpolation:
    def __init__(self):
        self.frame = Frame(root, bg='green', bd=20)
        self.frame.pack()

        self.label_name = Label(self.frame, text='Інтерполяція функції', font=('Garamond', 20), fg='white', bg='green')
        self.label_name.grid(row=1, column=2)

        self.label_var = Label(self.frame, text='Варіант 28', font=('Garamond', 17), fg='white', bg='green')
        self.label_var.grid(row=2, column=1)

        self.label_func = Label(self.frame, text='cos(2x +x^2) на відрізку [0;1]', font=('Garamond', 17), fg='white',
                                bg='green')
        self.label_func.grid(row=2, column=3)

        self.eitken = Label(self.frame, text='Поліном Лагранжа', font=('Garamond', 20), fg='white', bg='green')
        self.eitken.grid(row=4, column=2, rowspan=2)

        self.but1 = Button(self.frame, text='Графік інтерполяції', font=('Garamond', 14), bg='SlateBlue2', width=18,
                           command=self.count_interpolation)
        self.but1.grid(row=4, column=1)

        self.but2 = Button(self.frame, text='Похибка інтерполяції', font=('Garamond', 14), bg='SlateBlue2', width=18,
                           command=self.count_divergence)
        self.but2.grid(row=5, column=1)

        self.but3 = Button(self.frame, text='Графік sin(x)', font=('Garamond', 14), bg='SlateBlue2', width=18,
                           command=self.count_sin)
        self.but3.grid(row=4, column=3)

        self.but3 = Button(self.frame, text='Похибка sin(x)', font=('Garamond', 14), bg='SlateBlue2', width=18,
                           command=self.count_div_sin)
        self.but3.grid(row=5, column=3)

        a, b = 0, 3
        h = (b - a) / 10
        self.xi = np.arange(0, 2.01, 0.01)
        self.yi = np.cos((2 * self.xi) + (self.xi ** 2))

    def lagrange(self, x_i, y):
        n = len(x_i)

        def p(x):
            polynomial = 0
            for j in range(n):

                def product(j, n):
                    total = 1
                    for i in range(n):
                        if i == j:
                            continue
                        xi = x_i[i]
                        xj = x_i[j]
                        total *= (x - xi) / (xj - xi)
                    return total

                polynomial += product(j, n) * y[j]
            return polynomial

        return p

    def count_interpolation(self):
        pol = self.lagrange(self.xi, self.yi)
        x_arg = np.arange(0, 2.01, 0.01)
        fig = plt.figure()
        plt.subplot(211)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Задана функція')
        plt.plot(self.xi, self.yi, label='Задана функція')
        plt.subplot(212)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Інтерполяція функції')
        plt.plot(x_arg, pol(x_arg), label='Поліном Лагранжа')

        fig.subplots_adjust(hspace=0.5)
        fig = pylab.gcf()
        plt.show()

    def count_divergence(self):
        def f(x):
            return np.cos(2 * x + x ** 2)

        pol = self.lagrange(self.xi, self.yi)
        x_arg = np.arange(0, 2.01, 0.01)
        y_arg = f(x_arg) - pol(x_arg)

        plt.subplot(211)
        plt.xlabel('x')
        plt.ylabel('R(x)')
        plt.title('Похибка')

        plt.plot(x_arg, y_arg)
        plt.show()

    def count_sin(self):
        def f(x):
            return np.sin(x)

        x = np.arange(0, 3, 0.01)
        pol = self.lagrange(x, f(x))
        x_arg = np.arange(0, 3, 0.01)

        fig = plt.figure()
        plt.subplot(211)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('sin(x)')
        plt.plot(x, f(x))
        plt.axis([0, 4, 0, 1])

        plt.subplot(212)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Інтерполяція')
        plt.plot(x_arg, pol(x_arg), color='green')
        plt.axis([0, 4, 0, 1])

        fig.subplots_adjust(hspace=0.5)
        fig = pylab.gcf()

        plt.show()

    def count_div_sin(self):
        def f(x):
            return np.sin(x)

        list_constants_sin = []
        xi = np.arange(0, 3.01, 0.1)
        a = len(xi) - 1
        y_sin = np.sin(xi)
        while a >= 0:
            constant = 0
            for i in range(len(xi) - a):
                znam = 1
                for j in range(len(xi) - a):
                    if i != j:
                        znam *= (xi[i] - xi[j])
                constant += y_sin[i] / znam
            list_constants_sin.append(constant)
            a -= 1

        x = np.arange(0, 3.01, 0.1)
        pol = self.lagrange(x, f(x))
        x_arg = np.arange(0, 3.01, 0.1)
        y_arg = f(list_constants_sin) - pol(x_arg)

        plt.subplot(211)
        plt.xlabel('x')
        plt.ylabel('R(x)')
        plt.title('Похибка sin(x)')

        plt.plot(x_arg, y_arg)
        plt.show()


root = Tk()
obj = Interpolation()
root.title('Lab3')
root.mainloop()