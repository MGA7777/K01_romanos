def convertir_a_romano(numero):
    if type(numero) != int:
        return f"Error: Debes introducir un número entero"
    if not 0 < numero < 4000:
        return f"Error: El número debe estar entre 0 y 3999 ({numero})"
    return "TODO: Convertir a romano"


# if not isinstance(numero, int):
#   return "Error: Debe introducir un número entero ({numero})"  
# return "TODO: Convrtir a romano"

print (convertir_a_romano (56))
print (convertir_a_romano (0))
print (convertir_a_romano (4000))
print (convertir_a_romano (-7))
print (convertir_a_romano ("doce"))
print (convertir_a_romano (1))
print (convertir_a_romano (3999))