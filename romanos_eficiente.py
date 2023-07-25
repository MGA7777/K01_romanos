def convertir_a_romano(numero):
    if type(numero) != int:
        return f"Error: debes introducir un número entero ({numero})"

    # validar el valor del número
    if not (0 < numero < 4000):
        return f"Error: el número debe estar entre 1 y 3999 ({numero})"

    LISTA_EQUIVALENCIAS = [["", "M", "MM", "MMM"],
                           ["", "C", "CC", "CCC", "CD", "D",
                               "DC", "DCC", "DCCC", "CM"],
                           ["", "X", "XX", "XXX", "XL", "L",
                               "LX", "LXX", "LXXX", "XC"],
                           ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]]

    fila = 0
    romano = ''
    for i in range(3, -1, -1):
        punt = numero // 10**i
        numero = numero % 10**i
        romano += LISTA_EQUIVALENCIAS[fila][punt]
        fila += 1

    return romano


print(convertir_a_romano(358))
