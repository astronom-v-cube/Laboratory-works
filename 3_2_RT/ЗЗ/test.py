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
    sigma.append(((l)/(a*d))*(I_ob[i]/(I_k[i]*R)))
temp = []
for i in np.arange(0, 21):
    temp.append((-0.020*EDS[i]**4+0.420*EDS[i]**3-3.577*EDS[i]**2+39.46*EDS[i]+27+273.15))
print(temp)
print(sigma)