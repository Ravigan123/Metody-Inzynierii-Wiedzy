import math

lista = []
separator =' '
with open("C:/Users/Dominik/Desktop/australian.dat", "r+") as file:
    for line in file:
        tmp = line.split(separator)
        lista.append(list(map(lambda e: float(e), tmp)))

listax = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def CzyKredyt(x, lista, k):
    slownik = {}
    listaT = []
    suma = 0
    for i in lista:
        for j in range(len(x)-1):
            suma +=(x[j]-i[j])**2
        tmp = math.sqrt(suma)
        suma = 0
        kd = i[-1]
        tupla = (kd, tmp)
        listaT.append(tupla)
    for para in listaT:
        c = para[0]
        if not c in slownik:
            slownik[c] = []
        slownik[c].append(para[1])
    keysCount = len(slownik.keys())
    licznik = 0
    keysList = []
    wynik = {}
    for x in slownik.keys():
        keysList.append(x)
    while(licznik<keysCount):
        suma1 = 0
        listaSort = sorted(slownik[licznik])
        for p in listaSort[:k]:
            suma1+=p
        wynik[keysList[licznik]] = suma1
        licznik+=1
    NajmniejszaOdl = 11111111
    licznik = 0
    for p in wynik.values():
        if(p<NajmniejszaOdl):
            NajmniejszaOdl = p
    keyNaj = list(wynik.keys())[list(wynik.values()).index(NajmniejszaOdl)]
    if(keyNaj == 0):
        return False
    if(keyNaj == 1):
        return True


print(CzyKredyt(listax, lista, 5))