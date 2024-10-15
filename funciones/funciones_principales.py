from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla
from .auxiliares import transformar_matriz, obtener_total_vehiculos


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

    total_vehiculos = obtener_total_vehiculos(lista_cantidades)
    
    print(f"\n La cantidad total de vehiculos sumando los que se encuentran en cada garage es de {total_vehiculos} unidades\n")


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


def cantidad_garages_seis_o_mas(matriz_concesionaria: list[list]) -> None:
    """_summary_  Devuelve la cantidad de garages que tienen 6 o mas vehiculos

    Args:
        matriz_concesionaria (list[list]): _description_
    """

    matriz_transformada = transformar_matriz(matriz_concesionaria)
    cantidad_garages = 0
    

    for indice_fila in range(len(matriz_transformada)):
        if matriz_transformada[indice_fila][3] >= 6:
            cantidad_garages += 1
    
    print(f"\n La cantidad de garages con seis o mas vehiculos es de {cantidad_garages}\n ")


## INCOMPLETO
def mostrar_porcentajes_y_garage_mas_importante(matriz_concesionaria: list[list]) -> None:
    """_summary_ Muestra el porcentaje de unidades de cada marca de vehículo sobre el total de vehículos almacenados 
    entre todos los garajes de la sede matriz. Además muestra todos los datos del garaje con el máximo porcentaje de 
    vehículos almacenados.

    Args:
        matriz_concesionaria (list[list]): _description_
    """

    total_vehiculos = obtener_total_vehiculos(matriz_concesionaria[2])

    lista_marcas = matriz_concesionaria[0]

    marcas = []

    for marca in lista_marcas:
        if marca not in marcas:
            marcas.append(marca)

    matriz_marca_total = [
        marcas, []
    ]

    for marca in marcas:
        total_marca = 0
        for indice in range(len(matriz_concesionaria[0])):
            if matriz_concesionaria[0][indice] == marca:
                total_marca += matriz_concesionaria[2][indice]
        matriz_marca_total[1].append(total_marca)


    for indice in range(len(matriz_marca_total[0])):
        print(f"El porcentaje de {matriz_marca_total[0][indice]} es de {(matriz_marca_total[1][indice] / 83 * 100)}")
