# Numero entero mayor a 6 cifras y retorne la cantidad de dígitos que tiene el numero.
def contar_digitos(n):
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)

numero = 16582234
print("La cantidad de digitos del numero", numero, "es:", contar_digitos(numero))