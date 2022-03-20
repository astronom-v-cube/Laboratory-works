import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import math

v = np.loadtxt("LW200-1.txt")       # открыть файл с данными
y = [item[0] for item in v]			# первый столбец - y
x1 = [item[1] for item in v]			# второй стобец - x
x2 = [item[2] for item in v]			# второй стобец - x
x3 = [item[3] for item in v]			# второй стобец - x

w = np.linspace(1000, 5000, 4096)
R = 500
C = 6.8e-9
L = 0.72
e0 = 0.247
w_teor = w*2*np.pi
# If = lambda w_teor,L,R,C,e0: e0/(np.sqrt(R**2+(w_teor*L-1/(w_teor*C))**2))
# Ulf = lambda w_teor,L,R,C,e0: w_teor*L*If(w_teor,L,R,C,e0)
# Ucf = lambda w_teor,L,R,C,e0: 1/(w_teor*C)*If(w_teor,L,R,C,e0)
# Urf = lambda w_teor,L,R,C,e0: R*If(w_teor,L,R,C,e0)
If = e0/(np.sqrt(R**2+(w_teor*L-1/(w_teor*C))**2))
Ulf = w_teor*L*If
Ucf = 1/(w_teor*C)*If
Urf = R*If

# U_C_teory = ((e0)/(np.sqrt(R**2 + (w_teor * L - (1 / w_teor * C))**2)))
# U_R_teory = ((e0 * R)/(np.sqrt(R**2 + (w_teor * L - (1 / w_teor * C))**2)))
fig = plt.figure() 					# тело графика
plt.title ("Название графика")	    # название графика
plt.xlabel("Ось X", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("Ось Y", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
# plt.plot(x, y, label='Название линии')        # стандартный график (ломаная)
# plt.plot(x, ya, label='Легенда графика')        # график - апрокимация (прямая)

ax = fig.gca()          # возвращает текущую систему координат, not off
# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)
plt.plot(-w, Ulf, label='Теоретический график')        # стандартный график (ломаная)
plt.plot(-w, Urf, label='Теоретический график')        # стандартный график (ломаная)
plt.plot(-w, Ucf, label='Теоретический график')        # стандартный график (ломаная)

plt.scatter(y, x1, s=7, c='red', marker="o", alpha = 1, label=r'$U_{R}$')     # отображение точек
plt.scatter(y, x2, s=7, c='green', marker="x", alpha = 1, label=r'$U_{C}$')     # отображение точек
plt.scatter(y, x3, s=7, c='blue', marker="D", alpha = 1, label=r'$U_{L}$')     # отображение точек

plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=1, yerr=0.3, color = 'snow', ecolor='purple')     # погрешности - функция в разработке :)

# #  Устанавливаем интервал основных и вспомогательных делений:
# ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
# ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
# ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
#
# #  Добавляем линии основной сетки:
# ax.grid(which='major', color = 'k', linewidth = 1)
#
# #  Включаем видимость вспомогательных делений:
# ax.minorticks_on()
#
# #  Вид вспомогательной сетки:
# ax.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)

plt.show()


# https://pyprog.pro/mpl/mpl_short_guide.html
# https://devpractice.ru/matplotlib-lesson-1-quick-start-guide/
# https://python-scripts.com/matplotlib#1
# https://pyprog.pro/mpl/mpl_adding_a_line.html
