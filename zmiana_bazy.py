import numpy as np
import math

B = [[1,1,1,0,1,0,0,0], [1,1,1,0,-1,0,0,0], [1,1,-1,0,0,1,0,0], [1,1,-1,0,0,-1,0,0], [1,-1,0,1,0,0,1,0], [1,-1,0,1,0,0,-1,0], [1,-1,0,-1,0,0,0,1], [1,-1,0,-1,0,0,0,-1]]


A = [8,6,2,3,4,6,6,5]

def zmiana_bazy(A,B):
    A = np.array(A)
    B = np.array(B)
    if B.shape[0] != B.shape[1]:
        exit("Macierz nie jest kwadratowa")
    if A.shape[0] != B.shape[0]:
        exit("Błędny wektor")
    diag = np.dot(B.T,B)
    for i in diag:
        count = 0
        for j in range(len(diag)):
            if i[j]==0:
                count+=1
        if count != len(diag)-1:
            exit("Macież nie jest diagonalna")  
    B_nor = []
    for i in B.T:
        np.set_printoptions(suppress=True)
        dl = np.linalg.norm(i)
        B_nor.append(list(map(lambda v: v/dl, i)))
    B_nor1 = np.array(B_nor)
    jednostkowa = np.dot(B_nor1.T,B_nor1)
    for i in jednostkowa:
        count = 0
        count1 =0
        for j in range(len(jednostkowa)):
            if np.isclose(i[j],0)==True:
                count+=1
            if np.isclose(i[j],1)==True:
                count1+=1
        if count != len(jednostkowa)-1 and count1 != 1:
            exit("Macież nie jest jednostkowa")  
    return np.dot(B_nor1,A)


zmiana = zmiana_bazy(A,B)
print(zmiana)



