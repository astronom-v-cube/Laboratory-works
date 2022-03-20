import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

R = 13e3
C = 0.05e-6
L = 0.25

v = np.loadtxt("LW210-10.txt")       # открыть файл с данными
nu = [item[0] for item in v]			# первый столбец - y
fi = [item[1] for item in v]			# второй стобец - x

fi = -np.array(fi)
freq = np.array(nu)
fi[4:] = -fi[4:]


freq_teor = np.linspace(0, freq[-1], 4096)
w = freq*2*np.pi
w_teor = freq_teor*2*np.pi


teor = - np.arctan2(((w_teor*R*C)*(5-(w_teor*R*C)**2)),(1-6*(w_teor*R*C)**2))

fig = plt.figure() 					# тело графика
plt.title ("Фазовая задержка схемы №6")	    # название графика
plt.xlabel("ν, кГц", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("ϕ, рад", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(freq_teor/1000, teor, label='Теоретический график')        # стандартный график (ломаная)

ax = fig.gca()          # возвращает текущую систему координат, not off
# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(freq/1000, fi, s=12, c='red', marker="o", alpha = 1, label='Результаты измерений')     # отображение точек
plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=1, yerr=0.3, color = 'snow', ecolor='purple')     # погрешности - функция в разработке :)

# #  Устанавливаем интервал основных и вспомогательных делений:
# ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
# ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.005))
#
# #  Добавляем линии основной сетки:
# ax.grid(which='major', color = 'k', linewidth = 1)
#
# #  Включаем видимость вспомогательных делений:
# ax.minorticks_on()
#
# #  Вид вспомогательной сетки:
# ax.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)

plt.show()


# https://pyprog.pro/mpl/mpl_short_guide.html
# https://devpractice.ru/matplotlib-lesson-1-quick-start-guide/
# https://python-scripts.com/matplotlib#1
# https://pyprog.pro/mpl/mpl_adding_a_line.html
