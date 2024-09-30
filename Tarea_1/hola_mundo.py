# 1. Imprime "Hola, mundo"
print( "Hola, mundo" )

# 2. Imprime "Hola, Valeria" con el nombre en una variable
nombre = "Arturo"
print( "Hola, ",  nombre ) # con una coma
print( "Hola, " + nombre ) # con un +

# 3. Imprimir "Hola 156!" con el número en una variable
numero = 156
print( "Hola, ", numero ) # con una coma
print( "Hola, " + str(numero) ) # con un + -- este debería arrojar un error!, corrígelo con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables
comida1 = "pizzas"
comida2 = "milanesas"
print( "Me encanta comer {} y {}".format(comida1, comida2) ) # con .format()
print( f"Me encanta comer {comida1} y {comida2}" ) # con una cadena f



print(comida1 + comida2)
print(comida1, comida2)
# print(comida1 . comida2)
num1 = '5'
num2 = 4
# print(num1 + num2)

lista_prueba = [2, 4, 6]
print(lista_prueba)
lista_prueba.append(8)
print(lista_prueba)
print(lista_prueba[2])
