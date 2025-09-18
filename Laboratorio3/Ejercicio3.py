# Torres, pisos y viviendas
torres = ["A", "B", "C", "D", "E", "F", "G"]
pisos = 10
viviendas_por_piso = 6

# Construcción del conjunto (listas anidadas)
conjunto = []

for t in range(len(torres)):  # 7 torres
    torre_lista = []
    for p in range(1, pisos + 1):  # 10 pisos
        piso_lista = []
        for v in range(1, viviendas_por_piso + 1):  # 6 viviendas
            codigo = torres[t] + "-" + str(p) + str(v).zfill(2)  # Ej: A-101
            piso_lista.append([codigo, False])  # False = disponible
        torre_lista.append(piso_lista)
    conjunto.append(torre_lista)


# Función para vender una vivienda
def vender_vivienda(codigo):
    for t in range(len(conjunto)):
        for p in range(len(conjunto[t])):
            for v in range(len(conjunto[t][p])):
                vivienda = conjunto[t][p][v]
                if vivienda[0] == codigo:
                    if vivienda[1] == False:
                        vivienda[1] = True
                        print("Vivienda", codigo, "vendida en Torre", torres[t], "Piso", p + 1)
                    else:
                        print("Vivienda", codigo, "ya estaba vendida")
                    return
    print("Vivienda no existe")

# Mostrar la torre que deseemos
def mostrar_estado(torre_letra, piso_num):
    if torre_letra not in torres:
        print("Torre no existe")
        return
    if piso_num < 1 or piso_num > pisos:
        print("Piso no existe")
        return

    t = torres.index(torre_letra)
    piso = conjunto[t][piso_num - 1]

    print("Estado Torre", torre_letra, "Piso", piso_num, ":")
    for v in range(len(piso)):
        estado = "VENDIDA" if piso[v][1] else "DISPONIBLE"
        print(" ", piso[v][0], ":", estado)


# Ejemplos

vender_vivienda("E-901")
vender_vivienda("E-902")

print("\n--- Estado de Torre E, Piso 9 ---")
mostrar_estado("E", 9)