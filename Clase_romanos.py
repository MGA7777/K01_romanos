import re
class RomanNumber:
    def __init__(self, entrada):
        if isinstance(entrada, int):
            self.valor = entrada
            self.cadena = self.convertir_a_romano()   
        elif isinstance(entrada, str):
            self.cadena = entrada
            self.valor = self.romano_a_entero()  
        else:
            raise TypeError("Solo acepto enteros o cadenas")
    
    def convertir_a_romano(self):
        numero = self.valor
        if type(numero) != int:
            raise ValueError ("Error: Debes introducir un número entero")
        if not 0 < numero < 4000:
            raise ValueError ("Error: Debes introducir un número comprendido entre 0 y 3999")
    
        valores = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
                (5, 'V'), (4, 'IV'), (1, 'I')]
    
        resultado = ""
    
        for valor, simbolo in valores:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
    
        return resultado
    

    def romano_a_entero(self):
        romano = self.cadena
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

        for letra in romano:  
            if letra not in digitos_romanos:
                raise ValueError (f"Error: {letra} no es un dígito romano válido (I, V, X, L, C, D, M)")
                
            patron = r"(.)\1{3,}"
            if re.search(patron, romano):
                raise ValueError (f"Error: Un número romano no puede contener 3 letras seguidas iguales {letra}")

            actual = digitos_romanos [letra]
            if anterior < actual:
                if anterior > 0 and len (str(actual)) - len (str(anterior)) > 1:
                    raise ValueError (f"ERROR: Resta no posible ({anterior} - {actual})")
                
                if anterior > 0 and actual > super_anterior > 0:
                    raise ValueError (f"Error: 2 restas consecutivas")
                
                if anterior == "V" or anterior == "D" or anterior == "L":
                    raise ValueError (f"Error: Los simbolos multiplos de 5 solo pueden sumar no restar")
            
                resultado = resultado - anterior
                resultado = resultado + (actual - anterior)
    
            else:
                resultado = resultado + actual

            super_anterior = anterior
            anterior = actual
            
        return resultado
    

    def __str__(self): #
        return self.cadena

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, otro):  #Igual
        return self.cadena == otro or self.valor == otro
    
    def __ne__(self, otro): # No igual
        if isinstance(otro, RomanNumber):
            print ("Es un Roman Number")
            return self.valor != otro.valor
        if isinstance(otro, int):
            print ("Es un int")
            return self.valor != otro
        if isinstance (otro, str):
            print ("Es un str")
            return self.cadena != otro
        raise ValueError("Solo puedo comparar numeros romanos, enteros o cadenas")
    
    def __lt__(self, otro): # Menor que
        if isinstance(otro, RomanNumber):
            return self.valor < otro.valor
        if isinstance(otro, int):
            return self.valor < otro
        if isinstance (otro, str):
            return self.cadena < otro
        raise ValueError("Solo puedo comparar numeros romanos, enteros o cadenas")
    
    def __gt__(self, otro): # Mayor que
        if isinstance(otro, RomanNumber):
            return self.valor > otro.valor
        if isinstance(otro, int):
            return self.valor > otro
        if isinstance (otro, str):
            return self.cadena > otro
        raise ValueError("Solo puedo comparar numeros romanos, enteros o cadenas")
    
    def __add__(self, otro): # SUMA
        if isinstance(otro, RomanNumber):
            return self.valor + otro.valor
        if isinstance(otro, int):
            return self.valor + otro
        if isinstance (otro, str):
            return self.valor + RomanNumber(otro).valor
        raise ValueError("Solo puedo comparar numeros romanos, enteros o cadenas")
    # Esto podría sumar perfectamente a + 56, pero no 56 + a, para que no tenga problema
    # Habría qu añadir una r delante
    def __radd__(self, otro):
        return self.__add__(otro)
    
    def __sub__(self, otro):  # RESTA
        if isinstance(otro, RomanNumber):
            return self.valor - otro.valor
        if isinstance(otro, int):
            return self.valor - otro
        if isinstance (otro, str):
            return self.valor - RomanNumber(otro).valor
        raise ValueError("Solo puedo comparar numeros romanos, enteros o cadenas")
    def __rsub__(self, otro):
        if isinstance(otro, RomanNumber):
            return otro.valor - self.valor
        if isinstance(otro, int):
            return otro - self.valor
        if isinstance(otro, int):
            return RomanNumber(otro).valor - self.valor
        raise ValueError("Solo puedo comparar numeros romanos, enteros o cadenas")
    

    def __add__(self, otro): # SUMA DEVOLVIENDO NÚMERO ROMANO
        if isinstance(otro, RomanNumber):
            return RomanNumber (self.valor + otro.valor)
        if isinstance(otro, int):
            return RomanNumber (self.valor + otro)
        if isinstance (otro, str):
            return (self + RomanNumber(otro))
        raise ValueError("Solo puedo comparar numeros romanos, enteros o cadenas")
    def __radd__(self, otro):
        return self.__add__(otro)
    
    def __sub__(self, otro):  # RESTA DEVOLVIENDO NÚMERO ROMANO
        resta = 0
        if isinstance(otro, RomanNumber):
            resta = self.valor - otro.valor
        elif isinstance(otro, int):
            resta = self.valor - otro
        elif isinstance (otro, str):
            resta = self.valor - RomanNumber(otro).valor
        else: 
            raise ValueError("Solo se restar RomanNumber, int o str")
        
        if resta <=0:
            raise ValueError("Un número romano no puede ser negativo, no puedo hacer la resta")
        else:
            return RomanNumber(resta)
        
    def __rsub__(self, otro):  # RESTA DEVOLVIENDO NÚMERO ROMANO
        resta = 0
        if isinstance(otro, RomanNumber):
            resta = otro.valor - self.valor
        elif isinstance(otro, int):
            resta = otro - self.valor
        elif isinstance (otro, str):
            resta = RomanNumber(otro).valor - self.valor
        else: 
            raise ValueError("Solo se restar RomanNumber, int o str")
        
        if resta <=0:
            raise ValueError("Un número romano no puede ser negativo, no puedo hacer la resta")
        else:
            return RomanNumber(resta)


    




# En una clase los datos se guardan en un atributo
