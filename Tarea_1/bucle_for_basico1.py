# Básico: imprime todos los números enteros del 0 al 100.
for n in range(0, 101):
    print(n)
    
# Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
for n in range(2, 501, 2):
    print(n)
    
"""Contando Vanilla Ice: imprime los números enteros del 1 al 100.
    Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
"""
for n in range(0, 101):
    if (n % 5 == 0):
        print("ice ice")
    if (n % 10 == 0):
        print("baby")

# Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
sum = 0
for n in range(0, 500001, 2):
    sum += n
print("El resultado es: ", sum)

# Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
for n in range(2024, 0, -3):
    print(n)
    
"""Contador dinámico: establece tres variables: numInicial, numFinal y multiplo.
    Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo.
    Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas)."""
numInicial = 3
numFinal = 10
multiplo = 2
for n in range(numInicial, numFinal + 1):
    if (n%multiplo == 0):
        print(n)



