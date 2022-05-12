import numpy as np
import math

lista1 = [4,6,8,9,2,5,10,55,32]

def odchylenie_standardowe(vektor):
    v1 = np.array(vektor)
    v2 = np.ones(len(v1))
    sr = (np.dot(v1, v2))/len(v1)
    v3 = np.ones(len(vektor)) * sr
    sub = np.subtract(vektor,v3)
    trans = np.transpose(sub)
    wariancja = (np.dot(trans,sub))/len(vektor)
    odchylenie = math.sqrt(wariancja)
    return odchylenie

odch =  odchylenie_standardowe(lista1)
print(odch)