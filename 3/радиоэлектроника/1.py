import matplotlib.pyplot as plt
import matplotlib
import matplotlib.ticker as ticker
import numpy as np

x = [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 411.1, 411.2, 411.3, 411.4, 411.5, 411.6, 411.7, 411.8, 411.9, 412, 412.1, 412.2, 412.3, 413, 414, 415, 416, 417, 418, 419, 420]
y = []
y_1 = [160, 168, 174, 180, 188, 196, 204, 214, 224, 236, 246, 256, 254, 254, 258, 258, 34, 36, 36, 34, 34, 34, 32, 30, 28, 256, 248, 238, 228, 220, 208, 200, 192]
for i in y_1:
    i = i/2
    y.append(i)

fig = plt.figure() 					# тело графика
plt.title (r'АЧХ схемы при нагрузке $R_n$', fontsize = 15)	    # название графика
plt.xlabel(r'$\nu$, кГц', fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r'$U_{вых}$, мВ', fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(x, y)        # стандартный график (ломаная)

ax = fig.gca()          # возвращает текущую систему координат, not off

plt.scatter(x, y, s = 20, c='red', marker="o", alpha = 1, label='Практические измерения')     # отображение точек
plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=0.1, yerr=0.1, fmt = ',')       # отобразить погрешности

# #  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(4))
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