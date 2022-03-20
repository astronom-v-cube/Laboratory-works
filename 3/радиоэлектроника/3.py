import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def popolam(y, y_):
    for i in y:
        i = i/2
        y_.append(i)

x1 = [244, 246, 250, 252, 254, 260]
x2 = [153, 156, 159, 160, 162]
x3 = [569, 571, 572, 574, 575, 579]
y1 = []
y2 = []
y3 = []

popolam([40, 48, 100, 156, 92, 40], y1)
popolam([82, 138, 342, 428, 246], y2) 
popolam([100, 194, 222, 118, 90, 50], y3)

fig = plt.figure() 					# тело графика
plt.title (r'Исследование нелинейности с резонансной нагрузкой', fontsize = 15)	    # название графика
plt.xlabel(r'$\nu$, кГц', fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r'$U_{вых}$, мВ', fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки

ax = fig.gca()          # возвращает текущую систему координат, not off

plt.scatter(x1, y1, s = 20, c = 'red', marker="o", alpha = 1, label = 'Практические измерения')     # отображение точек
plt.scatter(x2, y2, s = 20, c = 'red', marker="o", alpha = 1)     # отображение точек
plt.scatter(x3, y3, s = 20, c = 'red', marker="o", alpha = 1)     # отображение точек
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=0.1, yerr=0.1, fmt = ',')       # отобразить погрешности

# #  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_locator(ticker.MultipleLocator(25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
#
# #  Добавляем линии основной сетки:
ax.grid(which='major', color = 'k', linewidth = 1)
#
# #  Включаем видимость вспомогательных делений:
ax.minorticks_on()
#
# #  Вид вспомогательной сетки:
ax.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)
#
plt.show()