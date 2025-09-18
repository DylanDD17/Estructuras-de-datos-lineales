import random
import math

# Lista de novillos en corral #1 (pesos entre 250 y 600 kg)
corral1 = [random.randint(250, 600) for i in range(60)]  # 60 novillos
print(f"Lista inicial de novillos inicial: \n {corral1}")

# Pilas para los corrales 2 y 3
corral2 = []  # pila
corral3 = []  # pila

for peso in corral1[:]:
    if 280 <= peso <= 400:
        corral2.append(peso)
        corral1.remove(peso)
    elif 401 <= peso <= 500:
        corral3.append(peso)
        corral1.remove(peso)

# Corral 1
num_c1 = len(corral1)
prom_c1 = sum(corral1)/num_c1 if num_c1 > 0 else 0

# Corral 2
num_c2 = len(corral2)
prom_c2 = sum(corral2)/num_c2 if num_c2 > 0 else 0

# Corral 3
num_c3 = len(corral3)
prom_c3 = sum(corral3)/num_c3 if num_c3 > 0 else 0

# Camiones
camiones_c2 = math.ceil(num_c2/10)
camiones_c3 = math.ceil(num_c3/10)

# -------------------------
# Mostrar información
# -------------------------
print("\n")
print("=== RESULTADOS DE LA SELECCIÓN ===")
print("\nCantidad de novillos por corral:")
print(f"\tCorral #1 -> {num_c1} novillos, peso promedio: {prom_c1:.2f} kg")
print(f"\tCorral #2 -> {num_c2} novillos, peso promedio: {prom_c2:.2f} kg")
print(f"\tCorral #3 -> {num_c3} novillos, peso promedio: {prom_c3:.2f} kg")
print("\nCantidad de camiones requeridos para el corral 2 y 3:")
print(f"\tCamiones requeridos corral #2: {camiones_c2}")
print(f"\tCamiones requeridos corral #3: {camiones_c3}")