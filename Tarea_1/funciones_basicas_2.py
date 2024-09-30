# 1 - multiplica_por_dos
def multiplica_por_dos(numIn):
    listaResul = []
    for n in range(0, numIn +1):
        listaResul.append(n * 2)
    print(listaResul)
    
multiplica_por_dos(5)

# 2 - suma_y_resta
def suma_y_resta(listaIn):
    print(listaIn[0] + listaIn[1])
    return (listaIn[0] - listaIn[1])

print(f"Devuelve: {suma_y_resta([5,4])}")

# 3 - sumatoria_menos_longitud
def sumatoria_menos_longitud(listaIn):
    suma = 0
    for n in listaIn:
        suma += n
    resta = suma - len(listaIn)
    return resta

print(f"Devuelve: {sumatoria_menos_longitud([1, 2, 3, 4])}")

# 4 - valores_multiplicados_segundo
def valores_multiplicados_segundo(listaIn):
    resultado = []
    if len(listaIn) >= 2:
        for n in listaIn:
            resultado.append(n * listaIn[1])
    return resultado
print(f"Devuelve: {valores_multiplicados_segundo([1, 3, 5, 7])}")

# 5 - valor_multiplicado_longitud
def valor_multiplicado_longitud(valor, longitud):
    lista = []
    for n in range(0, longitud):
        lista.append(valor * longitud)
    return lista

print(f"Devuelve: {valor_multiplicado_longitud(7, 5)}")