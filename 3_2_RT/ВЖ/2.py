import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]		# первый столбец - y
y_ = [255, 210, 183, 170, 150, 141, 138, 127, 125, 121, 107, 106, 108, 100, 102, 91, 91, 88, 93, 86, 90, 80, 84, 85, 86, 73, 74, 72, 74]			# второй стобец - x

y = []
for i in y_:
    y.append(np.log(i))

p = np.polyfit(x, y, 1)				# создание полинома первой степени - апроксимация
ya = np.polyval(p, x)				# координаты y для полинома

fig = plt.figure() 					# тело графика
plt.title ("Время жизни неосновных носителей тока")	    # название графика
plt.xlabel(r"$t$, мкс", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r"$ln(\Delta U_2)$", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(x, ya, label='Линейная аппроксимация')        # график - апрокимация (прямая)

ax = fig.gca()          # возвращает текущую систему координат, not off

# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x, y, s = 10, c='red', marker="o", alpha = 1, label='Практические измерения')     # отображение точек
plt.legend()   			# Отобразить легенду - label
plt.errorbar(x, y, xerr=0.1, yerr=0.3, markersize=40, linestyle='none', ecolor='grey', elinewidth=0.8, capsize=3, capthick=1)       # отобразить погрешности

# #  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
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
