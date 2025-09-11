# Numero entero mayor a 6 cifras y retorne la suma de sus dígitos pares.
def separar_digitos(n):
    if n == 0:
        return []
    return separar_digitos(n // 10) + [n % 10]

def numeros_pares(digitos):
    if not digitos:
        return []
    if digitos[0] % 2 == 0:
        return [digitos[0]] + numeros_pares(digitos[1:])
    return numeros_pares(digitos[1:])

def suma_pares(digitos):
    if not digitos:
        return 0
    if digitos[0] % 2 == 0:
        return digitos[0] + suma_pares(digitos[1:])
    return suma_pares(digitos[1:])

if __name__ == "__main__":
    numero = 16582234
    numero2 = 13553
    print("Numeros:", numero, "y", numero2)

    digitos1 = separar_digitos(numero)
    digitos2 = separar_digitos(numero2)

    print("Digitos 1:", digitos1)
    print("Digitos 2:", digitos2)

    pares1 = numeros_pares(digitos1)
    pares2 = numeros_pares(digitos2)

    print("Pares 1:", pares1 if pares1 else "No hay numeros pares")
    print("Pares 2:", pares2 if pares2 else "No hay numeros pares")

    print("Suma pares 1:", suma_pares(digitos1))
    print("Suma pares 2:", suma_pares(digitos2))
