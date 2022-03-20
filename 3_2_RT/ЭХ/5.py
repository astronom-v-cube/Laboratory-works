import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5]			# первый столбец - y
y_1_1 = [0.2, 1.6, 3, 4.65, 6.3, 7.9, 9.6, 10.9, 12.6, 14.05, 15.4, 17.25, 19.4, 19.95, 22.1, 23.25, 24.6, 26.2, 27.7, 29.15, 31.3, 32.55]			# второй стобец - x
y_2_2 = [-0.1, 2.5, 5.4, 8.05, 10.4, 12.8, 15.6, 18.5, 20.4, 23.05, 26.5, 28.45, 31.3, 34.15, 36.4, 38.85, 41.7, 44.8, 47.5, 48.95, 51.5, 54.65]
y_4 = [0.2, 4.9, 9.5, 14.25, 18.5, 23.7, 28.2, 33, 37.6, 42.65, 47.1, 51.35, 56.2, 60.65, 65.3, 70.35, 75.5, 80.5, 85.3, 88.85, 93.9, 97.15]
y_7_5 = [0.1, 6.4, 13.1, 19.45, 25.7, 32.3, 38.8, 44.9, 51.3, 58.45, 65.1, 71.35, 78.5, 84.75, 90.4, 98.55, 104.3, 110.5, 116, 123.25, 129.7, 136.45]


p = np.polyfit(x, y_1_1, 1)				# создание полинома первой степени - апроксимация
ya = np.polyval(p, x)				# координаты y для полинома

p = np.polyfit(x, y_2_2, 1)				# создание полинома первой степени - апроксимация
yb = np.polyval(p, x)				# координаты y для полинома

p = np.polyfit(x, y_4, 1)				# создание полинома первой степени - апроксимация
yc = np.polyval(p, x)				# координаты y для полинома

p = np.polyfit(x, y_7_5, 1)				# создание полинома первой степени - апроксимация
yd = np.polyval(p, x)				# координаты y для полинома

fig = plt.figure() 					# тело графика
plt.title ("Зависимость ЭДС Холла от тока образца")	    # название графика
plt.xlabel(r"Ток образца, $mA$", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r"ЭДС Холла, $mВ$", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
# plt.plot(x, y, label='Название линии')        # стандартный график (ломаная)
plt.plot(x, ya, label='График аппроксимации для магнитного поля 463,8 Гс')        # график - апрокимация (прямая)
plt.plot(x, yb, label='График аппроксимации для магнитного поля 733 Гс')        # график - апрокимация (прямая)
plt.plot(x, yc, label='График аппроксимации для магнитного поля 1394,4 Гс')        # график - апрокимация (прямая)
plt.plot(x, yd, label='График аппроксимации для магнитного поля 1932,5 Гс')        # график - апрокимация (прямая)


ax = fig.gca()          # возвращает текущую систему координат, not off

# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x, y_1_1, s = 20, c='red', marker="o", alpha = 1, label='Практические значения для магнитного поля 463,8 Гс')     # отображение точек
plt.scatter(x, y_2_2, s = 20, c='green', marker="o", alpha = 1, label='Практические значения для магнитного поля 733 Гс')     # отображение точек
plt.scatter(x, y_4, s = 20, c='blue', marker="o", alpha = 1, label='Практические значения для магнитного поля 1394,4 Гс')     # отображение точек
plt.scatter(x, y_7_5, s = 20, c='black', marker="o", alpha = 1, label='Практические значения для магнитного поля 1932,5 Гс')     # отображение точек
plt.legend()   			# Отобразить легенду - label
plt.errorbar(x, y_1_1, xerr=0.2, yerr=0.2, markersize=40, linestyle='none', ecolor='grey', elinewidth=0.8, capsize=3, capthick=1)       # отобразить погрешности
plt.errorbar(x, y_2_2, xerr=0.2, yerr=0.2, markersize=40, linestyle='none', ecolor='grey', elinewidth=0.8, capsize=3, capthick=1)       # отобразить погрешности
plt.errorbar(x, y_4, xerr=0.2, yerr=0.2, markersize=40, linestyle='none', ecolor='grey', elinewidth=0.8, capsize=3, capthick=1)       # отобразить погрешности
plt.errorbar(x, y_7_5, xerr=0.2, yerr=0.2, markersize=40, linestyle='none', ecolor='grey', elinewidth=0.8, capsize=3, capthick=1)       # отобразить погрешности

# #  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
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
