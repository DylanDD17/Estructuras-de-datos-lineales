# Reciba como parámetro un arreglo y un numero n, retornar la suma de los primeros n elementos.
def suma_n_elementos(lista, n):
    if n == 0:
        return 0
    return lista[n-1] + suma_n_elementos(lista, n-1)

if __name__ == "__main__":
    lista = [2, 4, 6, 8, 10, 12]
    n = 3
    print("Lista:", lista)
    print("Suma de los primeros", n, "elementos:", suma_n_elementos(lista, n))