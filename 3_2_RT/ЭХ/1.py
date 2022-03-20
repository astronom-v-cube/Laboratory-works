import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

x_ = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29, 29.5, 30]			# первый столбец - y
y = [0, 0.2, 0.3, 0.5, 0.7, 0.8, 1, 1.1, 1.3, 1.5, 1.7, 1.8, 2.1, 2.2, 2.3, 2.5, 2.7, 2.8, 3.1, 3.2, 3.2, 3.5, 3.6, 3.9, 4, 4.1, 4.3, 4.4, 4.7, 4.7, 5, 5.3, 5.4, 5.5, 5.8, 5.7, 5.9, 6, 6.5, 6.7, 6.7, 7, 7.2, 7.2, 7.2, 7.7, 7.8, 7.9, 8.1, 8.4, 8.3, 8.6, 8.8, 9, 9, 9.3, 9.5, 9.6, 9.8, 9.7, 10.2]			# второй стобец - x
x = []
for i in y:
    x.append(i/1000*1570)

p = np.polyfit(x_, y, 1)				# создание полинома первой степени - апроксимация
ya = np.polyval(p, x_)				# координаты y для полинома

fig = plt.figure() 					# тело графика
plt.title ("Вольт-амперная характеристика образца")	    # название графика
plt.xlabel("Напряжение, В", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r"Сила тока, $mA$", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
# plt.plot(x, y, label='Название линии')        # стандартный график (ломаная)
plt.plot(x_, ya, label='График аппроксимации')        # график - апрокимация (прямая)

ax = fig.gca()          # возвращает текущую систему координат, not off

# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x_, y, s = 20, c='red', marker="o", alpha = 1, label='Практические значения')     # отображение точек
plt.legend()   			# Отобразить легенду - label
plt.errorbar(x_, y, xerr=0.2, yerr=0.2, markersize=40, linestyle='none', ecolor='grey', elinewidth=0.8, capsize=3, capthick=1)       # отобразить погрешности

# #  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

# #  Добавляем линии основной сетки:
ax.grid(which='major', color = 'k', linewidth = 1)

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
