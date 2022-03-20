import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

x = np.linspace(1, 15, 15)
y = []
y_1 = [568, 560, 552, 536, 512, 480, 456, 448, 424, 408, 376, 360, 344, 328, 312]
for i in y_1:
    i = i/2
    y.append(i)
y_2 = np.linspace(468, 468, 15)

fig = plt.figure() 					# тело графика
plt.title (r'Зависимость выходного напряжения от частоты модуляции', fontsize = 15)	    # название графика
plt.xlabel(r'$f_{mod}$, кГц', fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r'$U_{вых}$, мВ', fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки

ax = fig.gca()          # возвращает текущую систему координат, not off
plt.plot(x, y_2, label=r'$R_1 = 20 кОм, C_1 = 100 пФ$')
plt.plot(x, y, label=r'$R_1 = 200 кОм, C_1 = 1000 пФ$')
plt.scatter(x, y_2, s = 20, c = 'red', marker="o", alpha = 1, label = r'Практические измерения при $\tau$ = $R_{1}C_{1}$')     # отображение точек
plt.scatter(x, y, s = 20, c = 'red', marker="x", alpha = 1, label = r'Практические измерения$\tau$ = $R_{2}C_{2}$')     # отображение точек
plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=0.1, yerr=0.1, fmt = ',')       # отобразить погрешности

# #  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
#
# #  Добавляем линии основной сетки:
ax.grid(which='major', color = 'k', linewidth = 1)
#
# #  Включаем видимость вспомогательных делений:
ax.minorticks_on()
#
# #  Вид вспомогательной сетки:
ax.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)
#
plt.show()