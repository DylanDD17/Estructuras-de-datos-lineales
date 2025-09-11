def numeros_antes(n):
    return list(range(1, n+1))

def numeros_pares_antes(n):
    pares = []
    for i in range(1, n+1):
        if i % 2 == 0:
            pares.append(i)
    suma = sum(pares)
    return suma

if __name__ == "__main__":
    n = 10
    print("Numero:", n)
    print("Numeros antes de", n, ":", numeros_antes(n))
    pares = [i for i in range(1, n+1) if i % 2 == 0]
    print("Pila de numeros pares antes de", n, ":", pares)
    print("Suma de numeros pares antes de", n, ":", numeros_pares_antes(n))
