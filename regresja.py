import numpy as np

sep = ","
lista = []
with open('regresja.txt') as file:
    i = 0
    for line in file:
        data = line.split(sep)
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
    if B[0][0]<0:
        wynik = "y = " + str(round(B[1][0],2)) + " * x " + str(round(B[0][0],2)) 
    else:
        wynik = "y = " + str(round(B[1][0],2)) + " * x" + " + "  + str(round(B[0][0],2)) 
    return wynik

regresja = regresja_liniowa(lista)
print(regresja)