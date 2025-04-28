MOD = 10**9 + 7

def multiply(F, M):
    x = (F[0][0]*M[0][0] + F[0][1]*M[1][0]) % MOD
    y = (F[0][0]*M[0][1] + F[0][1]*M[1][1]) % MOD
    z = (F[1][0]*M[0][0] + F[1][1]*M[1][0]) % MOD
    w = (F[1][0]*M[0][1] + F[1][1]*M[1][1]) % MOD
    F[0][0], F[0][1], F[1][0], F[1][1] = x, y, z, w

def power(F, n):
    if n == 0 or n == 1:
        return
    M = [[1, 1], [1, 0]]
    power(F, n // 2)
    multiply(F, F)
    if n % 2 != 0:
        multiply(F, M)

def fibonacci(A):
    if A == 1 or A == 2:
        return 1
    F = [[1, 1], [1, 0]]
    power(F, A - 2)
    return (F[0][0] + F[0][1]) % MOD

# Example usage
A = 10
pint(fibonacci(A))  # Output: 3
