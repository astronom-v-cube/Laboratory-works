import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

x = [85, 70, 65, 57, 55, 50, 49, 48]			# первый столбец - y
y1 = [100, 95, 92, 80, 70, 60, 50, 0]			# второй стобец - x
y = []
for i in y1:
    y.append(i/2)
    
fig = plt.figure() 					# тело графика
plt.title ("Бифуркационная диаграмма для жесткого режима генератора")	    # название графика
plt.xlabel(r"М, град", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r"U, В", fontsize=10, color='red') 		# ось ординат (y)
# plt.grid(True)                                # включение отображения стандартой сетки

ax = fig.gca()          # возвращает текущую систему координат, not off

# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)
x2 = [50, 57, 65]
y2 = [13.85, 9.3, 0]
plt.scatter(x, y, s = 45, c='red', marker="o", alpha = 1, label='Устойчивые состояния')     # отображение точек
plt.scatter(x2, y2, s = 45, c='red', marker="x", alpha = 1, label='Неустойчивые состояния')     # отображение точек
xx1 = [49, 49]
yy1 = [0, 24]
ax.arrow(49, 24, 0, -24, width = 0.15)    #  ширина стрелки
ax.arrow(65, 2, 0, 42, width = 0.15)    #  ширина стрелки

plt.legend()   			# Отобразить легенду - label

#  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
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
# https://pyprog.pro/mpl/mpl_adding_a_line.html
