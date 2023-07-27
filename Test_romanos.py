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
        self.assertEqual(romano_a_entero("IV"), 4)
        self.assertEqual(romano_a_entero("VI"), 6)
        self.assertEqual(romano_a_entero("MMMM"), 4000)

unittest.main()