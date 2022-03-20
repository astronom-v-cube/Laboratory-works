import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

x = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 5.6, 5.8, 6, 6.2, 6.4, 6.6, 6.8, 7, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.2, 10.4, 10.6, 10.8]			# первый столбец - y
y = [0, -0.1, -0.4, -0.6, -0.6, -0.8, -0.9, -1.1, -1.3, -1.3, -1.4, -1.5, -1.6, -1.6, -1.6, -1.7, -1.7, -1.7, -1.7, -1.6, -1.6, -1.7, -1.6, -1.5, -1.4, -1.4, -1.3, -1.2, -1.1, -0.9, -0.8, -0.7, -0.5, -0.4, -0.1, 0.1, 0.3, 0.4, 0.7, 0.9, 1.1, 1.4, 1.6, 2, 2.2, 2.5, 2.9, 3.3, 3.6, 3.8, 4.3, 4.5, 4.9, 5.4, 5.8]			# второй стобец - x

y_appr = []

for i in x:
    temp = ((0.1397*i**2)-(0.9743*i)+0.0029)
    y_appr.append(temp)

fig = plt.figure() 					# тело графика
plt.title ("Зависимость паразитного напряжения от тока образца")	    # название графика
plt.xlabel(r"Ток образца, $mA$", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r"Паразитное напряжение, $mВ$", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(x, y_appr, label='График аппроксимации')        # стандартный график (ломаная)

ax = fig.gca()          # возвращает текущую систему координат, not off

# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x, y, s = 20, c='red', marker="o", alpha = 1, label='Практические значения')     # отображение точек
plt.legend()   			# Отобразить легенду - label
plt.errorbar(x, y, xerr=0.2, yerr=0.2, markersize=40, linestyle='none', ecolor='grey', elinewidth=0.8, capsize=3, capthick=1)       # отобразить погрешности

# #  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.2))

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
