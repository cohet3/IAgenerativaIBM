import unittest


def division(numero1, numero2):
    """
    Realiza la división de dos números y maneja la división por cero.

    Args:
        numero1 (float): El numerador.
        numero2 (float): El denominador.

    Returns:
        float: El resultado de la división si es exitosa.
        str: Un mensaje de error si ocurre una división por cero.
    """
    try:
        return numero1 / numero2
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."


class TestDivisionFunction(unittest.TestCase):

    def test_division_normal(self):
        """Prueba divisiones normales."""
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(9, 3), 3)
        self.assertAlmostEqual(division(10, 3), 3.3333, places=4)

    def test_division_by_zero(self):
        """Prueba la división por cero."""
        self.assertEqual(division(10, 0), "Error: No se puede dividir por cero.")

    def test_division_negative_numbers(self):
        """Prueba divisiones con números negativos."""
        self.assertEqual(division(-10, 2), -5)
        self.assertEqual(division(10, -2), -5)
        self.assertEqual(division(-10, -2), 5)

    def test_division_with_zero_numerator(self):
        """Prueba divisiones donde el numerador es cero."""
        self.assertEqual(division(0, 10), 0)
        self.assertEqual(division(0, -10), 0)

    def test_division_float_results(self):
        """Prueba divisiones que producen resultados flotantes."""
        self.assertEqual(division(10, 4), 2.5)
        self.assertAlmostEqual(division(7, 3), 2.3333, places=4)

    def test_division_type_error(self):
        """Prueba divisiones con tipos incorrectos."""
        with self.assertRaises(TypeError):
            division("10", 2)
        with self.assertRaises(TypeError):
            division(10, "2")
        with self.assertRaises(TypeError):
            division("10", "2")


if __name__ == "__main__":
    unittest.main()
