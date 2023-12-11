# Jose Alfonzo 17-10012
from unittest import TestCase
from Pregunta4Main import *
class Tests(TestCase):
    def test(self):
        self.assertEqual(simplificar("CLASS A f g"), "Clase A con los metodos {'f': 'A', 'g': 'A'}")
        self.assertEqual(simplificar("CLASS B : A f h"), "Clase B con los metodos {'f': 'B', 'g': 'A', 'h': 'B'}")
        self.assertEqual(simplificar("DESCRIBIR A"), "f -> A :: f\ng -> A :: g")
        self.assertEqual(simplificar("DESCRIBIR B"), "f -> B :: f\ng -> A :: g\nh -> B :: h")
        self.assertEqual(simplificar("CLASS D : C f h"), "La clase C no existe")
        self.assertEqual(simplificar("Hola"), "Accion invalida, debe ser una de las siguientes: 'CLASS' 'DESCRIBIR' 'SALIR'")
        self.assertEqual(simplificar(""), "No se ingreso ninguna accion")
        self.assertEqual(simplificar("CLASS X f f c a"), "Hay definiciones repetidas en la lista de nombres de metodos")
        self.assertEqual(simplificar("CLASS A f g"), "El nombre de la nueva clase: A :ya existe")
        self.assertEqual(simplificar("DESCRIBIR Z"), "La clase Z no existe")
        with self.assertRaises(SystemExit):
            simplificar("SALIR")