import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

EDS = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]			# первый столбец - y
I_ob = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 10, 13, 16, 19, 22, 31, 39]			# второй стобец - x
I_k = [88.5, 85.6, 51.95, 64.5, 47, 31.95, 24.35, 16.8, 12.95, 9.8, 6.8, 4.95, 3.95, 3.45, 3.45, 3.5, 3.55, 3.7, 3.75, 4.3, 4.7]
R = 10
a = 0.4
d = 0.14
l = 0.7
sigma = []
for i in np.arange(0, 21):
    sigma.append(np.log((l)/(a*d))*(I_ob[i]/(I_k[i]*R)))
temp = []
for i in np.arange(0, 21):
    temp.append(1000/(-0.020*EDS[i]**4+0.420*EDS[i]**3-3.577*EDS[i]**2+39.46*EDS[i]+27+273.15))
x = np.arange(0, 20)
p = np.polyfit(temp[9:23], sigma[9:23], 1)				# создание полинома первой степени - апроксимация
ya = np.polyval(p, temp[9:23])				# координаты y для полинома

fig = plt.figure() 					# тело графика
plt.title (r"Зависимость $ln(\sigma)$ от $10^3/T$")	    # название графика
plt.xlabel(r"$10^3/T$", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel(r"$ln(\sigma)$", fontsize=10, color='red') 		# ось ординат (y)
plt.plot(temp[9:23], ya, label='Линейная аппроксимация')        # график - апрокимация (прямая)

ax = fig.gca()          # возвращает текущую систему координат, not off

plt.scatter(temp, sigma, s = 20, c='red', marker="o", alpha = 1, label='Практические измерения')     # отображение точек
plt.legend()   			# Отобразить легенду - label

# #  Устанавливаем интервал основных и вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.02))

# #  Добавляем линии основной сетки:
ax.grid(which='major', color = 'k', linewidth = 1)

#  Включаем видимость вспомогательных делений:
ax.minorticks_on()
#
#  Вид вспомогательной сетки:
ax.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)
#
plt.show()
print(f'темп {temp}')
print(f'сигма {sigma}')

# https://pyprog.pro/mpl/mpl_short_guide.html
# https://devpractice.ru/matplotlib-lesson-1-quick-start-guide/
# https://python-scripts.com/matplotlib#1
# https://pyprog.pro/mpl/mpl_adding_a_line.html
