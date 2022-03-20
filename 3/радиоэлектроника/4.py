import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

x = np.linspace(1, 10, 10)
y = []
y_1 = [8, 10, 13, 14.5, 16.5, 18.5, 20, 21, 22, 23.6]
for i in y_1:
    i = i/2
    y.append(i)

p = np.polyfit(x, y, 1)				# создание полинома первой степени - апроксимация
ya = np.polyval(p, x)				# координаты y для полинома

fig = plt.figure() 					# тело графика
plt.title (r'Детекторная характеристика', fontsize = 15)	    # название графика
plt.xlabel(r'$U_{вх}$, мВ', fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r'$U_{вых}$, мВ', fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(x, ya, label='График апроксимации')        # график - апрокимация (прямая)

ax = fig.gca()          # возвращает текущую систему координат, not off

plt.scatter(x, y, s = 20, c = 'red', marker="o", alpha = 1, label = 'Практические измерения')     # отображение точек
plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=0.1, yerr=0.1, fmt = ',')       # отобразить погрешности

# #  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
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