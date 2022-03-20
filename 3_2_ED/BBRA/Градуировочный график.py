import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import math

x = np.linspace(9.3841, 13.2, 20)		# первый столбец - y
y = [4, 10, 20, 30, 40, 50, 60, 69, 77.5, 75, 80, 85, 90, 96, 100, 100, 101, 100, 100, 97.5]			# второй стобец - x
x_ = np.linspace(9.3841, 13.2, 2048)
y_ = -0.3553*x_**3 + 3.3525*x_**2 + 87.1978*x_ - 819.8908


fig = plt.figure() 					# тело графика
plt.title ("Градуировочный график")	    # название графика
plt.xlabel("z, см", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r"$I_g$, мкА", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(x_, y_, label='Аппроксимация кубической регрессией')        # стандартный график (ломаная)
ax = fig.gca()          # возвращает текущую систему координат, not off

# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x, y, s = 20, c='red', marker="o", alpha = 1, label='Практические измерения')     # отображение точек
plt.legend()   			# Отобразить легенду - label


# #  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.02))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(2))
#
# #  Добавляем линии основной сетки:
ax.grid(which='major', color = 'k', linewidth = 1)
#
#  Включаем видимость вспомогательных делений:
ax.minorticks_on()
#
#  Вид вспомогательной сетки:
ax.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)
#
plt.show()


# https://pyprog.pro/mpl/mpl_short_guide.html
# https://devpractice.ru/matplotlib-lesson-1-quick-start-guide/
# https://python-scripts.com/matplotlib#1
# https://pyprog.pro/mpl/mpl_adding_a_line.html
