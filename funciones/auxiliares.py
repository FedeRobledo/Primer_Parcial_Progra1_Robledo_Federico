def mostrar_el_menu() -> None:
    menu = """
    Menú:

    1. Mostrar las existencias de vehiculos en cada Garage

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
            else:
                columna = matriz_concesionaria[indice_columna - 1][indice_fila]
            
            matriz_ordenada[indice_fila].append(columna)
    
    return matriz_ordenada
