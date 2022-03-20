import numpy as np
import math
r = float(input('Введи r: '))
v = 120
c = 0.00000075
vz = 114
vg = 99
v0 = 104
r0 = 9780
# t1 = - (math.log((vz)/(v-(v-vg))))*r*c
# t2 = (math.log(((vz-v0)*r + (vz-v)*r0)/(vg-v0)*r + (vg-v)*r0))*c
print (((((vz-v0)*r + (vz-v)*r0)/(vg-v0)*r + (vg-v)*r0))*c)
