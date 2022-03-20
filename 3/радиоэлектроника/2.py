import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

x = np.linspace(100, 1000, 10)
y = []
y_1 = [246, 236, 224, 214, 204, 196, 188, 180, 174, 168]
for i in y_1:
    i = i/2
    y.append(i)

p = np.polyfit(x, y, 1)				# создание полинома первой степени - апроксимация
ya = np.polyval(p, x)				# координаты y для полинома

fig = plt.figure() 					# тело графика
plt.title (r'Исследование нелинейности с резонансной нагрузкой', fontsize = 15)	    # название графика
plt.xlabel(r'$\nu$, кГц', fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r'$U_{вых}$, мВ', fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(x, ya, label='График апроксимации')        # график - апрокимация (прямая)

ax = fig.gca()          # возвращает текущую систему координат, not off

plt.scatter(x, y, s = 20, c = 'red', marker="o", alpha = 1, label = 'Практические измерения')     # отображение точек
plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=0.1, yerr=0.1, fmt = ',')       # отобразить погрешности

# #  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(100))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
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