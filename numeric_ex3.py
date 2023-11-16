from numpy.linalg import solve, norm # for the error calculations
import matplotlib.pyplot as plt

def jacobi(A, b, x0, eps = 1e-3, max_iter=1000):
    n = len(x0)
    res = x0.copy()
    res_true = solve(A, b)
    abs_errors = []
    rel_errors = []
    for k in range(max_iter):
        for i in range(n):
            s = 0
            for j in range(n):
                if j!=i:
                    s += A[i][j] * res[j]
            res[i] = (1 / A[i][i]) * (b[i] - s)

        err = res_true - res
        abs_errors.append(norm(err))
        rel_errors.append(norm(err) / norm(res_true))
        print('absulote error:', norm(err), ', relative error:', norm(err) / norm(res_true))

    #plot errors
    plt.plot(range(max_iter), rel_errors, range(max_iter), abs_errors)
    plt.show()


    return res

""""
    gauss_seidel

"""

def gauss_seidel(A, b, x0, eps = 1e-5, max_iter=1000):
    n = len(x0)
    res = x0.copy()
    res_true = solve(A, b)
    abs_errors = []
    rel_errors = []
    for k in range(max_iter):
        for i in range(n):
            s1, s2 = 0, 0
            for j1 in range(i):
                s1 += A[i][j1]*res[j1]
            for j2 in range(i+1, n):
                s2 += A[i][j2]*res[j2]

            res[i] = (1 / A[i][i]) * (b[i] - s1 - s2)
        err = res_true - res
        print('absulote error:', norm(err), ', relative error:', norm(err)/norm(res_true))
        abs_errors.append(norm(err))
        rel_errors.append(norm(err)/norm(res_true))
    # plot errors
    plt.plot(range(max_iter), rel_errors, range(max_iter), abs_errors)
    plt.show()
    return res


from numpy import array

A = [[7.0, -2.0, 1.0], [14.0, -7.0, -3.0], [-7.0, 11.0, 18.0]]
print(A)
b = [12.0, 17.0, 5.0]

x0 = [0.0, 0.0,0.0]

solution = gauss_seidel(A, b, x0, max_iter=20)
solution = jacobi(A, b, x0, max_iter=20)
print(solution)

x0 = [12.0, 17.0,5.0]

solution = gauss_seidel(A, b, x0, max_iter=20)
solution = jacobi(A, b, x0, max_iter=20)
print(solution)
