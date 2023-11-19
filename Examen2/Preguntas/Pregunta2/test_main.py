# Jose Alfonzo 17-10012 
# Pregunta 2) tests

from unittest import TestCase, expectedFailure
# Importamos nuestras funciones del main
from main import (
    evaluar,
    mostrar,
    prefijo,
    postfijo,
    procesar,
)
# Test nos permite ver los casos de prueba de nuestro programa
class Tests(TestCase):
    # Porbamos tests para ver si nos da bien nuestra funcion evaluar con 1 y 3
    def test_evaluar(self):
        self.assertEqual(evaluar("+", "1", "3"), 4)
        self.assertEqual(evaluar("-", "1", "3"), -2)
        self.assertEqual(evaluar("*", "1", "3"), 3)
        self.assertEqual(evaluar("/", "1", "3"), 0)
    # Porbamos tests para ver si nos da bien nuestra funcion mostrar con 1 y 3
    def test_mostrar(self):
        self.assertEqual(mostrar("+", "1", "3"), "1 + 3")
        self.assertEqual(mostrar("-", "1", "3"), "1 - 3")
        self.assertEqual(mostrar("*", "1", "3"), "1 * 3")
        self.assertEqual(mostrar("/", "1", "3"), "1 / 3")
    # Porbamos tests para ver si nos da bien nuestra funcion prefijo, en donde vamos a probar eval con nuestros 4 operadores y mostrar eso 
    def test_prefijo(self):
        self.assertEqual(prefijo("EVAL", ["+", "9", "4"]), "13")
        self.assertEqual(prefijo("EVAL", ["-", "4", "5"]), "-1")
        self.assertEqual(prefijo("EVAL", ["*", "3", "3"]), "9")
        self.assertEqual(prefijo("EVAL", ["/", "1", "2"]), "0")
        self.assertEqual(prefijo("MOSTRAR", ["+", "9", "4"]), "9 + 4")
        self.assertEqual(prefijo("MOSTRAR", ["-", "4", "5"]), "4 - 5")
        self.assertEqual(prefijo("MOSTRAR", ["*", "3", "3"]), "3 * 3")
        self.assertEqual(prefijo("MOSTRAR", ["/", "1", "2"]), "1 / 2")
     # Porbamos tests para ver si nos da bien nuestra funcion postfijo, en donde vamos a probar eval con nuestros 4 operadores y mostrar eso
    def test_postfijo(self):
        self.assertEqual(postfijo("EVAL", ["7", "3", "+"]), "10")
        self.assertEqual(postfijo("EVAL", ["3", "2", "-"]), "1")
        self.assertEqual(postfijo("EVAL", ["2", "2", "*"]), "4")
        self.assertEqual(postfijo("EVAL", ["1", "1", "/"]), "1") 
        self.assertEqual(postfijo("MOSTRAR", ["7", "3", "+"]), "7 + 3")
        self.assertEqual(postfijo("MOSTRAR", ["3", "2", "-"]), "3 - 2")
        self.assertEqual(postfijo("MOSTRAR", ["2", "2", "*"]), "2 * 2")
        self.assertEqual(postfijo("MOSTRAR", ["1", "1", "/"]), "1 / 1")
    # Porbamos tests para ver si nos da bien nuestra funcion procesar, en donde vamos a probar varios ejemplos
    def test_procesar(self):
        # Ejemplo del parcial con su mostrar adecuado
        self.assertEqual(procesar("EVAL PRE + * + 3 4 5 7"), "42") 
        self.assertEqual(procesar("MOSTRAR PRE + * + 3 4 5 7"), "(3 + 4) * 5 + 7")
        # Ejemplo del parcial con su mostrar adecuado
        self.assertEqual(procesar("EVAL POST 8 3 - 8 4 4 + * +"), "69")
        self.assertEqual(procesar("MOSTRAR POST 8 3 - 8 4 4 + * +"), "8 - 3 + 8 * (4 + 4)")
        # Ejemplo random adicional usando PRE
        self.assertEqual(procesar("EVAL PRE / * + - 9 2 3 5 5"), "10")
        self.assertEqual(procesar("MOSTRAR PRE / * + - 9 2 3 5 5"), "((9 - 2 + 3) * 5) / 5")
        # Ejemplo random adicional usando POST 
        self.assertEqual(procesar("EVAL POST 8 3 - 8 4 4 + * -"), "-59")
        self.assertEqual(procesar("MOSTRAR POST 8 3 - 8 4 4 + * -"), "8 - 3 - 8 * (4 + 4)")
        # Revisamos nuestros try except 
        self.assertEqual(procesar("EVAL"), "Falta el parametro <orden>")
        self.assertEqual(procesar("EVAL PRE"), "Falta el parametro <expr>")
        self.assertEqual(procesar("EVAL POST"), "Falta el parametro <expr>")
        self.assertEqual(procesar("EVAL INF"), "El orden no valido, tiene que ser PRE o POST")
        self.assertEqual(procesar("EVAL -6 -6 - -1 -2 -3 + * +"), "El orden no valido, tiene que ser PRE o POST")
        self.assertEqual(procesar("MOSTRAR"), "Falta el parametro <orden>")
        self.assertEqual(procesar("MOSTRAR PRE"), "Falta el parametro <expr>")
        self.assertEqual(procesar("MOSTRAR POST"), "Falta el parametro <expr>")
        self.assertEqual(procesar("MOSTRAR INF"), "El orden no valido, tiene que ser PRE o POST")
        self.assertEqual(procesar("MOSTRAR -6 -6 - -1 -2 -3 + * +"), "El orden no valido, tiene que ser PRE o POST")
        # Probamos si el usuario ingreso algo loco en la entrada
        self.assertEqual(procesar("algo"), "La accion no es ni EVAL,MOSTRAR o SALIR")
        with self.assertRaises(SystemExit):
            procesar("SALIR")