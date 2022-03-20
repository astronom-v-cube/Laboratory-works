import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

v = np.loadtxt("LW204-3.txt")       # открыть файл с данными
x2 = [item[0] for item in v]			# первый столбец - y
x1 = [item[1] for item in v]			# первый столбец - y
y1 = [item[2] for item in v]			# второй стобец - x
y2 = [item[3] for item in v]			# второй стобец - x
y3 = [item[6] for item in v]			# второй стобец - x
y4 = [item[7] for item in v]			# второй стобец - x
y5 = [item[10] for item in v]			# второй стобец - x
y6 = [item[11] for item in v]        	# второй стобец - x
y7 = [item[14] for item in v]			# второй стобец - x
y8 = [item[15] for item in v]			# второй стобец - x


p1 = np.polyfit(x2, y1, 1)				# создание полинома первой степени - апроксимация
p2 = np.polyfit(x1, y2, 1)				# создание полинома первой степени - апроксимация
p3 = np.polyfit(x1, y3, 1)				# создание полинома первой степени - апроксимация
p4 = np.polyfit(x2, y4, 1)				# создание полинома первой степени - апроксимация
p5 = np.polyfit(x1, y5, 1)				# создание полинома первой степени - апроксимация
p6 = np.polyfit(x2, y6, 1)				# создание полинома первой степени - апроксимация
p7 = np.polyfit(x1, y7, 1)				# создание полинома первой степени - апроксимация
p8 = np.polyfit(x2, y8, 1)				# создание полинома первой степени - апроксимация


ya = np.polyval(p1, x2)				# координаты y для полинома
yb = np.polyval(p2, x1)				# координаты y для полинома
yc = np.polyval(p3, x1)				# координаты y для полинома
yd = np.polyval(p4, x2)				# координаты y для полинома
ye = np.polyval(p5, x1)				# координаты y для полинома
yf = np.polyval(p6, x2)				# координаты y для полинома
yg = np.polyval(p7, x1)				# координаты y для полинома
yh = np.polyval(p8, x2)				# координаты y для полинома

fig = plt.figure() 					# тело графика
plt.title ("U (J) при B = const и B = 0")	    # название графика
plt.xlabel("J (mA)", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("U (V)", fontsize=10, color='red') 		# ось ординат (y)
# plt.grid(True)                                # включение отображения стандартой сетки

plt.plot(x2, ya, label='U при В = 0 и J +', linestyle = "--")        # график - апрокимация (прямая)
plt.plot(x1, yb, label='U при В = 0 и J -', linestyle = "--")        # график - апрокимация (прямая)
plt.plot(x1, yc, label='U при В = +650 и J -')        # график - апрокимация (прямая)
plt.plot(x2, yd, label='U при В = +650 и J +')        # график - апрокимация (прямая)
plt.plot(x1, ye, label='U при В = +1500 и J -')        # график - апрокимация (прямая)
plt.plot(x2, yf, label='U при В = +1500 и J +')        # график - апрокимация (прямая)
plt.plot(x1, yg, label='U при В = +2400 и J -')        # график - апрокимация (прямая)
plt.plot(x2, yh, label='U при В = +2400 и J +')        # график - апрокимация (прямая)


ax = fig.gca()          # возвращает текущую систему координат, not off
# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x2, y1, s=12, c='red', marker="s", alpha = 1)     # отображение точек
plt.scatter(x1, y2, s=12, c='red', marker="s", alpha = 1)     # отображение точек
plt.scatter(x1, y3, s=12, c='red', marker="D", alpha = 1)     # отображение точек
plt.scatter(x2, y4, s=12, c='red', marker="D", alpha = 1)     # отображение точек
plt.scatter(x1, y5, s=12, c='red', marker="x", alpha = 1)     # отображение точек
plt.scatter(x2, y6, s=12, c='red', marker="x", alpha = 1)     # отображение точек
plt.scatter(x1, y7, s=12, c='red', marker="^", alpha = 1)     # отображение точек
plt.scatter(x2, y8, s=12, c='red', marker="^", alpha = 1)     # отображение точек

plt.legend(fontsize = 10, ncol = 2)  			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=1, yerr=0.3, color = 'snow', ecolor='purple')     # погрешности - функция в разработке :)

# Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.02))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.005))

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
