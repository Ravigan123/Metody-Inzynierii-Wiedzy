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
    A = []
    B = []
    for i in lista:
        A.append([1,i[0]])
        B.append([i[1]])
    A = np.array(A)
    B = np.array(B)
    A_trans_A = np.dot(A.T,A)
    A_trans_B = np.dot(A.T,B)
    B = np.dot(np.linalg.inv(A_trans_A),A_trans_B)
    if B[0][0]<0:
        wynik = "B = " + str(round(B[1][0],2)) + " * A " + str(round(B[0][0],2)) 
    else:
        wynik = "B = " + str(round(B[1][0],2)) + " * A" + " + "  + str(round(B[0][0],2)) 
    return wynik

regresja = regresja_liniowa(lista)
print(regresja)