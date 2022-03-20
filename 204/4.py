import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

v = np.loadtxt("LW204-1.txt")       # открыть файл с данными
x1 = [item[0] for item in v]			# первый столбец - y
x2 = [item[3] for item in v]			# первый столбец - y
y = [item[1] for item in v]			# второй стобец - x
z = [item[2] for item in v]			# третий стобец - z
p1 = np.polyfit(x1, y, 1)				# создание полинома первой степени - апроксимация
p2 = np.polyfit(x2, z, 1)				# создание полинома первой степени - апроксимация
y1 = np.polyval(p1, x1)				# координаты y для полинома
y2 = np.polyval(p2, x2)				# координаты y для полинома

fig = plt.figure() 					# тело графика
plt.title ("U (J)")	    # название графика
plt.xlabel("J, mA", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("U, B", fontsize=10, color='red') 		# ось ординат (y)
# plt.grid(True)                                # включение отображения стандартой сетки
# plt.plot(x, y, label='Название линии')        # стандартный график (ломаная)
plt.plot(x1, y1, label='Апроксимация результатов при J = +')        # график - апрокимация (прямая)
plt.plot(x2, y2, label='Апроксимация результатов при J = -')        # график - апрокимация (прямая)

ax = fig.gca()          # возвращает текущую систему координат, not off
# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x1, y, s=14, c='red', marker="o", alpha = 1, label='Результаты измерений при J = +')     # отображение точек
plt.scatter(x2, z, s=14, c='green', marker="x", alpha = 1, label='Результаты измерений J = -')     # отображение точек
plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=1, yerr=0.3, color = 'snow', ecolor='purple')     # погрешности - функция в разработке :)

#  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
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
