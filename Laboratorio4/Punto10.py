# Dada una lista de números enteros positivos, invierta la lista.
def invertir_lista(lista):
    if not lista: 
        return []
    return [lista[-1]] + invertir_lista(lista[:-1])

lista = [1, 2, 3, 4, 5]
print("Lista original:", lista)
print("Lista invertida:", invertir_lista(lista))
