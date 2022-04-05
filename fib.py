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

n = int(input("n = "))

fib = [[1,1],[1,0]]

print(matrix_pow(fib, n - 1)[0][0])
