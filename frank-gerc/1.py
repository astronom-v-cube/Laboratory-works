import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

x = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]

y = [0, 0, 0, 0.02, 0.1, 0.19, 0.27, 0.33, 0.38, 0.43, 0.45, 0.46, 0.47, 0.49, 0.5, 0.505, 0.505, 0.505, 0.5, 0.49, 0.48, 0.47, 0.46, 0.44, 0.42, 0.42, 0.41, 0.4, 0.39, 0.38, 0.38, 0.38, 0.39, 0.39, 0.395, 0.4, 0.41, 0.43, 0.43, 0.45, 0.46, 0.47, 0.48, 0.5, 0.51, 0.52, 0.54, 0.55, 0.57, 0.58, 0.59, 0.6, 0.61, 0.61, 0.62, 0.62, 0.625, 0.625, 0.62, 0.62, 0.62, 0.62, 0.615, 0.61, 0.61, 0.61, 0.605, 0.605, 0.6, 0.6, 0.6, 0.61, 0.61, 0.61, 0.62, 0.62, 0.62, 0.63, 0.63, 0.63, 0.64, 0.65, 0.65, 0.65, 0.66, 0.67, 0.67, 0.69, 0.69, 0.7, 0.7, 0.71, 0.72, 0.72, 0.73, 0.74, 0.75, 0.75, 0.76, 0.77, 0.77, 0.78, 0.78, 0.79, 0.79]

fig = plt.figure() 					# тело графика
plt.title ("Анодно - сеточная характеристика")	    # название графика
plt.xlabel(r"Ускорющая разность потенциалов $\varphi_y, В$", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r"Анодный ток $I_a, mA$", fontsize=10, color='red') 		# ось ординат (y)

ax = fig.gca()          # возвращает текущую систему координат, not off

# ax.set_xticks(np.arange(100, 300, 10))        # задание сетки по х (от, до, шаг)
# ax.set_yticks(np.arange(0, 12, 1))            # задание сетки по y (от, до, шаг)

plt.scatter(x, y, s = 20, c='red', marker="o", alpha = 1, label='Практические измерения')     # отображение точек
plt.legend()   			# Отобразить легенду - label
""" plt.errorbar(x, y, xerr=0.25, yerr=0.01, fmt = ',')       # отобразить погрешности """

x1 = [84.5, 84.5]
y1 = [0, 0.625]
plt.plot(x1, y1, 'black', linestyle='--', marker='')

x2 = [44, 44]
y2 = [0, 0.505]
plt.plot(x2, y2, 'black', linestyle='--', marker='')

#  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
#  Добавляем линии основной сетки:
ax.grid(which='major', color = 'k', linewidth = 1)

#  Включаем видимость вспомогательных делений:
ax.minorticks_on()

# #  Вид вспомогательной сетки:
ax.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)
#
plt.show()
