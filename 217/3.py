import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

R = 965
C = 6.8e-9
L = 0.313
e0 = 0.247

v = np.loadtxt("LW217-3.txt")       # открыть файл с данными
y = [item[0] for item in v]			# первый столбец - y
x1 = [item[1] for item in v]			# второй стобец - x
x2 = [item[2] for item in v]			# второй стобец - x
x3 = [item[3] for item in v]			# второй стобец - x

nu = np.linspace(200, 5000, 5120)
If = e0/(np.sqrt(R**2+(nu*2*np.pi*L-1/(nu*2*np.pi*C))**2))
Ulf = nu*2*np.pi*L*If
Ucf = 1/(nu*2*np.pi*C)*If
Urf = R*If


fig = plt.figure() 					# тело графика
plt.title ("Исследование вынужденных колебаний в электрическом контуре (R = 860 Ом)")	    # название графика
plt.xlabel("ν, Гц", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("U, В", fontsize=10, color='red') 		# ось ординат (y)
# plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(nu, Urf, c='red', label=r'Теоретический график $U_{R}$')        # стандартный график (ломаная)
plt.plot(nu, Ucf, c='green', label=r'Теоретический график $U_{С}$')        # стандартный график (ломаная)
plt.plot(nu, Ulf, c='blue', label=r'Теоретический график $U_{L}$')        # стандартный график (ломаная)

ax = fig.gca()          # возвращает текущую систему координат, not off
# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(y, x1, s=10, c='red', marker="o", alpha = 1, label=r'Практические значения $U_{R}$')     # отображение точек
plt.scatter(y, x2, s=10, c='green', marker="x", alpha = 1, label=r'Практические значения $U_{С}$')     # отображение точек
plt.scatter(y, x3, s=10, c='blue', marker="D", alpha = 1, label=r'Практические значения $U_{L}$')     # отображение точек

plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=1, yerr=0.3, color = 'snow', ecolor='purple')     # погрешности - функция в разработке :)

#  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(500))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(100))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))

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
