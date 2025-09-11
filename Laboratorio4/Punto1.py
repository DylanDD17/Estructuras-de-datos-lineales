lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if not lista:
    print("La lista está vacía")
else:
    lista = lista[::-1]
    remove = lista.pop()

print(lista)