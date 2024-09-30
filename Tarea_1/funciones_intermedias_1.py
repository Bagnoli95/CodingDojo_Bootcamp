# 1. Actualizar valores en diccionarios y listas
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

matriz[1][0] = 6
print(f"Ejercicio 1 - Resultado 1: {matriz}")
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(f"Ejercicio 1 - Resultado 2: {cantantes}")
ciudades["México"][2] = "Monterrey"
print(f"Ejercicio 1 - Resultado 3: {ciudades}")
coordenadas[0]["latitud"] = 9.9355431
print(f"Ejercicio 1 - Resultado 4: {coordenadas}")

# 2. Iterar a través de una lista de diccionarios
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(listaCantantes):
    for n in listaCantantes:
        nombre = n["nombre"]
        pais = n["pais"]
        print(f"nombre - {nombre}, pais - {pais}")

iterarDiccionario(cantantes)

# 3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for n in lista:
        nombre = n[llave]
        print(nombre)

iterarDiccionario2("pais", cantantes)

# 4. Iterar a través de un diccionario con valores de lista
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(llave, diccionario):
    total = len(diccionario[llave])
    mayuscula = llave.upper()
    print(f"{total} {mayuscula}")
    for n in diccionario[llave]:
        print(n)
    
imprimirInformacion("comidas", costa_rica)
