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

qr = macierzQR(A)
print(qr)

def war_wlasne(A):
    for i in range(100):
        QR = macierzQR(A)
        np.set_printoptions(suppress=True)
        A_pom = np.dot(np.transpose(QR[0]),A)
        A = np.dot(A_pom,QR[0])
    return np.diag(A)

wlasne = war_wlasne(A)
print(wlasne)