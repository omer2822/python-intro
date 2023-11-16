from math import sqrt
psi = (1+sqrt(5))/2 #golden ratio

def fibonacci(n):
    res = (psi**n - (1-psi)**n)/sqrt(5)
    return int(res)
fibs = [fibonacci(i) for i in range(100)]
diff = [(fibs[i]**2 - (fibs[i-1]*fibs[i+1])) for i in range(1,80)]

print(fibs)