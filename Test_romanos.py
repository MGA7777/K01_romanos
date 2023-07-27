import unittest
from Kata01_romanos import *

class RomanosTest(unittest.TestCase):

    def test_unidades(self):
        self.assertEqual(romano_a_entero("I"), 1)
        self.assertEqual(romano_a_entero("V"), 5)
        self.assertEqual(romano_a_entero("X"), 10)
        self.assertEqual(romano_a_entero("L"), 50)
        self.assertEqual(romano_a_entero("C"), 100)
        self.assertEqual(romano_a_entero("D"), 500)
        self.assertEqual(romano_a_entero("M"), 1000)

    def test_numeros_basicos(self):
        self.assertEqual(romano_a_entero("IV"), 4)
        self.assertEqual(romano_a_entero("VI"), 6)
        self.assertEqual(romano_a_entero("MCXXIII"), 1123)
        self.assertEqual(romano_a_entero("LVI"), 56)
        self.assertEqual(romano_a_entero("XL"), 40)
        self.assertEqual(romano_a_entero("CCV"), 205)
    
    def test_no_resta_mas_un_orden_magnitud(self):
        self.assertRaises(ValueError, romano_a_entero, "XM")
        self.assertRaises(ValueError, romano_a_entero, "IC")
        self.assertRaises(ValueError, romano_a_entero, "XC")  # ESTO COMO NO ES UNA EXCEPCION FALLA
    
    def test_no_3letras_seguidas(self):
        self.assertRaises(ValueError, romano_a_entero, "MMMM")
        self.assertRaises(ValueError, romano_a_entero, "MIIII")

    def test_caracteres_validos(self):
        self.assertRaises(ValueError, romano_a_entero, "A")
        self.assertRaises(ValueError, romano_a_entero, "3")

    def test_no_restas_consecutivas(self):
        self.assertRaises(ValueError, romano_a_entero, "IIV")
        self.assertRaises(ValueError, romano_a_entero, "MXXC")
        self.assertRaises(ValueError, romano_a_entero, "IVX")

    def test_no_resta_multiplos5(self):
        self.assertRaises(ValueError, romano_a_entero, "VX")
        self.assertRaises(ValueError, romano_a_entero, "VXX")
        self.assertRaises(ValueError, romano_a_entero, "LC")
        self.assertRaises(ValueError, romano_a_entero, "DM")
    
    def test_otros_casos(self):
         self.assertRaises(ValueError, romano_a_entero, "XIXXIII")
        
unittest.main()