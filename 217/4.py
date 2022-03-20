import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

v = np.loadtxt("LW217-4.txt")       # открыть файл с данными
x = [item[0] for item in v]			# первый столбец - y
y = [item[1] for item in v]			# второй стобец - x
R_teor = np.linspace(100, 2400, 4096)
y_teor = ((2*0.313)/(R_teor))

fig = plt.figure() 					# тело графика
plt.title (r'$τ_{уст}$')	    # название графика
plt.xlabel("R, Ом", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("τ, мс", fontsize=10, color='red') 		# ось ординат (y)
# plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(R_teor, y_teor*1000, label='Теоретический график')        # стандартный график (ломаная)

ax = fig.gca()          # возвращает текущую систему координат, not off

plt.scatter(x, y, s=22, c='red', marker="o", alpha = 1, label='Практические измерения')     # отображение точек
plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=0.1, yerr=0.1, fmt = ',')       # отобразить погрешности

#  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(500))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

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
