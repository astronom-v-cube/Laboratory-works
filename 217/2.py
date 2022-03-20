import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
pi = np.pi
sqrt = np.sqrt

v = np.loadtxt("LW217-2.txt")       # открыть файл с данными
x = [item[0] for item in v]			# первый столбец - y
y = [item[1] for item in v]			# второй стобец - x
# a1a5 = [item[2] for item in v]			# второй стобец - x
# pogr_proc = [item[3] for item in v]			# второй стобец - x

p = np.polyfit(x, y, 1)				# создание полинома первой степени - апроксимация
ya = np.polyval(p, x)				# координаты y для полинома

R_teor = np.linspace(0, 2400, 3072)
C = 6.8e-9
L = 0.31
d = (pi*(R_teor)*(sqrt(C/L)))

fig = plt.figure() 					# тело графика
plt.title ("График декремента от сопротивления")	    # название графика
plt.xlabel("R, Ом", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("d", fontsize=10, color='red') 		# ось ординат (y)
# plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(R_teor, d, label='Теоретический график')        # стандартный график (ломаная)
plt.plot(x, ya, label='График апроксимации')        # график - апрокимация (прямая)

ax = fig.gca()          # возвращает текущую систему координат, not off
# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x, y, s=12, c='red', marker="o", alpha = 1, label='Практические измерения по стандартой формуле')     # отображение точек
# plt.scatter(x, a1a5, s=12, c='green', marker="x", alpha = 1, label='Практические измерения по формуле для A1 и А5')     # отображение точек

plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, a1a5, xerr=0, yerr=pogr_proc, fmt = ',', capsize=2)

#  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(100))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))

#  Добавляем линии основной сетки:
ax.grid(which='major', color = 'k', linewidth = 1)

#  Включаем видимость вспомогательных делений:
ax.minorticks_on()

#  Вид вспомогательной сетки:
ax.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)

plt.show()


# https://pyprog.pro/mpl/mpl_short_guide.html
# https://devpractice.ru/matplotlib-lesson-1-quick-start-guide/
# https://python-scripts.com/matplotlib#1
# https://pyprog.pro/mpl/mpl_adding_a_line.html
