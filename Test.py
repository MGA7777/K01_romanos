import unittest
from Clase_romanos import RomanNumber

class RomanosTest(unittest.TestCase):
    def test_crear_numero_romano_desde_entero(self):
        numero = RomanNumber(1)
        self.assertEqual (numero.valor, 1)
        self.assertEqual (numero.cadena, "I")
        numero = RomanNumber(1745)
        self.assertEqual (numero.valor, 1745)
        self.assertEqual (numero.cadena, "MDCCXLV")
    
    def test_crear_numero_romano_desde_cadena(self):
        cadena = RomanNumber("I")
        self.assertEqual (cadena.cadena, "I")
        self.assertEqual (cadena.valor, 1)
        cadena = RomanNumber ("MDCCXLV")
        self.assertEqual (cadena.cadena, "MDCCXLV" )
        self.assertEqual (cadena.valor, 1745)

    def test_romano_con_representacion_cadena_str(self):
        numero = RomanNumber (1745)
        self.assertEqual(str(numero), "MDCCXLV")

    def test_comprobar_igualdad(self):
        uno = RomanNumber (1)
        otrouno = RomanNumber (1)
        dos = RomanNumber (2)
        self.assertEqual (uno, otrouno)
        self.assertNotEqual (uno, dos)
        self.assertNotEqual (otrouno, dos)
    
    def test_comprobar_suma(self):
        tres = RomanNumber (3)
        cuatro = RomanNumber (4)
        self.assertEqual (tres+cuatro, 7)
        self.assertEqual (tres+7, 10)
        self.assertEqual (tres+"VII", 10)
        self.assertEqual ("VII"+tres, 10)

unittest.main()

