import numpy as np
import math

lista = []
sep = " "
with open('australian.dat') as file:
    for line in file:
        data = line.split(sep)
        lista.append(list(map(lambda a: float(a), data)))

def vektorowo(lista1,lista2, utnij=False):
    if lista1 == lista2:
        return 0
    if utnij:
        lista1 = lista1[:-1]
        lista2 = lista2[:-1]
    v1 = np.array(lista1)
    v2 = np.array(lista2)
    v3 = v1 - v2
    c = np.dot(v3,v3)
    wynik = math.sqrt(c)
    return wynik
	
def lista_suma(lista):
    lista_odl = []
    for i in range(len(lista)):
        begin = lista[i]
        lista_odl.append([])
        for j in lista:
            odl = vektorowo(begin, j, True)
            lista_odl[i].append(odl)
    lista_sum = []
    for i in lista_odl:
        suma = 0
        for j in range(len(lista_odl[0])):
            suma +=i[j]
        lista_sum.append(suma)
    return lista_sum
	
def kolorowanie(lista):
    liczba_wartosci = 2
    for i in lista:
        i[-1] = np.random.randint(0,liczba_wartosci)
    for i in range(3):
        lista_srodkow = []
        for j in range(2):
            lista_pom = [x for x in lista if x[-1]==j]
            lista_sum = lista_suma(lista_pom)
            srodek = lista_sum.index(min(lista_sum))
            lista_srodkow.append(lista_pom[srodek])
        for k in lista:
            tmp = 0
            min_odl = vektorowo(k, lista_srodkow[0], True)
            for l in range(1,liczba_wartosci):
                odl = vektorowo(k, lista_srodkow[1], True)
                if odl<min_odl:
                    min_odl = odl
                    tmp = 1
                k[-1] = tmp
    return lista
			
k_srednich = kolorowanie(lista)
print(k_srednich)