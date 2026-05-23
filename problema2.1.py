# ==============================================================================
# Fase 5 - Evaluación Final POA - Problema 2
# Solución de programación en Python
# ==============================================================================

# Definición de la matriz con el numero de productos solicitado
# Formato: [Nombre del Producto, Categoría, Precio Base] 
menu = [
    ["Hamburguesa Sencilla", "Comidas Rápidas", 15000.0],
    ["Pizzamiliar", "Comidas Rápidas", 45000.0],
    ["Ensalada César", "Saludable", 20000.0],
    ["Jugo Natural", "Bebidas", 5000.0],
    ["Sopa de Tomate", "Saludable", 12000.0],
    ["Cerveza Artesanal", "Bebidas", 18000.0],
    ["Papas Fritas", "Comidas Rápidas", 8000.0]
]

# Módulo/Función para calcular el precio final 
def calcular_precio_final(categoria_producto, precio_base, categoria_objetivo, umbral_precio):
    """
    Calcula el precio final aplicando un 15% de descuento si cumple la lógica de negocio.
    """
    # Lógica de negocio: 15% descuento si la categoría coincide y precio > umbral 
    if categoria_producto == categoria_objetivo and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
        return precio_final
    else:
        # Mantiene el precio base si no se cumplen las condiciones 
        return precio_base

# Función principal para ejecutar el programa
def principal():
    # Define la categoría objetivo y el umbral definido para la promoción 
    categoria_promocion = "Comidas Rápidas"
    umbral_descuento = 10000.0

    print("=" * 60)
    print(" " * 15 + "REPORTE DE PRECIOS DEL MENÚ")
    print("=" * 60)
    print(f"Promoción: 15% de descuento en la categoría '{categoria_promocion}'")
    print(f"Aplica solo para productos con precio base mayor a ${umbral_descuento}")
    print("-" * 60)

    # Estructura de repetición (bucle) para recorrer la matriz de productos
    for producto in menu:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]

        # Llamado a la función que optimiza la solución 
        precio_final = calcular_precio_final(categoria, precio_base, categoria_promocion, umbral_descuento)

        # Salida de datos en consola 
        print(f"Producto: {nombre:<20} | Precio Base: ${precio_base:<8.2f} | Precio Final: ${precio_final:<8.2f}")

    print("=" * 60)

# Punto de entrada del programa
if __name__ == "__main__":
    principal()

    # Esta línea pausa la consola para que no se cierre sola
    input("\nPresiona Enter para salir...")