def separar_digitos(numero):
    digitos = []
    while numero > 0:
        digitos.append(numero % 10)
        numero //= 10

    digitos.reverse()
    return digitos

def contar(digitos):
    return len(digitos)

if __name__ == "__main__":
    numero = 16582234
    print("Numero:", numero)
    print("Cantidad de digitos:" , contar(separar_digitos(numero)))