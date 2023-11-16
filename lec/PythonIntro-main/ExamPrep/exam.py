# write python function that input vector v,  integer n and returns the v_i that appers more than n times

def elementsThatApearsMoreThan_n(v, n):
    vTag = [vi for vi in v if v.count(vi) >= n]
    return set(vTag)
v = (1,7,9,5,0,3,6,9, 4,9,7,0)
print(elementsThatApearsMoreThan_n(v,2))

# powerMethod for computing MAX(eigenValues(A))
import numpy as np
def powerMethod(A, N):
    Xn = np.ones((A.shape[1],1))
    cn = 0
    for i in range(N):
        Yn = np.dot(A, Xn)
        cn1 = np.linalg.norm(Yn)
        if abs(cn1 - cn) < 0.0001:
            break
        cn = cn1
        Xn = np.dot(1/cn, Yn)
    return cn

def power_iteration(A, N: int):
    bk = np.ones((3,1))

    for i in range(N):
        b1 = np.dot(A, bk)
        b1_norm = np.linalg.norm(b1,np.inf)
        bk = b1 / b1_norm
    print(bk)
    return np.linalg.norm(bk,np.inf)

Aw = np.matrix([[0,11,5],[-2,17,-7],[-4,26,-10]])
#print(power_iteration(Aw, 100000))


C = np.random.randint(1,10, size=(5,5))
print(C)
print(C[[1,2,-1]]) #rows 1,2,4
# C[1,1] C[1,2] C[1,3]
# C[2,1] C[2,2] C[2,3]
# C[4,1] C[4,2] C[4,3]
print(C[[1,2,-1]][:, [1,2,-2]])


