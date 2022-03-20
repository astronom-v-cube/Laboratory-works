import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

v = np.loadtxt("xxx.txt")       # открыть файл с данными
x = [item[0] for item in v]			# первый столбец - y
y = [item[1] for item in v]			# второй стобец - x

p = np.polyfit(x, y, 1)				# создание полинома первой степени - апроксимация
ya = np.polyval(p, x)				# координаты y для полинома

fig = plt.figure() 					# тело графика
plt.title ("Название графика")	    # название графика
plt.xlabel("Ось X", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("Ось Y", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(x, y, label='Название линии')        # стандартный график (ломаная)
plt.plot(x, ya, label='Легенда графика')        # график - апрокимация (прямая)

ax = fig.gca()          # возвращает текущую систему координат, not off

# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x, y, s = 10, c='red', marker="o", alpha = 1, label='Легенда точек')     # отображение точек
plt.legend()   			# Отобразить легенду - label
plt.errorbar(x, y, xerr=0.1, yerr=0.1, fmt = ',')       # отобразить погрешности

# #  Устанавливаем интервал основных и вспомогательных делений:
# ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
# ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
# ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
#
# #  Добавляем линии основной сетки:
# ax.grid(which='major', color = 'k', linewidth = 1)
#
# #  Включаем видимость вспомогательных делений:
# ax.minorticks_on()
#
# #  Вид вспомогательной сетки:
# ax.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)
#
# plt.show()


# https://pyprog.pro/mpl/mpl_short_guide.html
# https://devpractice.ru/matplotlib-lesson-1-quick-start-guide/
# https://python-scripts.com/matplotlib#1
# https://pyprog.pro/mpl/mpl_adding_a_line.html
