def convertir_a_romano(numero):

    if type(numero) != int:
        return f"Error: Debes introducir un número entero"
    if not 0 < numero < 4000:
        return f"Error: Debes introducir un número comprendido entre 0 y 3999" 
    
    valores = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
              (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
              (5, 'V'), (4, 'IV'), (1, 'I')]
    
    resultado = ""
    
    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    
    return resultado


num1 = int(input("Introduce el primer número: "))
num_rom_1 = (convertir_a_romano(num1))
print ("El numero introducido equivale a ", num_rom_1, "en romano.")
num2 = int(input("Introduce el segundo número: "))
num_rom_2 = (convertir_a_romano(num2))
print ("El numero introducido equivale a ", num_rom_2, "en romano.")

def romano_a_entero(romano):

    """digitos_romanos = ["I", "V", "X", "L", "C", "D", "M"]
    valores = [1, 5, 10, 50, 100, 500, 1000]"""
    digitos_romanos = {
        "I": 1, 
        "V": 5, 
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    if not isinstance (romano, str):
        return "Error: Tiene que ser un número romano en formato cadena de texto"
    
    resultado = 0
    anterior = 0

    for letra in romano:
        if letra not in digitos_romanos:
            return f"Error: {letra} no es un dígito romano válido (I, V, X, L, C, D, M)"
        #i = digitos_romanos.index(letra)
        #resultado = resultado + valores [i]
        #resultado = resultado + digitos_romanos[letra]
        actual = digitos_romanos [letra]
        
        if anterior < actual:
            # Si el numero se 
            if anterior > 0 and len (str(actual)) - len (str(anterior)) > 1:
                return f"ERROR: Resta no posible ({anterior} - {actual})"
            #deshace la suma de la anterior condicion
            resultado = resultado - anterior
            resultado = resultado + (actual - anterior)
        else:
            resultado = resultado + actual
        anterior = actual
        
    return resultado

pruebas = ["A", "", 3, ["X", "X", "I"], "I", "MCXXIII", "IV", "XIV", "XM"]
for valor in pruebas:
    print(romano_a_entero(valor))









