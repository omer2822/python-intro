#import numpy as np
#import sympy as sp
##import matplotlib.pyplot as plt
#from matplotlib.pyplot import plot, figure
#from numpy.linalg import pinv # pseudo inverse
#x = sp.Symbol('x')

def count_fl(exp=3,mant=4,sign=1):
    lst = [0]
    for j in range(2**exp):
        k=2**j
        #print(k)
        for i in range(1, 2**mant):
            if (i*k) in lst:
                pass
            else:
                lst.append(i*k)
    # times 2 (for negative numbers) minus 1 (for single zero representation)
    leng = (len(lst))*(sign+1)-1
    return leng, lst
#print('possible rep:', count_fl()[1])
#print('len: ',count_fl()[0])



#print(rep)

import numpy as np

def fl_n(n, base=10, exp=3,mant=4,sign=1, iter=2):
    count, rep = count_fl()
    if abs(n) in rep:
        return n

    nt, sgn = abs(n), n/abs(n)

    while nt > max(rep):
        nt //= base
    if nt in rep:
        return (int(nt*sgn))
    for i in range(iter):
        nt//=base
        if nt in rep:
            return (int(nt*sgn))
    return int(nt*sgn)

    #n_arr = list(map(int, str(n)))



def max_abs_err():
    test1 = np.random.randint(200,1000,size=200)
    test2 = np.random.randint(10000,20000,size=1000)
    test3 = np.random.randint(10000, 2000000, size=10000)

    err1 = [abs(a - fl_n(a)) for a in test1]
    err2 = [abs(a - fl_n(a)) for a in test2]
    err3 = [abs(a - fl_n(a)) for a in test3]

    print(max(err1))
    print(max(err2))
    print(max(err3))

def min_abs_err():
    test1 = np.random.randint(1600,10000,size=1000)
    test2 = np.random.randint(2000, 10000, size=1000)
    test3 = np.random.randint(2000, 10000, size=1000)
    #test20 = np.random.randint(10000,100000,size=1000)
    #test30 = np.random.randint(10000, 8000000, size=1000)

    err1 = [abs(a - fl_n(a)) for a in test1]
    err2 = [abs(a - fl_n(a)) for a in test2]
    err3 = [abs(a - fl_n(a)) for a in test3]

    print(min(err1))
    print(min(err2))
    print(min(err3))

def max_rel_err():
    test1 = np.random.randint(200,5000,size=1000)
    test2 = np.random.randint(10000,80000,size=10000)
    test3 = np.random.randint(10000, 10000000, size=10000)

    err1 = [abs(a - fl_n(a))/a for a in test1]
    err2 = [abs(a - fl_n(a))/a for a in test2]
    err3 = [abs(a - fl_n(a))/a for a in test3]

    print(max(err1))
    print(max(err2))
    print(max(err3))


n = 153623
m=10
#print(fl_n(n))
#print((n-(n%m))//m)
#print(n//m)
print(count_fl()[1])

min_abs_err()