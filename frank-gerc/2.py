import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

x= [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]
y_1 = [0.01, 0.02, 0.03, 0.05, 0.075, 0.06, 0.16, 0.2, 0.25, 0.31, 0.41, 0.52, 0.6, 0.7, 0.81, 0.99]
y_2 = [0.01, 0.02, 0.04, 0.05, 0.08, 0.11, 0.16, 0.18, 0.24, 0.32, 0.4, 0.5, 0.59, 0.69, 0.79, 0.99]
y_3 = [0.01, 0.02, 0.03, 0.04, 0.06, 0.09, 0.14, 0.18, 0.24, 0.32, 0.4, 0.48, 0.55, 0.65, 0.78, 0.95]

fig = plt.figure() 					# тело графика
plt.title ("Анодно - сеточная характеристика")	    # название графика
plt.xlabel(r"Ускорющая разность потенциалов $\varphi_y, В$", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r"Анодный ток $I_a, mA$", fontsize=10, color='red') 		# ось ординат (y)

ax = fig.gca()          # возвращает текущую систему координат, not off

# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x, y_1, s = 30, c='red', marker="o", alpha = 0.8, label=r'Практические измерения при $\varphi_з$ = 40 В')     # отображение точек
plt.scatter(x, y_2, s = 30, c='green', marker="x", alpha = 0.8, label=r'Практические измерения при $\varphi_з$ = 45 В')     # отображение точек
plt.scatter(x, y_3, s = 30, c='blue', marker="D", alpha = 0.8, label=r'Практические измеренияпри $\varphi_з$ = 50 В')     # отображение точек
plt.legend()   			# Отобразить легенду - label
""" plt.errorbar(x, y, xerr=0.25, yerr=0.01, fmt = ',')       # отобразить погрешности """

line_1 = lambda x: 0.41 + (((x - 56)*(0.58))/5)
line_2 = lambda x: 0.4 + (((x - 56)*(0.55))/5)
line_3 = lambda x: 0.4 + (((x - 56)*(0.55))/5)

x_line = np.linspace(52, 61, 100)

plt.plot(x_line, line_1(x_line), linestyle='--', marker='', linewidth = 0.9)
plt.plot(x_line, line_2(x_line), linestyle='--', marker='', linewidth = 0.9)
plt.plot(x_line, line_3(x_line), linestyle='--', marker='', linewidth = 0.9)
#  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
#  Добавляем линии основной сетки:
ax.grid(which='major', color = 'k', linewidth = 0.8)

#  Включаем видимость вспомогательных делений:
ax.minorticks_on()

# #  Вид вспомогательной сетки:
ax.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)
#
plt.show()
