def separar_digitos(numero):
    digitos = []
    while numero > 0:
        digitos.append(numero % 10)
        numero //= 10

    digitos.reverse()
    return digitos
    
def numeros_pares(digitos):
    pares = []
    for numero in digitos:
        if numero % 2 == 0:
            pares.append(numero)
    if not pares:
        return "No hay numeros pares"
    return pares

def suma_pares(digitos):
    suma = 0
    for numero in digitos:
        if numero % 2 == 0:
            suma += numero
    return suma

if __name__ == "__main__":
    numero = 16582234
    numero2 = 13553
    print("Numeros: 1.", numero, "y 2.", numero2)
    digitos = separar_digitos(numero)
    digitos2 = separar_digitos(numero2)
    print("Digitos del numero:", digitos)
    print("Digitos del numero 2:", digitos2)
    pares = numeros_pares(digitos)
    pares2 = numeros_pares(digitos2)
    print("Numeros pares:", pares)
    print("Numeros pares del numero 2:", pares2)
    suma = suma_pares(digitos)
    suma2 = suma_pares(digitos2)
    print("Suma de numeros pares:", suma)
    print("Suma de numeros pares del numero 2:", suma2)