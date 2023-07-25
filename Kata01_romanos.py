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








