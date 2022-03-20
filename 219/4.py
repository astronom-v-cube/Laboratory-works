import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

v = np.loadtxt("LW219-4.txt")       # открыть файл с данными
y = [item[1] for item in v]			# первый столбец - y
x = [item[0] for item in v]			# второй стобец - x
# p = np.polyfit(x, y, 1)				# создание полинома первой степени - апроксимация
# ya = np.polyval(p, x)				# координаты y для полинома

fig = plt.figure() 					# тело графика
plt.title ("Амплитудно-частотная характеристика усилителя")	    # название графика
plt.xlabel("ν, Гц", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("К", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
# plt.plot(x, y, label='Название линии')        # стандартный график (ломаная)
# plt.plot(x, ya, label='Легенда графика')        # график - апрокимация (прямая)

ax = fig.gca()          # возвращает текущую систему координат, not off
ax.semilogx()
# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 13, 2))            # задание сетки по y (от, до, шаг)

plt.scatter(x, y, s=10, c='red', marker="o", alpha = 1)     # отображение точек
# plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=1, yerr=0.3, color = 'snow', ecolor='purple')     # погрешности - функция в разработке :)
#  Устанавливаем интервал основных и вспомогательных делений:
# ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
# ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
#
# #  Добавляем линии основной сетки:
ax.grid(which='major', color = 'k', linewidth = 1)
#
# #  Включаем видимость вспомогательных делений:
ax.minorticks_on()
#
# #  Вид вспомогательной сетки:
ax.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)

plt.show()


# https://pyprog.pro/mpl/mpl_short_guide.html
# https://devpractice.ru/matplotlib-lesson-1-quick-start-guide/
# https://python-scripts.com/matplotlib#1
