# Numero n, n ≥ 1, y calcule el cuadrado, de n: es igual a la suma de los n primeros números impares.
def cuadrado(n):
    if n == 1:
        return 1
    return (2 * n - 1) + cuadrado(n - 1)

n=4
print(cuadrado(n))