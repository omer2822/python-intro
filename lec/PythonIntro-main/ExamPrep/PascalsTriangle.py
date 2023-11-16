# Print Pascal's Triangle in Python


def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)


def pascal_triangle(n):
    for i in range(n):
        for j in range(n-i+1):
            # for left spacing
            print(end='  ')
        for j in range(i+1):
            # nCr = n!/((n-r)!*r!)
            #print(int(factorial(i)/(factorial(j)*factorial(i-j))), end=' ')
            print('{:>3}'.format(int(factorial(i) / (factorial(j) * factorial(i - j)))), end=' ')
        # for new line
        print()


pascal_triangle(20)

print()




from math import sqrt
def s1(x):
    x = (x**2 + sqrt(x*(x+1)) + sqrt(x**5 - x))
    y = (x**8-5)**1/3 * sqrt(x**4 +x +1)
    return x/y

#print(sum([s1(i) for i in range(10000)]))







#print(sum([srs(i) for i in range(10)]))