import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

x = [0, 154.6, 309.2, 463.8, 618.4, 773, 927.6, 1082.2, 1236.8, 1391.4, 1546, 1700.6, 1855.2, 2009.8, 2164.4, 2319, 2473.6]			# первый столбец - y
y_1_1 = [0.05, 1.05, 2.45, 3.35, 4.65, 5.55, 6.75, 8.25, 8.85, 10.35, 11.55, 12.45, 13.85, 14.95, 15.95, 17.35, 18.05]			# второй стобец - x
y_2_2 = [0.2, 2.3, 4.4, 6.9, 9.2, 11.4, 13.6, 16.1, 18, 20.2, 23.3, 24.8, 27.2, 29.6, 32.2, 34.4, 36.2]
y_4 = [-0.1, 4.2, 8.3, 12.2, 16.7, 21.1, 24.9, 29.2, 32.8, 37.2, 41.5, 45.8, 49.2, 54.4, 57.8, 61.7, 67.1]
y_7_5 = [0.15, 7.85, 15.35, 23.55, 31.15, 38.65, 46.95, 53.95, 61.65, 69.85, 77.65, 86.05, 93.65, 100.45, 110.25, 116.85, 126.15]


p = np.polyfit(x, y_1_1, 1)				# создание полинома первой степени - апроксимация
ya = np.polyval(p, x)				# координаты y для полинома

p = np.polyfit(x, y_2_2, 1)				# создание полинома первой степени - апроксимация
yb = np.polyval(p, x)				# координаты y для полинома

p = np.polyfit(x, y_4, 1)				# создание полинома первой степени - апроксимация
yc = np.polyval(p, x)				# координаты y для полинома

p = np.polyfit(x, y_7_5, 1)				# создание полинома первой степени - апроксимация
yd = np.polyval(p, x)				# координаты y для полинома

fig = plt.figure() 					# тело графика
plt.title ("Зависимость ЭДС Холла от магнитного поля")	    # название графика
plt.xlabel("Магнитное поле, Гс", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r"ЭДС Холла, $mВ$", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
# plt.plot(x, y, label='Название линии')        # стандартный график (ломаная)
plt.plot(x, ya, label='График аппроксимации для тока образца 1.1 В')        # график - апрокимация (прямая)
plt.plot(x, yb, label='График аппроксимации для тока образца 2.2 В')        # график - апрокимация (прямая)
plt.plot(x, yc, label='График аппроксимации для тока образца 4 В')        # график - апрокимация (прямая)
plt.plot(x, yd, label='График аппроксимации для тока образца 7.5 В')        # график - апрокимация (прямая)


ax = fig.gca()          # возвращает текущую систему координат, not off

# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x, y_1_1, s = 20, c='red', marker="o", alpha = 1, label='Практические значения для тока образца 1.1 В')     # отображение точек
plt.scatter(x, y_2_2, s = 20, c='green', marker="o", alpha = 1, label='Практические значения для тока образца 2.2 В')     # отображение точек
plt.scatter(x, y_4, s = 20, c='blue', marker="o", alpha = 1, label='Практические значения для тока образца 4 В')     # отображение точек
plt.scatter(x, y_7_5, s = 20, c='black', marker="o", alpha = 1, label='Практические значения для тока образца 7.5 В')     # отображение точек
plt.legend()   			# Отобразить легенду - label
plt.errorbar(x, y_1_1, xerr=0.2*773, yerr=0.2, markersize=40, linestyle='none', ecolor='grey', elinewidth=0.8, capsize=3, capthick=1)       # отобразить погрешности
plt.errorbar(x, y_2_2, xerr=0.2*773, yerr=0.2, markersize=40, linestyle='none', ecolor='grey', elinewidth=0.8, capsize=3, capthick=1)       # отобразить погрешности
plt.errorbar(x, y_4, xerr=0.2*773, yerr=0.2, markersize=40, linestyle='none', ecolor='grey', elinewidth=0.8, capsize=3, capthick=1)       # отобразить погрешности
plt.errorbar(x, y_7_5, xerr=0.2*773, yerr=0.2, markersize=40, linestyle='none', ecolor='grey', elinewidth=0.8, capsize=3, capthick=1)       # отобразить погрешности

# #  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(100))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

# #  Добавляем линии основной сетки:
ax.grid(which='major', color = 'k', linewidth = 1)

#  Включаем видимость вспомогательных делений:
ax.minorticks_on()
#
#  Вид вспомогательной сетки:
ax.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)
#
plt.show()


# https://pyprog.pro/mpl/mpl_short_guide.html
# https://devpractice.ru/matplotlib-lesson-1-quick-start-guide/
# https://python-scripts.com/matplotlib#1
# https://pyprog.pro/mpl/mpl_adding_a_line.html
