import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

v = np.loadtxt("LW204-2.txt")       # открыть файл с данными
x1 = [item[0] for item in v]			# первый столбец - y
y1 = [item[1] for item in v]			# второй стобец - x
y3 = [item[3] for item in v]			# второй стобец - x
y5 = [item[5] for item in v]			# второй стобец - x
p1 = np.polyfit(x1, y1, 1)				# создание полинома первой степени - апроксимация
p2 = np.polyfit(x1, y3, 1)				# создание полинома первой степени - апроксимация
p3 = np.polyfit(x1, y5, 1)				# создание полинома первой степени - апроксимация

ya = np.polyval(p1, x1)				# координаты y для полинома
yb = np.polyval(p2, x1)				# координаты y для полинома
yc = np.polyval(p3, x1)				# координаты y для полинома


fig = plt.figure() 					# тело графика
plt.title ("U(B) при J = const")	    # название графика
plt.xlabel("B, Гс", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("U, B", fontsize=10, color='red') 		# ось ординат (y)
# plt.grid(True)                                # включение отображения стандартой сетки
# plt.plot(x, y, label='Название линии')        # стандартный график (ломаная)
# plt.plot(x, ya, label='Легенда графика')        # график - апрокимация (прямая)

ax = fig.gca()          # возвращает текущую систему координат, not off
# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x1, y1, s=7, c='blue', marker="D", alpha = 1, label='Результаты измерений при J = +2 мА')     # отображение точек
plt.scatter(x1, y3, s=7, c='orange', marker="v", alpha = 1, label='Результаты измерений при J = +5 мА')     # отображение точек
plt.scatter(x1, y5, s=7, c='green', marker="o", alpha = 1, label='Результаты измерений при J = +8 мА')     # отображение точек
  			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=1, yerr=0.3, color = 'snow', ecolor='purple')     # погрешности - функция в разработке :)
plt.plot(x1, ya, label='График апрокимации при J = +2 мА')        # график - апрокимация (прямая)
plt.plot(x1, yb, label='График апрокимации при J = +5 мА')        # график - апрокимация (прямая)
plt.plot(x1, yc, label='График апрокимации при J = +8 мА')        # график - апрокимация (прямая)
plt.legend()

 # Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(250))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.01))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.001))

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
