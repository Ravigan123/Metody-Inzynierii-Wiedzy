import numpy as np
import math

A = [[0,2,1,0], [2,0,1,2], [2,1,1,0],[1,0,1,1]]

def macierzQR(A):
    li_wektorow = len(A)
    v1 = np.array(A[0])
    dl_u1 = math.sqrt(np.dot(v1,v1))
    e1 = np.divide(v1,dl_u1)
    U = [v1]
    Q = [e1]
    for i in range(1,li_wektorow): 
        suma_proj = 0
        v = np.array(A[i])
        for j in range(i):
            projp = np.dot(v, U[j])/np.dot(U[j],U[j])
            proj = np.dot(U[j],projp)
            suma_proj+=proj
        u = np.subtract(v,suma_proj)
        U.append(u)
        dl_u = math.sqrt(np.dot(u,u))
        e = np.divide(u,dl_u)
        Q.append(e)
    AT = np.transpose(A)
    np.set_printoptions(suppress=True)
    R = np.dot(Q,AT)
    QT = np.transpose(Q)
    QR = [QT,R]
    return QR

def war_wlasne(A):
    for i in range(100):
        QR = macierzQR(A)
        np.set_printoptions(suppress=True)
        A_pom = np.dot(np.transpose(QR[0]),A)
        A = np.dot(A_pom,QR[0])
    return np.diag(A)
 

def wektory_wlasne(A):
    A = np.array(A, float)
    if A.shape[0] != A.shape[1]:
        print("Macierz nie jest kwadratowa")
        exit()
    A_pom = []
    war_w = war_wlasne(A)
    print("Wartosci wlasne: ",war_w)
    for i in war_w:
        v = np.array(A)
        v = v - round(i,5) * np.eye(len(A))
        A_pom.append(v)
    X = []
    for j in range(len(A_pom)):
        Y = np.array(A_pom[j])
        i = 0
        for _ in range(len(Y)-1):                       
            pom = Y[i][i]
            tmp = i
            while pom == 0:
                tmp += 1
                if tmp > (len(Y)-1):
                    tmp = i
                if tmp == i:
                    i += 1
                    pom = Y[i][i]
                    break
                Y[[i,tmp]] = Y[[tmp,i]]
                pom = Y[i][i]
            for k in range(len(Y)):
                Y[i][k] /= pom
            for l in range(len(Y)):
                if l==i or Y[l][i] == 0:
                    continue
                Y[l] -= Y[l][i] * Y[i]
            i += 1
        X.append(Y)
    wek_wl = []
    for i in X:
        Z = []
        Y = i
        for j in range(len(Y)):
            tmp = 1
            flaga = 1
            for k in range(len(Y)):
                if Y[k][k] != 1:
                    flaga = 0
                tmp -= Y[j][k]
            if flaga == 1:
                tmp = 1
            Z.append(round(tmp,2))
        wek_wl.append(Z)
    wek_wl = np.array(wek_wl)
    return wek_wl

wektory = wektory_wlasne(A)

print("Wektory własne:\n" ,wektory)