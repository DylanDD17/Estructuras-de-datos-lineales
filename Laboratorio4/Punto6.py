def numeros_antes(n):
    if n == 0:
        return []
    return numeros_antes(n-1) + [n]

def numeros_pares_antes(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + numeros_pares_antes(n-1)
    return numeros_pares_antes(n-1)

n = 10
print("Numero:", n)
print("Numeros antes de", n, ":", numeros_antes(n))
print("Suma de numeros pares antes de", n, ":", numeros_pares_antes(n))
