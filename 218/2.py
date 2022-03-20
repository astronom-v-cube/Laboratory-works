i = 1
while i<10000:

    dc1 = 0.000000002
    c1 = 0.000001
    r1 = float(input('r1 = '))
    r2 = float(input('r2 = '))
    dr2 = float(input('dr2 = '))
    dc2 = ((r1/r2)*dc1)+(((c1*r1)/r2**2)*dr2)
    print('Погрешность - ' + str(dc2))
    i = i+1
