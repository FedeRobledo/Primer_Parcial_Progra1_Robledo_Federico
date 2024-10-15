from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla
from .auxiliares import transformar_matriz

def mostrar_existencias(matriz_concesionaria: list[list]) -> None:
    """_summary_ Esta funcion muestra todos los datos de los vehiculos que hay en los 20 garages.

    Args:
        matriz_concesionaria (list[list]): _description_
    """
    matriz_transformada = transformar_matriz(matriz_concesionaria)
    mostrar_matriz_texto_tabla(matriz_transformada, ['Indice Garage', 'Marca', 'Modelo', 'Cantidad', 'Precio', 'Ganancia'])


def calcular_total_vehiculos(lista_cantidades: list) -> None:
    """_summary_ Esta funcion permite sumar toda la cantidad de vehiculos existentes por garage.

    Args:
        lista_cantidades (list): _description_
    """

    cantidad_filas = len(lista_cantidades)
    cantidad_de_vehiculos = 0

    for indice_cantidad_garage in range(cantidad_filas):
        cantidad_de_vehiculos += lista_cantidades[indice_cantidad_garage]
    
    print(f"La cantidad total de vehiculos sumando los que se encuentran en cada garage es de {cantidad_de_vehiculos} unidades")
        