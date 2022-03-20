#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 20:42:31 2022

@author: edombek
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

def read_spec(fname):
    freq = []
    gamma = []
    
    with open(fname, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = "\t")
        list_reader = list(file_reader)
        for i in np.arange(1, 50000, 1):
            freq.append(float((list_reader[i])[1]))
            gamma.append(float((list_reader[i])[4]))
    return np.array(freq), np.array(gamma)

# wide - полу ширина окна(px), s - степень полинома и глубина взятия производных
def derivative(x,y,wide=50,s=2, di = -1):
    dx = x[1] - x[0]
    x_local = np.linspace(-wide*np.abs(dx),wide*np.abs(dx),2*wide+1)*np.sign(dx)
    ds = np.zeros((x.shape[0]-2*wide,s+1))
    coeffds = np.array([np.math.factorial(a) for a in range(s+1)])[::-1]
    for i in range(len(ds)):
        if di != -1: i = di-wide
        y_local = y[i:2*wide+1+i]
        p = np.polyfit(x_local, y_local, s)
        #кусок для отладки
        if di != -1:
            f = np.poly1d(p)
            plt.figure()
            plt.plot(x_local, y_local, 'k', alpha = 0.6)
            plt.plot(x_local, f(x_local), 'k')
            print(p)
            break
        ds[i] = (p*coeffds)[::-1]
        print(f'{i}/{len(ds)}')
    return x[wide:-wide], ds

freq, amp = read_spec("140145sam38.csv")

freqds, damps = derivative(freq, amp, wide=18, s=10)

fig, axs = plt.subplots(3,1, sharex=True, figsize=(16,10))
plt.xlabel('x')
for ax in axs:
    ax.grid(which='minor', color = 'k', linewidth = 0.25)
    ax.grid(which='major', color = 'k', linewidth = 1)
    ax.xaxis.set_minor_locator(AutoMinorLocator(20))
    ax.yaxis.set_minor_locator(AutoMinorLocator(5))
axs[0].title.set_text('f')
axs[1].title.set_text('f\'')
axs[2].title.set_text('f\"')

axs[0].plot(freq, amp, 'k', alpha=0.5)
for i, ax in enumerate(axs):
    ax.plot(freqds,damps[:,i], 'k')
plt.tight_layout()
plt.savefig('out.png')
plt.show()