# Reciba dos arreglos y muestre los arreglos pareados.
def mostrar_pareados(lista1, lista2, i=0):
    if i == len(lista1):  # caso base
        return
    print(lista1[i], lista2[i])
    mostrar_pareados(lista1, lista2, i + 1)

lista1 = [1, 2, 3, 4]
lista2 = ["a", "b", "c", "d"]

mostrar_pareados(lista1, lista2)
