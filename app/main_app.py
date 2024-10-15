from funciones import mostrar_el_menu, validar_numero, mostrar_existencias, calcular_total_vehiculos
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
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
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