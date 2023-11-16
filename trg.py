'''
 trg 1

math operator: +, +=, -, *, /, **, //, %

5//2 # == 2
10//3 # == 3

x % y == x - y*(x//y) # cool !

comparison operator: <, >, ==, !=, and, or, not
assigment: =
types (floats, ints..)
strings: +, +=, *, *=, ==, < (lexicographical(ascii) order compare)
strings as arrays: str[i] + str[j], str[i:j]
len (saved word)
str.isalpha() # only_letters?
str.isdigit str.islower str.isupper

if, else, for, print, range, math.sqrt, import,

7 boom:
for i in range(1,Max):
    if i%7==0 or i%10==7 or i//10==7:
        print ('boom')
    else:
        print(i)
fibonachi:
factorial:
'''
'''
trg 2

collatz, base 2 to base 10 : h.w
print with format(f{}) ?
        
casting: int(4.3)->4, float(4)->4.0
input(),  
'''
'''
trg 3:
base 2 to base 10
x = "101111" # binary(23)
x = x[::-1] #reverse
for i, c in enumarate(x):
break, continue
is_prime():
list = []
l3 = l1 + l2
lst.append()

if 5 in lst
for item in lst
max, len, sum, count, insert, pop, remove, index, sorted()
print([i**2 for i in range(1,10)]) # similar to set notation in math
print(sum(int(c) * 2**i for i,c in enumarate(x[::-1])))
list comprehension
tuples are imutable (good for acting as keys)

dictianory : map from key to value
for k,v in dict.items():
    print(f"key: {k}, value: {v}")
#print with aligment:
def multiplication_table(n=10):
    for i in range(1,n):
        for j in range(1,n):
            print(f"{i*j:>3}", end=' ')
        print()

def is_prime(n):


phermas ""primes""
'''
"""
trg 4 

...
tic tac toe

"""


def is_ribua(n):
    squares = (i**2 for i in range(1,10**6)) #lazy evaluation
    return n in squares

def is_square(n):
    return int(n**(1/2))**2 == n

print(is_square(144))
print(is_ribua(100))


#print with aligment:

def multiplication_table(n=10):
    for i in range(1,n):
        for j in range(1,n):
            print(f"{i*j:3}", end=' ')
        print()


multiplication_table(12)