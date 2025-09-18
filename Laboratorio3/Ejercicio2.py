import random

TOTAL = 504
MAX_ALTURA = 8
POSICIONES = TOTAL // MAX_ALTURA  # 63

# Crear bodega: 
bodega = [[] for i in range(POSICIONES)]

# Generar 504 códigos únicos (4 cifras)
codigos = random.sample(range(1000, 10000), TOTAL)

# Almacenar contenedores secuencialmente
i = 0
for codigo in codigos:
    bodega[i].append(codigo)
    if len(bodega[i]) == MAX_ALTURA:
        i += 1

# Función para retirar un contenedor
def retirar_contenedor(codigo):
    for pos, pila in enumerate(bodega):
        if codigo in pila:
            nivel = pila.index(codigo)
            pila.pop(nivel)
            return f"Código {codigo} retirado en posición {pos}, nivel {nivel}"
    return f"Código {codigo} no existe"

# Simular retiro de 3 contenedores
a_retirar = random.sample(codigos, 3)
for c in a_retirar:
    print(retirar_contenedor(c))

# Mostrar estado de la bodega
print("\nAltura actual de cada pila:")
for pos, pila in enumerate(bodega):
    print(f"Posición {pos}: {len(pila)} contenedores")
