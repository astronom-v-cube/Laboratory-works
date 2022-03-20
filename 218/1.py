import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

v = np.loadtxt("LW218-1.txt")       # открыть файл с данными
x = [item[0] for item in v]			# первый столбец - y
y = [item[1] for item in v]			# второй стобец - x
z = [item[2] for item in v]			# второй стобец - x
p = np.polyfit(x, y, 1)				# создание полинома первой степени - апроксимация
pz = np.polyfit(x, z, 1)				# создание полинома первой степени - апроксимация
ya = np.polyval(p, x)				# координаты y для полинома
yz = np.polyval(pz, x)				# координаты y для полинома

fig = plt.figure() 					# тело графика
plt.title ("График погрешностей")	    # название графика
plt.xlabel("R₁", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("ΔC₂, мкФ", fontsize=10, color='red') 		# ось ординат (y)
# plt.grid(True)                                # включение отображения стандартой сетки
# plt.plot(x, y, label='Название линии')        # стандартный график (ломаная)
plt.plot(label='U = 15B')        # график - апрокимация (прямая)
plt.plot(label='U = 45B')        # график - апрокимация (прямая)

ax = fig.gca()          # возвращает текущую систему координат, not off
# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x, y, s=10, c='red', marker="o", alpha = 0.8, label='Результаты измерений с U = 15B')     # отображение точек
plt.scatter(x, z, s=10, c='green', marker="s", alpha = 0.8, label='Результаты измерений с U = 45B' )     # отображение точек
plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=1, yerr=0.3, color = 'snow', ecolor='purple')     # погрешности - функция в разработке :)

#  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(1000))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))

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
