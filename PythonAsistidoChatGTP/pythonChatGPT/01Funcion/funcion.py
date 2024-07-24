def division(numero1, numero2):
    """
    Realiza la división de dos números y maneja la división por cero.

    Args:
        numero1 (float): El numerador.
        numero2 (float): El denominador.

    Returns:
        float: El resultado de la división si es exitosa.
        str: Un mensaje de error si ocurre una división por cero.
    """
    try:
        return numero1 / numero2
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."


def obtener_numero(mensaje):
    """
    Solicita un número al usuario, manejando errores de entrada.

    Args:
        mensaje (str): El mensaje que se muestra al usuario para solicitar el número.

    Returns:
        float: El número ingresado por el usuario.
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debes ingresar un valor numérico.")


def main():
    """
    Función principal que ejecuta el flujo del programa.

    Solicita dos números al usuario, realiza la división y muestra el resultado.
    """
    numero1 = obtener_numero("Ingresa un número: ")
    numero2 = obtener_numero("Ingresa otro número: ")
    resultado = division(numero1, numero2)
    print("El resultado es:", resultado)


if __name__ == "__main__":
    main()
