import math

lista = []
listax = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
sep = " "
with open('australian.dat') as file:
    for line in file:
        data = line.split(sep)
        lista.append(list(map(lambda a: float(a), data)))

def CzyKredyt(lista, x, k):
    slownik = {}
    suma = 0
    for i in lista:
        for j in range(len(x)-1):
            suma+=(x[j]-i[j])**2
        tmp = math.sqrt(suma)
        suma = 0
        kd = i[-1]
        if not kd in slownik:
            slownik[kd] = []
        slownik[kd].append(tmp)
    count_key = len(slownik.keys())
    lista_keys = []
    for i in slownik.keys():
        lista_keys.append(i)
    wynik = {}
    i = 0
    while(i<count_key):
        suma = 0
        sort_lista = sorted(slownik[i])
        for j in sort_lista[:k]:
            suma+=j
        wynik[lista_keys[i]] = suma
        i+=1
    min_value = min(wynik.values())
    keyNaj = list(wynik.keys())[list(wynik.values()).index(min_value)]
    if(keyNaj == 0):
        return False
    if(keyNaj == 1):
        return True

wynik = CzyKredyt(lista,listax,5)
print(wynik)