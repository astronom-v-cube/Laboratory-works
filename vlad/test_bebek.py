import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

freq = []
gamma = []

with open("140145sam38.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = "\t")
    list_reader = list(file_reader)
    for i in np.arange(1, 50000, 1):
        freq.append(float((list_reader[i])[1]))
        gamma.append(float((list_reader[i])[4]))

x = np.array(freq)
y = np.array(gamma)

def derivative(x,y,s):
    return (x[s:]+x[:-s])/2, (y[s:]-y[:-s])/(2*(x[s]-x[0]))


fig = plt.figure() 					# тело графика
plt.title ("Название графика")	    # название графика
plt.xlabel("Ось X", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("Ось Y", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(freq, gamma, label='Название линии')        # стандартный график (ломаная)
plt.show()

x_, y_ = derivative(x,y,s=100)

plt.figure()
plt.title ("Первая производная")	    # название графика
plt.xlabel("Ось X", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("Ось Y", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(x_, y_, label='Название линии')        # стандартный график (ломаная)
plt.show()

x__, y__ = derivative(x_,y_,s=1000)

plt.figure()
plt.title ("Вторая производная")	    # название графика
plt.xlabel("Ось X", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("Ось Y", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(x__, y__, label='Название линии')        # стандартный график (ломаная)
plt.show()