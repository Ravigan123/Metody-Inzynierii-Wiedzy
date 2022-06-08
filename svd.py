import numpy as np
import math

A = [[2,0,1], [1,1,0]]

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
    np.set_printoptions(suppress=True)
    if A.shape[0] != A.shape[1]:
        print("Macierz nie jest kwadratowa")
        exit()
    v = np.linalg.eig(A)
    return np.round(v[1],2)

def SVD(A):
    A = np.array(A)
    if A.shape[0] < A.shape[1]:
        v_prawe = np.dot(A,A.T)
        v_lewe = np.dot(A.T,A)
        war_w = war_wlasne(v_prawe)
        sorted(war_w)
        u_wlasne = wektory_wlasne(v_prawe)
        singularne = []
        for i in range(A.shape[0]):
            tmp = []
            for j in range(A.shape[1]):
                if i==j:
                    tmp.append(round(math.sqrt(war_w[i]),2))
                else:
                    tmp.append(0)
            singularne.append(tmp)
        singularne = np.array(singularne)
        war_w = np.array([war_w[0],war_w[1],0])
        v_wlasne = wektory_wlasne(v_lewe)
    else:
        v_prawe = np.dot(A,A.T)
        v_lewe = np.dot(A.T,A)
        war_w = war_wlasne(v_lewe)
        u_wlasne = wektory_wlasne(v_lewe)
        singularne = []
        for i in range(A.shape[0]):
            tmp = []
            for j in range(A.shape[1]):
                if i==j:
                    tmp.append(math.sqrt(war_w[i]))
                else:
                    tmp.append(0)
            singularne.append(tmp)
        singularne = np.array(singularne).T
        war_w = np.array([war_w[0],war_w[1],0])
        v_wlasne = wektory_wlasne(v_prawe)
    return u_wlasne,singularne, np.transpose(v_wlasne)
    

svd = SVD(A)

print(svd)