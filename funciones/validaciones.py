def validar_numero(min: int, max: int) -> int:
    """_summary_ Esta funcion valida que la eleccion del usuario no supere cierto maximo y minimo.

    Args:
        min (int): _description_
        max (int): _description_

    Returns:
        int: _description_
    """
    numero_a_validar = input(f"Elija la opcion que desea realizar entre el {min} y {max}: ")

    if not numero_a_validar or not numero_a_validar.isdigit() or int(numero_a_validar) < min and int(numero_a_validar) > max:
        return validar_numero()
    
    return int(numero_a_validar)