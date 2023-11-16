
"""
newlist = [expression for item in iterable if condition == True]
"""
import array

a = [1, 2, -1, 3, 4, 5, 6, 7]
b = ['a', 'b', 'c', 'd']
fruits = ['banana', 'orange']

squares = [i * i for i in range(10)]
A_square = [i * i for i in a]
prod = [(x,y) for x in a for y in b]  #cartesian products

even = [x for x in a if x % 2 == 0]
odd  = [x for x in a if x % 2 != 0]

newlist = [x if x != "banana" else "orange" for x in fruits] #Return "orange" instead of "banana":
print(A_square)



def get_price(price):
    return price if price > 0 else 0

prices = [get_price(i) for i in a]




def get_alphabets(startletter, stopletter, step):
    for c in range(ord(startletter.lower()), ord(stopletter.lower()), step):
        yield chr(c)

print(list(get_alphabets("a", "h", 1)))