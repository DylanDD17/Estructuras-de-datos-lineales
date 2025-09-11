a = int(input("Escriba el numerito1: "))
b = int(input("Escriba el numerito2: "))

def multiplicar(a, b):
    if b == 0:
        return 0

    return a + multiplicar(a, b - 1)
    
print(multiplicar(a,b))