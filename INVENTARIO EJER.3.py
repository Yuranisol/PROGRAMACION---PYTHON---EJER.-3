# Universidad Nacional Abierta y a Distancia - UNAD
# Curso: Fundamentos de Programación - Código: 213022
# Fase 5 - Evaluación Final POA
# Problema 3: Auditoría de Inventario

# MATRIZ DEL INVENTARIO

inventario = [
    ["A01", "Cuadernos", 5, 10],
    ["A02", "Lápices", 20, 15],
    ["A03", "Borradores", 3, 8],
    ["A04", "Marcadores", 12, 12],
    ["A05", "Colores", 2, 6]
]

# FUNCIÓN PARA CALCULAR LA CANTIDAD A PEDIR

def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        cantidad_pedir = 0

    return cantidad_pedir


# MOSTRAR RESULTADOS

print("LISTA DE PEDIDOS")
print("-----------------------")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad = calcular_pedido(stock_actual, stock_minimo)

    print("Artículo:", nombre)
    print("Cantidad a pedir:", cantidad)
    print("-----------------------")
    