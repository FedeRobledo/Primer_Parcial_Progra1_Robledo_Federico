from funciones import mostrar_el_menu, validar_numero, mostrar_existencias, calcular_total_vehiculos,\
 calcular_garage_menos_unidades, calcular_mayor_cant_unidades, calcular_recaudacion_total, cantidad_garages_seis_o_mas
from UTN_Heroes_Dataset.utn_pp import clear_console

def concesionaria_app(matriz_concesionaria: list[list]):

    while True:
        mostrar_el_menu()
        numero_validado = validar_numero(1, 9)

        match numero_validado:
            case 1:
                mostrar_existencias(matriz_concesionaria)
            case 2:
                calcular_total_vehiculos(matriz_concesionaria[2])
            case 3:
                calcular_garage_menos_unidades(matriz_concesionaria)
            case 4:
                calcular_mayor_cant_unidades(matriz_concesionaria)
            case 5:
                calcular_recaudacion_total(matriz_concesionaria)
            case 6:
                cantidad_garages_seis_o_mas(matriz_concesionaria)
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                break
            case _:
                continue
    clear_console()