import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

v = np.loadtxt("LW217-2.txt")       # открыть файл с данными
x = [item[0] for item in v]			# первый столбец - y
y = [item[1] for item in v]			# второй стобец - x
p = np.polyfit(x, y, 1)				# создание полинома первой степени - апроксимация
ya = np.polyval(p, x)				# координаты y для полинома

C = 6.8e-9
L = 0.313

x_teor = np.linspace(1, 2400, 2048)
# T_teor_tompson = 2*np.pi*(np.sqrt(L*C))
drob = ((1/(L*C))-((x_teor**2)/4*(L**2)))
print(drob)
T_teor = (2*np.pi)/(np.sqrt(drob))*(10**6)
fig = plt.figure() 					# тело графика
plt.title ("График периода от сопротивления")	    # название графика
plt.xlabel("R, Ом", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("T, мкс", fontsize=10, color='red') 		# ось ординат (y)
# plt.grid(True)                                # включение отображения стандартой сетки
# plt.plot(x_teor, T_teor_tompson, label='Теория')        # стандартный график (ломаная)
# plt.plot(x, ya, label='График апроксимации')        # график - апрокимация (прямая)

ax = fig.gca()          # возвращает текущую систему координат, not off
# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x, y, s=12, c='red', marker="o", alpha = 1, label='Практические измерения')     # отображение точек
plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, yerr=0.03, fmt = ',', color='red')

# #  Устанавливаем интервал основных и вспомогательных делений:
# ax.xaxis.set_major_locator(ticker.MultipleLocator(500))
# ax.xaxis.set_minor_locator(ticker.MultipleLocator(100))
# ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
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
