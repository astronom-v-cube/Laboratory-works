import numpy as np
import matplotlib.pyplot as plt
import requests
def test(a,b):
    userdata = {"in_ua": a, "in_ub": b, "ok":"ok"}
    resp = requests.post('https://spec.jpl.nasa.gov/ftp/pub/catalog/catform.html', data=userdata)
    print(a,b)
    #print(resp.text)
    return float(resp.text.split('показания милливольтметра ')[1].split(' мВ.')[0])

print(test(1,1))

a = np.array([450,750,1400, 1900])/773
b = np.linspace(0,10,1024)
e = []
for a_ in a:
    e_ = np.zeros(b.shape)
    for i, b_ in enumerate(b):
        e_[i] = test(b_,a_)
    e.append(e_)
    plt.plot(b, e_, label=f'Ток магнита({a_})')
plt.legend()
