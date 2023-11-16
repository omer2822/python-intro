def Diff(func, x, h=1E-6):
    f, h = func, h
    return ((4/3 * (f(x+h) - f(x-h)) / (2*h)) - (1/3 * (f(x+(2*h)) - f(x-(2*h))) / (4*h)))
    #return (f(x + h) - f(x - h)) / (2 * h)

def newton_raphson(f, x0, Nmax=150, verbose=True):
    n=1
    while n <= Nmax:
        dfdx = Diff(f,x0)
        x0 -= f(x0)/ dfdx
        if verbose:
            print(f"iteration:{n}, xi: {x0}, f(xi): {f(x0)}, f'(xi):{dfdx}")

        if abs(f(x0)) < 1E-6:
            return x0

        n+=1

    return None
def bisect(f,a,b,Nmax=150,verbose=True):
    n=1
    while n <= Nmax:
        c = (a+b)/2.0
        if verbose:
#            print('n: {0:2d}, a: {1:3.6f}, c: {2:3.6f}, b: {3:3.6f}, f(c): {4:3.6f}'. \
#              format(n, a, c, b, f(c)))
            print(f"iteration:{n}, [a,b]: [{a}, {b}], (f(a),f(b)): ({f(a)}, {f(b)}), f(c):{f(c)}")

        if f(c) == 0 or n == Nmax:
            return c
        else:
            n+=1
            if f(c)*f(a) < 0:
                b=c
            else:
                a=c



# this method is the same as bisection method only you take "weighted average" instead of the middle of the interval.
def regula_falsi(f,a,b,Nmax=150,verbose=True):
    n=1
    while n <= Nmax:
        c = ((b*f(a) - a*f(b)) / (f(a)-f(b)))
        if verbose:
            print('n: {0:2d}, a: {1:3.6f}, c: {2:3.6f}, b: {3:3.6f}, f(c): {4:3.6f}'.format(n, a, c, b, f(c)))
            #print(f"iteration:{n}, [a,b]: [{a}, {b}], (f(a),f(b)): ({f(a)}, {f(b)}), f(c):{f(c)}")
        if abs(f(c)) <= (10**(-7)) or n == Nmax:
            return c
        else:
            n+=1
            if f(c)*f(a) < 0:
                b=c
            else:
                a=c



n1=3151
n=2009

def func1(x):
    return x**2 - n



alpha = bisect(func1,1,n,Nmax=35, verbose=False)
print('bisection method - the rot is: ', alpha)

alpha  = newton_raphson(func1, n/2, verbose=False)
print('newton raphson - the root is: ', alpha)

alpha = regula_falsi(func1, 1, n, Nmax=1000, verbose=False)
print('regula falsi - the root is: ', alpha)


