import unittest
from io import StringIO
import sys
from producto import Producto, Subproducto
from gestor_productos import GestorProductos
from utilidades import mostrar_productos


class TestGestorProductos(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorProductos()
        self.gestor.crear_producto('Camisa', 'Camisa de algodón', 20.0)
        self.gestor.crear_producto('Pantalón', 'Pantalón de mezclilla', 30.0)
        self.gestor.crear_producto('Zapatillas', 'Zapatillas deportivas', 50.0, 'Nike')

    def test_crear_producto(self):
        self.gestor.crear_producto('Sombrero', 'Sombrero de lana', 15.0)
        producto = self.gestor.leer_producto('Sombrero')
        self.assertIsNotNone(producto)
        self.assertEqual(producto.nombre, 'Sombrero')
        self.assertEqual(producto.descripcion, 'Sombrero de lana')
        self.assertEqual(producto.precio, 15.0)
        self.assertFalse(hasattr(producto, 'marca'))

    def test_crear_subproducto(self):
        self.gestor.crear_producto('Gorra', 'Gorra deportiva', 10.0, 'Adidas')
        subproducto = self.gestor.leer_producto('Gorra')
        self.assertIsNotNone(subproducto)
        self.assertEqual(subproducto.nombre, 'Gorra')
        self.assertEqual(subproducto.descripcion, 'Gorra deportiva')
        self.assertEqual(subproducto.precio, 10.0)
        self.assertTrue(hasattr(subproducto, 'marca'))
        self.assertEqual(subproducto.marca, 'Adidas')

    def test_leer_producto_existente(self):
        producto = self.gestor.leer_producto('Camisa')
        self.assertIsNotNone(producto)
        self.assertEqual(producto.nombre, 'Camisa')

    def test_leer_producto_inexistente(self):
        producto = self.gestor.leer_producto('Zapato')
        self.assertIsNone(producto)

    def test_actualizar_producto_existente(self):
        self.gestor.actualizar_producto('Camisa', descripcion='Camisa de lino', precio=25.0)
        producto = self.gestor.leer_producto('Camisa')
        self.assertIsNotNone(producto)
        self.assertEqual(producto.descripcion, 'Camisa de lino')
        self.assertEqual(producto.precio, 25.0)

    def test_actualizar_subproducto_existente(self):
        self.gestor.actualizar_producto('Zapatillas', precio=55.0, marca='Adidas')
        subproducto = self.gestor.leer_producto('Zapatillas')
        self.assertIsNotNone(subproducto)
        self.assertEqual(subproducto.precio, 55.0)
        self.assertEqual(subproducto.marca, 'Adidas')

    def test_actualizar_producto_inexistente(self):
        with self.assertRaises(ValueError):
            self.gestor.actualizar_producto('Zapato', descripcion='Zapato de cuero')

    def test_borrar_producto_existente(self):
        self.gestor.borrar_producto('Camisa')
        producto = self.gestor.leer_producto('Camisa')
        self.assertIsNone(producto)

    def test_borrar_producto_inexistente(self):
        with self.assertRaises(ValueError):
            self.gestor.borrar_producto('Zapato')

    def test_mostrar_productos(self):
        # Redirigir la salida estándar a un StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            mostrar_productos(self.gestor.productos)
            output = out.getvalue().strip()
        finally:
            sys.stdout = saved_stdout

        # Verificar la salida esperada
        self.assertIn("Producto(nombre='Camisa', descripcion='Camisa de algodón', precio=20.0)", output)
        self.assertIn("Producto(nombre='Pantalón', descripcion='Pantalón de mezclilla', precio=30.0)", output)
        self.assertIn(
            "Subproducto(nombre='Zapatillas', descripcion='Zapatillas deportivas', precio=50.0, marca='Nike')", output)


if __name__ == "__main__":
    unittest.main()
