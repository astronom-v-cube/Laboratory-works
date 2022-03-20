from numpy import *
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1,11)

#меандр
An = lambda n: 2/(np.pi*n)*(1-(-1)**n)
An(n)/An(1)*5
fi = pi/2

plt.figure()
plt.bar(n, An(n),width = 0.4)
plt.xlabel('N')
plt.ylabel('An')
plt.title('Меандр')

#пила
an = lambda n:(np.pi*n*sin(np.pi*n)+cos(np.pi*n)-1)/(np.pi*n)**2
bn = lambda n:(sin(np.pi*n)-np.pi*n*cos(np.pi*n))/(np.pi*n)**2
An = lambda n: sqrt(an(n)**2+bn(n)**2)
An(n)*8
fi = lambda n: -np.arctan(an(n)/bn(n))/np.pi*180
fi(n)

plt.figure()
plt.bar(n, An(n),width = 0.4)
plt.xlabel('N')
plt.ylabel('An')
plt.title('Пила')

#треугольник
An = lambda n:  2*(2*sin(np.pi*n/2)-np.pi*n*cos(np.pi*n/2))/(np.pi*n)**2 - (4*sin(np.pi*n) - 4*sin(np.pi*n/2) - 2*np.pi*n*cos(np.pi*n/2))/(np.pi*n)**2
An(n)
fi = pi/2 , 3*pi/2

plt.figure()
plt.bar(n, abs(An(n)),width = 0.4)
plt.xlabel('N')
plt.ylabel('An')
plt.title('Треугольник')

n = np.arange(1,10)
plt.plot(n, An(n), 'ko')

plt.show()
