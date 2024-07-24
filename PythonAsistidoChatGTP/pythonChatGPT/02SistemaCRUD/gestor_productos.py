from producto import Producto, Subproducto


class GestorProductos:
    def __init__(self):
        self.productos = []

    def crear_producto(self, nombre, descripcion, precio, marca=None):
        """
        Crea y agrega un nuevo producto o subproducto a la lista de productos.
        """
        if marca:
            producto = Subproducto(nombre, descripcion, precio, marca)
        else:
            producto = Producto(nombre, descripcion, precio)
        self.productos.append(producto)

    def leer_producto(self, nombre):
        """
        Lee y retorna un producto por su nombre.
        """
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def actualizar_producto(self, nombre, descripcion=None, precio=None, marca=None):
        """
        Actualiza los atributos de un producto existente.
        """
        producto = self.leer_producto(nombre)
        if producto:
            if descripcion:
                producto.descripcion = descripcion
            if precio:
                producto.precio = precio
            if marca and isinstance(producto, Subproducto):
                producto.marca = marca
            elif marca and not isinstance(producto, Subproducto):
                raise ValueError("No se puede asignar una marca a un producto que no es un subproducto.")
        else:
            raise ValueError("Producto no encontrado")

    def borrar_producto(self, nombre):
        """
        Elimina un producto de la lista por su nombre.
        """
        producto = self.leer_producto(nombre)
        if producto:
            self.productos.remove(producto)
        else:
            raise ValueError("Producto no encontrado")
