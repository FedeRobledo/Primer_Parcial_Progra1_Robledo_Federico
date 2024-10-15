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
    
    print(f"\n La cantidad total de vehiculos sumando los que se encuentran en cada garage es de {cantidad_de_vehiculos} unidades\n")


def calcular_garage_menos_unidades(matriz_concesionaria: list[list]) -> None:
    """_summary_ Esta funcion permite obtener el garage con menos unidades.

    Args:
        matriz_concesionaria (list:[list]): _description_
    """
    matriz_transformada = transformar_matriz(matriz_concesionaria)

    indice_minimo = None

    for indice_fila in range(len(matriz_transformada)):
        if indice_minimo == None or matriz_transformada[indice_fila][3] < matriz_transformada[indice_minimo][3]:
            indice_minimo = indice_fila

    print(f"""
        El garage que tiene menos vehiculos es el número {matriz_transformada[indice_minimo][0]}
        Tiene un total de {matriz_transformada[indice_minimo][3]} vehiculos de la marca {matriz_transformada[indice_minimo][1]}
        modelo {matriz_transformada[indice_minimo][2]} con un valor de {matriz_transformada[indice_minimo][4]}$ por unidad
        """)


# Se que son mas de uno y que podria mostrarlos con su detalle pero prefiero avanzar, completarlo luego.
def calcular_mayor_cant_unidades(matriz_concesionaria: list[list]) -> None:
    """_summary_ Permite saber cuanta es la mayor cantidad de unidades que tiene el garage con mas unidades

    Args:
        matriz_concesionaria (list[list]): _description_
    """

    matriz_transformada = transformar_matriz(matriz_concesionaria)
    indice_maximo = None

    for indice_fila in range(len(matriz_transformada)):
        if indice_maximo == None or matriz_transformada[indice_fila][3] > matriz_transformada[indice_maximo][3]:
            indice_maximo = indice_fila
    
    print(f"El garage que mas vehiculos tiene cuenta con un total de {matriz_transformada[indice_maximo][3]} unidades.")

def calcular_recaudacion_total(matriz_concesionaria: list[list]) -> None:
    """_summary_ Suma la recaudacion de cada garage y luego un resumen con la recaudacion total

    Args:
        matriz_concesionaria (list[list]): _description_
    """
    matriz_transformada = transformar_matriz(matriz_concesionaria)

    total = 0

    for filas in range(len(matriz_concesionaria[0])):
        total += matriz_transformada[filas][4]
    
    print(f"\nTOTAL DE RECAUDACON: {total}\n")
