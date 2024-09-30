"""
Ejercicio para reconocer variables => COMENTARIO DE VARIAS LINEAS
"""

# declaración de variable => COMENTARIO DE UNA LINEA
numero1 = 70        # Tipos de datos primitivos => Número entero
numero2 = 3.14      # Tipos de datos primitivos => Número Flotante/Decimal
booleano = False    # Tipos de datos primitivos => Boolean
cadena = 'Hola Mundo'   # Tipos de datos primitivos => Strings/Cadenas

# TIPOS DE DATOS COMPUESTOS
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate']        # LISTAS - INICIALIZAR
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False}    # DICCIONARIOS - INICIALIZAR
frutas = ('guayaba', 'fresa', 'papaya')                                             # TUPLAS - INICIALIZAR
print(type(frutas))                         # IMPRIMIR TIPO DE VARIABLE
print(ingredientes_pastel[2])               # LISTAS - ACCESAR VALOR
ingredientes_pastel.append('Mantequilla')   # LISTAS - AGREGAR VALOR
print(persona['nombre'])                    # DICCIONARIOS - ACCESAR VALOR
persona['nombre'] = 'Kevin'                 # DICCIONARIOS - CAMBIAR VALOR
persona['color_ojos'] = 'cafe'              # DICCIONARIOS - AGREGAR VALOR
print(frutas[2])                            # TUPLAS - ACCESAR VALOR

if numero1 > 45:                            # CONDICIONAL - IF - ELSE
    print("Numero mayor")
else:
    print("Numero menor")

if len(cadena) < 5:                         # CONDICIONAL - IF - ELSE IF - ELSE
    print("Cadena corta")
elif len(cadena) > 15:
    print("Cadena larga")
else:
    print("Cadena perfecta")

for x in range(8):                          # BUCLE FOR
    print(x)
for x in range(2,8):                        # BUCLE FOR
    print(x)
for x in range(2,8,2):                      # BUCLE FOR
    print(x)
x = 0                                       # BUCLE WHILE
while(x < 8):
    print(x)
    x += 1

ingredientes_pastel.pop()                   # LISTA - BORRAR ULTIMO VALOR
ingredientes_pastel.pop(1)                  # LISTA - BORRAR VALOR SEGUN POSICION

print(persona)                              # DICCIONARIO - ACCESAR VALOR
persona.pop('color_ojos')                   # DICCIONARIO - BORRAR VALOR
print(persona)                              # DICCIONARIO - ACCESAR VALOR

for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina':
        continue
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        break

def imprime_hola_10_veces():
    for numero in range(10):
        print('Hola')

imprime_hola_10_veces()

def imprime_hola_n_veces(n):
    for numero in range(n):
        print('Hola')

imprime_hola_n_veces(5)

def imprime_hola_n_o_diez_veces(n = 10):
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces()
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

# print(numero3)
# numero3 = 86
# frutas[0] = 'naranja'
# print(persona['hobbies'])
# print(ingredientes_pastel[11])
#   print(booleano)
# frutas.append('manzana')
# frutas.pop(1)