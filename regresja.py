import numpy as np
import math

sep = ","
lista = []
with open('regresja.txt') as file:
    i = 0
    for line in file:
        data = line.split(sep)
        print(data)
        lista.append(list(map(lambda a: float(a), data)))

print(lista)

def regresja_liniowa(lista):
    X = []
    Y = []
    for i in lista:
        X.append([1,i[0]])
        Y.append([i[1]])
    X = np.array(X)
    Y = np.array(Y)
    xTx = np.dot(X.T,X)
    xTy = np.dot(X.T,Y)
    B = np.dot(np.linalg.inv(xTx),xTy)
    wynik = "y = " + str(round(B[0][0],5)) + " + " + str(round(B[1][0],5)) + " * x"
    return wynik

regresja = regresja_liniowa(lista)
print(regresja)