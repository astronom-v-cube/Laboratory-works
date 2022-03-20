import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

v = np.loadtxt("LW222-2.txt")       # открыть файл с данными
y = v[:,0]		# первый столбец - y
x = v[:,1]			# второй стобец - x
z = x - (10000*(y/1000))
p = np.polyfit(z, y, 1)				# создание полинома первой степени - апроксимация
ya = np.polyval(p, x)				# координаты y для полинома

fig = plt.figure() 					# тело графика
plt.title ("ВАХ неоновой лампы")	# название графика
plt.xlabel("Напряжение, В", fontsize=10, color='blue')		# ось абсцисс (у)
plt.ylabel("Сила тока, А", fontsize=10, color='red') 		# ось ординат (х)
plt.grid(True)      # включение отображения сетки
# plt.plot(x, z, label='Название линии')
# plt.plot(p, ya, label='ВАХ неоновой лампы')

ax = fig.gca()
# ax.set_xticks(np.arange(100, 300, 10))
# ax.set_yticks(np.arange(0, 12, 1))

plt.scatter(z, y, s=7, c='red', marker="o", alpha = 0.5, label='Результаты измерений')
plt.legend()   			# Отобразить легенду - label
# plt.errorbar(x, y, xerr=1, yerr=0.3, color = 'snow', ecolor='purple')


################################

#  Устанавливаем интервал основных и
#  вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.2))

#  Добавляем линии основной сетки:
ax.grid(which='major', color = 'k', linewidth = 1)

#  Включаем видимость вспомогательных делений:
ax.minorticks_on()
#  Теперь можем отдельно задавать внешний вид
#  вспомогательной сетки:
ax.grid(which='minor', color = 'dimgrey', linestyle = ':', linewidth = 0.5)
























plt.show()



#https://devpractice.ru/matplotlib-lesson-1-quick-start-guide/
