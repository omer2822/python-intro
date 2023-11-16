import numpy as np

def CheckIfPrime(N):
    if (N <= 3):
        s=1
    else:
        n = range(2, N-1)
        rem = [N % x for x in n]
        if (np.prod((np.array(rem))) != 0):
            s = 1
        else:
            s = 0
    return s


print(CheckIfPrime(1997))
