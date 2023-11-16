def is_prime(p):
    for i in range(2,p//2+1):
        if p%i==0:
            return False
    return True

def Dec_gormim(p):
    gor=[]
    for i in range(2,p//2+1):
        if p%i==0:
            if is_prime(i)==True:
                gor.append(i)
    return gor



def is_armstrong_number(t):
    n=t
    digits=[]
    while n>0:
        digits.append(n%10)
        n = n // 10
    l = len(digits)
    for i in range(l):
        print(digits[i])
        digits[i] = digits[i]**l
        print(digits[i])

    return sum(digits)==t

#print(is_armstrong_number(153))


#print(Dec_gormim(12))

import numpy as np

def euclid_dist(p1,p2):
    d=0
    for i in range(len(p1)):
        d += (p1[i]-p2[i])**2
    return d**0.5

def euclidean_distance(p1, p2):
  #### IMPLEMENT YOUR CODE HERE ####
  d = p2-p1
  print(d)
  print(np.sqrt(sum([di**2 for di in d])))
  return np.linalg.norm(d)

x = np.array([7,32,16])
y = np.array([10,40,31])
print(euclidean_distance(x,y))
print(euclid_dist(x,y))
print(np.sqrt(9+64+225))