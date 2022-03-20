
import numpy as np
R = 100
C = 6.8e-9
L = 0.33
e0 = 0.247
nu = np.linspace(1000, 5000, 4096)
If = e0/(np.sqrt(R**2+(nu*2*np.pi*L-1/(nu*2*np.pi*C))**2))

print(If)
