# -*- coding: utf-8 -*-
""" 
wsh_matplotlib_01.py
    
    'b'         blue
    'g'         green
    'r'         red
    'c'         cyan
    'm'         magenta
    'y'         yellow
    'k'         black
    'w'         white
    ``'-'``             solid line style
    ``'--'``            dashed line style
    ``'-.'``            dash-dot line style
    ``':'``             dotted line style
    ``'.'``             point marker
    ``','``             pixel marker
    ``'o'``             circle marker
    ``'v'``             triangle_down marker
    ``'^'``             triangle_up marker
    ``'<'``             triangle_left marker
    ``'>'``             triangle_right marker
    ``'1'``             tri_down marker
    ``'2'``             tri_up marker
    ``'3'``             tri_left marker
    ``'4'``             tri_right marker
    ``'s'``             square marker
    ``'p'``             pentagon marker
    ``'*'``             star marker
    ``'h'``             hexagon1 marker
    ``'H'``             hexagon2 marker
    ``'+'``             plus marker
    ``'x'``             x marker
    ``'D'``             diamond marker
    ``'d'``             thin_diamond marker
    ``'|'``             vline marker
    ``'_'``             hline marker
"""

import os
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import numpy.random as rnd # Генерация случайных чисел
os.chdir("d:/work.p/")

# Основы MATPLOTLIB
# Рассказать структуру рисунков - figure -> axes -> artists

# ********** Структура полотна (figure). Размещение рисунков (axes) *****
# ****************** Использованеи функции plot **************

# # Пустое полотно
# fig = plt.figure()  # an empty figure with no axes
# fig.suptitle('No axes on this figure')  # Add a title so we know which it is
# plt.show() # В spyder ничего не нарисуют, т.к. нет axes - 
# # полотен для рисования !!!

# # Размещение рисунков на сетке 
# fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# print(ax_lst.shape) # Массив адресов axes 
# fig.subplots_adjust(wspace=0.5, hspace=0.5) # Поля вокруг Axes
# # Подписи к Axes и к осям
# ax_lst[0, 0].set_title("Первый график")
# ax_lst[0, 0].set_xlabel("X")
# ax_lst[0, 0].set_ylabel("Y")
# plt.show() # Можно показать в spyder

# # Постепенное структурирование полотна
# x = np.linspace(0, 2*np.pi, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# fig = plt.figure()
# ax1 = fig.add_subplot(211)
# ax1.plot(x, y1, label = "sin")
# ax1.legend(loc = "best") #upper left, lower
# ax2 = fig.add_subplot(212)
# ax2.plot(x, y2, label = "cos")
# ax2.legend(loc = "best") #upper left, lower
# plt.show()

# # Нерегулярное размещение рисунков
# # Figure создается нами.
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
# t1 = np.arange(0.0, 3.0, 0.01)
# fig = plt.figure()
# # Сначала вводим две строки, один столбец. Размещвем во второй строке
# ax1 = fig.add_subplot(212)
# ax1.margins(0.05)           # Default margin is 0.05, value 0 means fit
# ax1.plot(t1, f(t1))
# # Тот же самый лист делим на 2х2 частей. Размещвем в первой строке
# # Если увеличить число строк, то может возникнуть наложение
# ax2 = fig.add_subplot(221)
# ax2.margins(2, 2)           # Values >0.0 zoom out
# ax2.plot(t1, f(t1))
# ax2.set_title('Zoomed out')
# ax3 = fig.add_subplot(222)
# ax3.margins(x=0, y=-0.25)   # Values in (-0.5, 0.0) zooms in to center
# ax3.plot(t1, f(t1))
# ax3.set_title('Zoomed in')
# plt.show()

# # Нерегулярное размещение рисунков
# # Figure создается в фоновом режиме.
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
# t1 = np.arange(0.0, 3.0, 0.01)
# # Сначала вводим две строки, один столбец. Размещвем во второй строке
# ax1 = plt.subplot(212)
# ax1.margins(0.05)           # Default margin is 0.05, value 0 means fit
# ax1.plot(t1, f(t1))
# # Далее вводим две строки, два столбца. Размещвем в первой строке
# ax2 = plt.subplot(221)
# ax2.margins(2, 2)           # Values >0.0 zoom out
# ax2.plot(t1, f(t1))
# ax2.set_title('Zoomed out')
# ax3 = plt.subplot(222)
# ax3.margins(x=0, y=-0.25)   # Values in (-0.5, 0.0) zooms in to center
# ax3.plot(t1, f(t1))
# ax3.set_title('Zoomed in')
# plt.show()

# # Использование gridspec для конфигурирования листа
# ax = np.empty([5,], 'O')
# # Смециальный менеджер масштабирует элементы рисунков, 
# # чтобы оформление осей и подписи не перекрывались.
# #fig3 = plt.figure(constrained_layout=True)
# fig3 = plt.figure(layout="constrained") 
# gs = fig3.add_gridspec(3, 3)
# #------------------------------------
# ax[0] = fig3.add_subplot(gs[0, :])
# ax[0].set_title('ax[0] -> gs[0, :]')
# #------------------------------------
# ax[1] = fig3.add_subplot(gs[1, :2])
# ax[1].set_title('ax[1] -> gs[1, :2]')
# #------------------------------------
# ax[2] = fig3.add_subplot(gs[1:, -1])
# ax[2].set_title('ax[2] -> gs[1:, -1]')
# #------------------------------------
# ax[3] = fig3.add_subplot(gs[-1, 0])
# ax[3].set_title('ax[3] -> gs[-1, 0]')
# #------------------------------------
# ax[4] = fig3.add_subplot(gs[-1, -2])
# ax[4].set_title('ax[4] -> gs[-1, -2]')
# plt.show()

## Печать документации к функции
# with open("./notes/plotdoc.txt", "w") as fln:
#     print(plt.plot.__doc__, file = fln)
# with open("./notes/legenddoc.txt", "w") as fln:
#     print(plt.legend.__doc__, file = fln)

# ***************** Определение свойств линий ******************
# # Первый вариант 2, 6 и т.д.
# #color, linewidth, linestyle
# x = np.linspace(-1, 1, 100) 
# y = 2*np.pi*x
# plt.plot(x, y, linewidth=1.0, color='g', linestyle='-.')

# # Второй вариант
# # '<color><marker><linestyle>'
# x = np.linspace(-1, 1, 100) 
# line, = plt.plot(x, 2*x, 'r+-')
# """
# Сглаживание используется для уменьшения 
# неровных краев и придания графику более плавного вида
# """
# line.set_antialiased(False)

# # Третий вариант
# x = np.linspace(-1, 1, 100)
# nu = 1/3
# omega = 2*np.pi*nu
# ysn = np.sin(omega*x)
# lines = plt.plot(x, ysn)
# # use keyword args
# # color = (r, g, b, alpha)
# plt.setp(lines, color='r', linewidth=2.0) # Для любого объекта
# print(plt.setp(lines)) # Все настройки
# *************** Печать документации ****************
# with open('./output/pltcontrol.txt', 'w') as f:
#     plt.setp(lines, file=f)
# plt.setp(lines, 'linestyle')
# # **************************************************

# # Столбчатая диаграмма
# # 1
# names = ['А', 'Б', 'В']
# values = [1, 30, 10]
# clr = ['r', 'g', 'b']
# plt.bar(names, values, color=clr)
# plt.show()

# # 2 Категоризированный график
# X = np.array([1,3,5])
# Offset = 0.4
# Y = [1,2,3]
# Z = [3,1,4]
# plt.bar(X - Offset, Y) # offset of -0.4
# plt.bar(X + Offset, Z) # offset of  0.4
# plt.show()

# # 3 Ручная простановка подписей
# X = ['A','B','C']
# Y = [1,2,3]
# Z = [3,1,4]
# _X = np.arange(len(X))
# Width = 0.4
# plt.bar(_X - 0.2, Y, Width)
# plt.bar(_X + 0.2, Z, Width)
# plt.xticks(_X, X) # set labels manually
# plt.legend(loc='best', labels=['D1', 'D2'])
# plt.show()

# # 4 Качественные данные
# n = 300
# p = [0.2, 0.5, 0.3]
# Z = rnd.choice(["a", "b", "c"], n, replace=True, p=p)
# U = np.unique(Z, return_counts=True)
# ax[1].bar(U[0], U[1])
# plt.show()

# # 5 Размещение нескольких графиков
# cm = 1/2.54 # Размер в см
# fig, ax = plt.subplots(2, 1, figsize=(5*cm, 10*cm))
# fig.subplots_adjust(wspace=0.5, hspace=0.5)
# names = ['А', 'Б', 'В']
# values = [1, 30, 10]
# #clr = ['r', 'g', 'b']
# clr = [(0.5,0,0), (0,1,0), (0,0,0.8)] 
# ax[0].bar(names, values, color=clr)

# # ........... Диаграмма рассеивания - scatterplot ............

# # 1
# c1 = (1,0,0)
# c2 = (0,1,0)
# c3 = (0,0,1)
# c4 = (0.5, 0.5, 0.5)
# c = [c1, c2, c3, c4]
# #c = [1, 2, 3, 4]
# d = [100, 200, 300, 400]
# x = np.arange(4.0)
# y = x**2
# plt.scatter(x, y, c=c, s=d)
# plt.show()

# # 2
# num = 50
# x = rnd.uniform(-1, 2, num)
# v = rnd.randn(num)
# y1 = 2.0 + 3.0*x + v
# y2 = 1.0 + 2.0*x + v
# cm = 'r'
# cf = 'b'
# plt.scatter(x, y1, c=cm, marker = '+', label='male')
# plt.scatter(x, y2, c=cf, label='female')
# plt.legend(loc='best')

# # 3 Выгрузка из БД
# num = 50
# gnd = rnd.choice(["m", "f"], num)
# x = rnd.uniform(-1, 2, num)
# v = rnd.randn(num)
# y = 2.0 + 3.0*x + v
# cm = 'r'
# cf = 'b'
# c = np.where(gnd == "m" ,cm, cf)
# plt.scatter(x, y, c=c)


# # Диаграмма Бокса-Уискера
# # 1
# num = 500
# y = rnd.randn(num)
# plt.boxplot(y, notch = True, showmeans=True, whis=1.5)
# plt.show()


# # 2 Категоризированный график. Выборки одного объема
# num = 1000
# y1 = rnd.uniform(-0.5, 1, num)
# # излишне y1.shape = (num, 1)
# y2 = rnd. uniform(-1, 0.5, num)
# # излишне y2.shape = (num, 1)
# y = np.c_[y1, y2] #  Собираем один массив из столбцов np.r_ - строки 
# # Вариант - y = np.hstack([y1, y2]) #  Собираем один массиы
# # boostrap = number - дов. интервал для медианы
# plt.boxplot(y, notch = True, showmeans=True, whis=1.5, labels=['A','B'])
# plt.show()

# # 3 Категоризированный график. Выборки разного объема
# num1 = 1000
# num2 = 900
# y1 = rnd.uniform(-0.5, 1, num1)
# y2 = rnd. uniform(-1, 0.5, num2)
# # boostrap = number - дов. интервал для медианы
# plt.boxplot([y1, y2], notch = True, showmeans=True, whis=1.5, labels=['A','B'])
# plt.show()

# # Гистограмма
# # 1 Выбор структуры категорий
# num = 500
# y = rnd.randn(num)
# # Запасной вариант - самим все рассчитывать.
# # bins = 1.44*np.log(num) # По Стерджесу
# # # По Фридману - Диаконису
# # Q75 = np.quantile(y, 0.75, axis=0, out=None, interpolation='linear') 
# # Q25 = np.quantile(y, 0.25, axis=0, out=None, interpolation='linear')
# # IQR = Q75 - Q25
# # h = 2*IQR/(np.power(num, 1/3))
# # Можно в bins указать количество категорий или список границ
# bins = ['sturges', 'fd', 'scott'] # Готовые стратегии 'fd' - Фридман-Диаконис
# for k in bins:
#  plt.hist(y, k, density=True, cumulative = False)
#  plt.grid(True)
#  plt.title('Histogram type: ' + k)
#  plt.show()

# # 2 Категоризированная гистограмма Выборки одного объема
# num = 1000
# y1 = rnd.uniform(-0.5, 1, num)
# y2 = rnd.randn(num)
# y = np.c_[y1, y2]
# # bins - кол или последовтельность концов полуоткрытых отрезков (кроме правого)
# plt.hist(y, 'fd', density=True, cumulative = False, color=['g','y'], 
#           label=['A', "B"]) # 50 bins, sum==1
# plt.xlabel('Значения')
# plt.ylabel('Вероятности')
# plt.title('Гистограмма значений')
# plt.grid(True)
# plt.legend(loc='best')
# plt.show()

# 3 Выборки разного объема
# y1 = rnd.uniform(-0.5, 1, 1000)
# y2 = rnd.randn(900)
# plt.hist([y1, y2], 50, density=True, cumulative = False, color=['g','y'], 
#           label=['A', "B"]) # 50 bins, sum==1
# plt.xlabel('Значения')
# plt.ylabel('Вероятности')
# plt.title('Гистограмма значений')
# plt.grid(True)
# plt.legend(loc='best')
# plt.show()

# # 4 Смесь распределений
# num = 1000
# m1 = 0
# s1 = 1
# m2 = 1.5
# s2 = 1
# y1 = s1*rnd.randn(num) + m1
# y2 = s2*rnd.randn(num) + m2
# sel = rnd.uniform(0, 1, num)
# y = np.where(sel < 0.7, y1, y2)
# plt.hist(y, 'fd', density=True)
# plt.show()