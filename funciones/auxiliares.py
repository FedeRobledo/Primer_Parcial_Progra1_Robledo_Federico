def mostrar_el_menu() -> None:
    menu = """
    Menú:

    1. Mostrar las existencias de vehiculos en cada Garage
    2. Calcular la cantidad total de unidades almacenadas.
    3. Datos completos del garaje que almacena menos unidades de vehículos.
    4. Máxima cantidad de unidades que almacena el garaje con más unidades.
    5. Obtener recaudación: para ello deberás crear una función que calcule la recaudación de cada garaje, teniendo en cuenta su precio unitario y cantidad de unidades almacenadas en cada garaje.
    6. Cantidad de garajes que hayan almacenado 6 o más unidades de vehículos.
    7. Porcentaje de unidades de cada marca de vehículo sobre el total de vehículos almacenados entre todos los garajes de la sede matriz. Además mostrar todos los datos del garaje con el máximo porcentaje de vehículos almacenados.
    8. Generar un informe con la recaudación de cada garaje, ordenada de mayor a menor.
    9. Salir

    """
    print(menu)

def transformar_matriz(matriz_concesionaria: list[list]) -> list[list]:
    """_summary_ Devuelve la matriz ordenada de forma tal de ser compatible con la funcion mostrar_matriz_texto_tabla

    Args:
        matriz_concesionaria (list[list]): _description_ Matriz original

    Returns:
        list[list]: _description_ Matriz transformada para poder mostrarse
    """

    matriz_ordenada = []
    cantidad_filas = len(matriz_concesionaria[0])
    cantidad_columnas = len(matriz_concesionaria)

    for indice_fila in range(cantidad_filas):
        matriz_ordenada.append([])
        for indice_columna in range(cantidad_columnas + 1):
            if indice_columna == 0:
                columna = indice_columna + indice_fila
            elif indice_columna == 5:
                columna = int(matriz_concesionaria[2][indice_fila]) * \
                    int(matriz_concesionaria[3][indice_fila])
            else:
                columna = matriz_concesionaria[indice_columna - 1][indice_fila]
            
            matriz_ordenada[indice_fila].append(columna)
    
    return matriz_ordenada
