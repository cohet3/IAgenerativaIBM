class Producto:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return f"Producto(nombre='{self.nombre}', descripcion='{self.descripcion}', precio={self.precio})"


class Subproducto(Producto):
    def __init__(self, nombre, descripcion, precio, marca):
        super().__init__(nombre, descripcion, precio)
        self.marca = marca

    def __str__(self):
        return f"Subproducto(nombre='{self.nombre}', descripcion='{self.descripcion}', precio={self.precio}, marca='{self.marca}')"


# Crear una lista de productos de prueba
productos = [
    Producto('Camisa', 'Camisa de algodón', 20.0),
    Producto('Pantalón', 'Pantalón de mezclilla', 30.0),
    Subproducto('Zapatillas', 'Zapatillas deportivas', 50.0, 'Nike')
]


# Funciones CRUD
def crear_producto(nombre, descripcion, precio, marca=None):
    """
    Crea y agrega un nuevo producto o subproducto a la lista de productos.
    """
    if marca:
        producto = Subproducto(nombre, descripcion, precio, marca)
    else:
        producto = Producto(nombre, descripcion, precio)
    productos.append(producto)


def leer_producto(nombre):
    """
    Lee y retorna un producto por su nombre.
    """
    for producto in productos:
        if producto.nombre == nombre:
            return producto
    return None


def actualizar_producto(nombre, descripcion=None, precio=None, marca=None):
    """
    Actualiza los atributos de un producto existente.
    """
    producto = leer_producto(nombre)
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


def borrar_producto(nombre):
    """
    Elimina un producto de la lista por su nombre.
    """
    producto = leer_producto(nombre)
    if producto:
        productos.remove(producto)
    else:
        raise ValueError("Producto no encontrado")


# Ejemplos de uso:
try:
    print("Producto creado: Camisa")
    crear_producto('Camisa', 'Camisa de seda', 25.0)
    print(productos[-1])
except Exception as e:
    print(e)

try:
    print("\nLeer producto: Zapatillas")
    prod = leer_producto('Zapatillas')
    print(prod)
except Exception as e:
    print(e)

try:
    print("\nActualizar producto: Zapatillas")
    actualizar_producto('Zapatillas', precio=55.0, marca='Adidas')
    prod = leer_producto('Zapatillas')
    print(prod)
except Exception as e:
    print(e)

try:
    print("\nBorrar producto: Camisa")
    borrar_producto('Camisa')
    print(productos)
except Exception as e:
    print(e)
