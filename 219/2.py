import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

v = np.loadtxt("LW219-3.txt")       # открыть файл с данными
y1 = [item[0] for item in v]			# первый столбец - y
y2 = [item[1] for item in v]			# первый столбец - y
y3 = [item[2] for item in v]			# первый столбец - y
y4 = [item[3] for item in v]			# первый столбец - y
# x = [item[0] for item in v]			# второй стобец - x

y1 = y1[9:]
y2 = y2[6:]
y3 = y3[4:]
y4 = y4[1:-5]

x1 = []
for i in np.arange(-2.5,5.5,0.5):
    x1.append(i)

x2 = []
for i1 in np.arange(-4,5.5,0.5):
    x2.append(i1)

x3 = []
for i2 in np.arange(-5,5.5,0.5):
    x3.append(i2)

x4 = []
for i3 in np.arange(-6.5,3,0.5):
    x4.append(i3)
print(x1, x2, x3, x4)
# p = np.polyfit(x, y, 1)				# создание полинома первой степени - апроксимация
# ya = np.polyval(p, x)				# координаты y для полинома

fig = plt.figure() 					# тело графика
plt.title ("Статическая анодно-сеточная характеристика триода")	    # название графика
plt.xlabel("Uα, В", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("Iα, mA", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
# plt.plot(x, y, label='Название линии')        # стандартный график (ломаная)
# plt.plot(x, ya, label='Легенда графика')        # график - апрокимация (прямая)

ax = fig.gca()          # возвращает текущую систему координат, not off
# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x1, y1, s=7, c='red', marker="o", alpha = 1, label='Iα при Uα = 60 В')     # отображение точек
plt.scatter(x2, y2, s=7, c='green', marker="D", alpha = 1, label='Iα при Uα = 80 В')     # отображение точек
plt.scatter(x3, y3, s=7, c='blue', marker="^", alpha = 1, label='Iα при Uα = 100 В')     # отображение точек
plt.scatter(x4, y4, s=7, c='black', marker="x", alpha = 1, label='Iα при Uα = 120 В')     # отображение точек

plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=1, yerr=0.3, color = 'snow', ecolor='purple')     # погрешности - функция в разработке :)

# Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

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
