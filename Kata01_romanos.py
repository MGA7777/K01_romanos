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


"""num1 = int(input("Introduce el primer número: "))
num_rom_1 = (convertir_a_romano(num1))
print ("El numero introducido equivale a ", num_rom_1, "en romano.")
num2 = int(input("Introduce el segundo número: "))
num_rom_2 = (convertir_a_romano(num2))
print ("El numero introducido equivale a ", num_rom_2, "en romano.")"""

import re
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
        raise TypeError ("Error: Tiene que ser un número romano en formato cadena de texto")

    resultado = 0
    anterior = 0
    super_anterior = 0

    # letra_igual = 0 Forma fácil de encontrar 3 letras seguidas. Irá con todo lo que esta entre 59-64

    for letra in romano:  
        if letra not in digitos_romanos:
            raise ValueError (f"Error: {letra} no es un dígito romano válido (I, V, X, L, C, D, M)")
            # Estas excepciones en realidad son para los programadores. No la ven los usuarios

        patron = r"(.)\1{3,}"
        if re.search(patron, romano):
            raise ValueError (f"Error: Un número romano no puede contener 3 letras seguidas iguales {letra}")
        # if actual == anterior:
        #     letra_igual +=1
        # else:
        #     letra_igual = 0
        # if letra_igual == 3:
        #     return "Error: Un número romano no puede contener 3 letras seguidas iguales {letra}"

        actual = digitos_romanos [letra]
        if anterior < actual:
            # Si el anterior es 2 unidades más pequeño, no se debe restar
            if anterior > 0 and len (str(actual)) - len (str(anterior)) > 1:
                raise ValueError (f"ERROR: Resta no posible ({anterior} - {actual})")
            
            if anterior > 0 and actual > super_anterior > 0:
                raise ValueError (f"Error: 2 restas consecutivas")
            # Deshace la suma de la anterior condicion
            resultado = resultado - anterior
            resultado = resultado + (actual - anterior)
 
        else:
            resultado = resultado + actual

        super_anterior = anterior
        anterior = actual
        
    return resultado

# Podemos hacer las pruebas de forma automática, le decimos a python que voy a 
# hacer un pgrama que prueba mi programa. De tal forma que si rompo mi programa, 
# al lanzar la bateria de prueba me avise de forma directa.
# Las pruebas las quitamos y nos abrimos un fichero nuevo que sea test_romanos
# le decimos que traspase este programa allí


"""pruebas = ["A", "", 3, ["X", "X"], "I", "MCXXIII", "IV", "XIV", "XM", "MMMMX", "MCXXX", "VX", "LC"]
for valor in pruebas:
    try:
        print(romano_a_entero(valor))
    except TypeError:
        print("Uy!, el tipo no es válido")
    except ValueError:
        print("Va a ser que esa cadena no es un número romano")
    except Exception as ex:
        print("Hey!", ex)
        # Le ayudamos a que no se rompa el programa con las excepciones y pueda continuar, simplemente haciendo un 
        # try y except con las pruebas, si además le metemos en except (Exception as ex) que nos printe la excepcion , 
        # nos dice el error por el que no funciona. Incluso podemos hacer una excepcion con un print diferente según 
        # el tipo de error. """









