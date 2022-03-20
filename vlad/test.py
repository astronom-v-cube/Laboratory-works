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

h = 0.1
f = []

for i in range(1, 4999):
    f.append(-(gamma[i+1] - 2*gamma[i] + gamma[i-1]) / h)

x = np.linspace(140000, 145000, 4998)

fig = plt.figure() 					# тело графика
plt.title ("Название графика")	    # название графика
plt.xlabel("Ось X", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("Ось Y", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(freq, gamma, label='Название линии')        # стандартный график (ломаная)
plt.show()


plt.title ("Название графика")	    # название графика
plt.xlabel("Ось X", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("Ось Y", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(x, f, label='Название линии')        # стандартный график (ломаная)
plt.show()