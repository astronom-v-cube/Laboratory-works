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

h = 3
f = []

for i in range(1,49992):
    
    f.append(-(gamma[i+3] - 2*gamma[i] + gamma[i-3]) / h**2)



# fig = plt.figure() 					# тело графика
# plt.title (" ")	    # название графика
# plt.xlabel("frequency", fontsize=10, color='blue')		# ось абсцисс (x)
# plt.ylabel("gamma", fontsize=10, color='red') 		# ось ординат (y)
# plt.grid(True)                                # включение отображения стандартой сетки
# plt.plot(freq, gamma, label='Название линии')        # стандартный график (ломаная)
# plt.show()

fig = plt.figure() 
plt.title ("вторая производная")	    # название графика
plt.xlabel("frequency", fontsize=10, color='blue')		# ось абсцисс (x)
plt.ylabel("gamma", fontsize=10, color='red') 		# ось ординат (y)
plt.grid(True)                                # включение отображения стандартой сетки
plt.plot(freq[4:-4], f, label='Название линии')        # стандартный график (ломаная)

x_data = [140142.8067, 142139.7317, 142544.1610, 142785.5746, 144895.3400]
y_data = [0, 0, 0, 0, 0]
plt.errorbar(x_data, y_data, yerr=2e-7, markersize=40, linestyle='none', ecolor='black', elinewidth=1, capsize=3, capthick=1)

x_data = [140141.8067, 142138.7317, 142514.1610, 142905.5746, 144175.3400]
y_data = [0, 0, 0, 0, 0]
plt.errorbar(x_data, y_data, yerr=2e-7, markersize=40, linestyle='none', ecolor='red', elinewidth=1, capsize=3, capthick=1)
plt.show()