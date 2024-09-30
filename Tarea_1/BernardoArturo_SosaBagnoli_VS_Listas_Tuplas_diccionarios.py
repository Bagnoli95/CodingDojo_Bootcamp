# 1 - Carga de Datos
ventas = [
    {"fecha":"2024-01-01", "producto":"Etiqueta pequeña", "cantidad":200, "precio":1500},
    {"fecha":"2024-01-02", "producto":"Etiqueta mediana", "cantidad":150, "precio":2200},
    {"fecha":"2024-01-03", "producto":"Etiqueta grande", "cantidad":120, "precio":5500},
    {"fecha":"2024-01-04", "producto":"Insumo hojas", "cantidad":32, "precio":24500},
    {"fecha":"2024-01-05", "producto":"Insumo tintas", "cantidad":8, "precio":350000}
]
print(f'1 - Lista de Ventas: {ventas}')

# 2 - Cálculo de Ingresos Totales
def ingresosTotales(listaDiccionario):
    montoTotalVentas = 0
    for n in listaDiccionario:
        montoTotalVentas += n["cantidad"] * n["precio"]
    return montoTotalVentas
print(f'2 - Los ingresos totales son: {ingresosTotales(ventas)}')

# 3 - Análisis del Producto Más Vendido
def productoMasVendido(listaVentas):
    ventas_por_producto = {'clave': 'n', 'valor': 0}
    for n in listaVentas:
        if n["cantidad"] > ventas_por_producto["valor"]:
            ventas_por_producto["clave"] = n["producto"]
            ventas_por_producto["valor"] = n["cantidad"]
    return ventas_por_producto
print(f'3 - Producto más vendido: {productoMasVendido(ventas)}')

# 4 - Promedio de Precio por Producto:
def promedioPrecioPorProducto(listaVentas):
    lista_precios_por_productos = []
    for n in listaVentas:
        precios_por_producto = {
            'clave': n["producto"], 
            'valor': {
                'ventaTotal': n['precio'] * n['cantidad'], 
                'cantidadTotal': n['cantidad']
            }
        }
        print(precios_por_producto)
        lista_precios_por_productos.append(precios_por_producto)
    return lista_precios_por_productos
print(f'4 - Promedio de precios por Productos: {promedioPrecioPorProducto(ventas)}')

# 5 - Ventas por Día
def ingresosPorDia(listaVentas):
    ingresos_por_dia = {}
    for venta in listaVentas:
        fecha = venta["fecha"]
        ingreso_total = venta["precio"] * venta["cantidad"]
        if fecha in ingresos_por_dia:
            ingresos_por_dia[fecha] += ingreso_total
        else:
            ingresos_por_dia[fecha] = ingreso_total
            
    return ingresos_por_dia
print(f'5 - Ventas por dia: {ingresosPorDia(ventas)}')

# 6 - Representación de Datos
def resumenVentas(listaVentas):
    resumen_ventas = {}
    for venta in listaVentas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        ingresos = venta["precio"] * cantidad
        if producto not in resumen_ventas:
            resumen_ventas[producto] = {
                'cantidad_total': 0,
                'ingresos_totales': 0,
                'precio_promedio': 0
            }
        # Actualizamos la cantidad total y los ingresos totales
        resumen_ventas[producto]['cantidad_total'] += cantidad
        resumen_ventas[producto]['ingresos_totales'] += ingresos
    # Calcular el precio promedio para cada producto
    for producto, datos in resumen_ventas.items():
        datos['precio_promedio'] = datos['ingresos_totales'] / datos['cantidad_total']
    return resumen_ventas
print(f'6 - Representación de Datos: {resumenVentas(ventas)}')

