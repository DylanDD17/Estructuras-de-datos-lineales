# Dada una pila de enteros, muestre en consola los elementos en orden invertido (del tope al fondo).
def mostrar_invertido(pila):
    # Caso base
    if not pila:
        return

    tope = pila.pop()
    print(tope)
    mostrar_invertido(pila)  # llamada recursiva con el resto

pila = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if not pila:
    print("La pila está vacía")
else:
    mostrar_invertido(pila)
