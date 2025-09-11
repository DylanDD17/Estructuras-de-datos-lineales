# Compare dos arreglos unidimensionales de enteros, de igual longitud, y determine si son iguales elemento a elemento.
import random

def comparar_listas_recursivo(lista1, lista2, i=0):
    if i == len(lista1):
        return True
    if lista1[i] != lista2[i]:
        return False
    return comparar_listas_recursivo(lista1, lista2, i + 1)

lista1 = [random.randint(1, 10) for i in range(5)]
print(lista1)
lista2 = [random.randint(1, 10) for i in range(5)]
print(lista2)

# Mostrar par por par si son iguales o no
for i in range(len(lista1)):
    if lista1[i] == lista2[i]:
        print(f"Elemento {i}: {lista1[i]} == {lista2[i]} -> Iguales")
    else:
        print(f"Elemento {i}: {lista1[i]} != {lista2[i]} -> Diferentes")

son_iguales = comparar_listas_recursivo(lista1, lista2)
print("Son iguales?", son_iguales)