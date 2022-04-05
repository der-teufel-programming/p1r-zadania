def matrix_mul(a, b):
    d = [[0,0],[0,0]]
    d[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
    d[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
    d[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
    d[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
    return d

def matrix_sq(a):
    return matrix_mul(a,a)

def matrix_pow(b, n):
    a = [[1,0],[0,1]]
    c = b.copy()
    while n > 0:
        if n % 2 != 0:
            a = matrix_mul(a.copy(), c)
        n = n // 2
        c = matrix_sq(c.copy())
    return a

def fib(n):
    f = [[1,1],[1,0]]
    return matrix_pow(f, n - 1)[0][0]

def fibsum(lim):
    (a,b) = (1,1)
    s = 1
    res = 0
    while b < lim:
        res += s * b
        a, b = b, a+b
        s = 1 - s
    return res

print(fibsum(3*10**6))
