lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

pila = []

for elemento in lista:
    pila.append(elemento)

lista_invertida = []

while pila: # Mientras la pila no esté vacía
    lista_invertida.append(pila.pop()) # Operación de "pop"

print(lista_invertida)