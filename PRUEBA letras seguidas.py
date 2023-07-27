import re
def validar_numero_romano(numero):
    patron = r"(.)\1{3,}"
    if re.search(patron, numero):
        return False
    else:
        return True

numero_romano = "MMMMCC"
if validar_numero_romano(numero_romano):
    print("El número romano es válido.")
else:
    print("El número romano no es válido.")