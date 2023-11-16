# n_orig=7
# i=0
# n = n_orig
# while n != 1:
#     if n%2 == 0:
#         n/=2
#     else:
#         n = n*3 + 1
#     i += 1
# print("for n =", n_orig, ", i = ", i)


def collazt(n):
    i = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        i += 1
    return i

#print(collazt(7))


import itertools
from itertools import permutations

a = 'Omer'

#p = permutations(a)
l = list(itertools.combinations(a, 2))
print(l)

from math import comb

print(comb(4,2))