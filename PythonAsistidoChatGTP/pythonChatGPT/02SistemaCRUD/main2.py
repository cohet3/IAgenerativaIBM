from gestor_productos import GestorProductos
from utilidades import mostrar_productos


def main():
    gestor = GestorProductos()

    # Crear algunos productos
    gestor.crear_producto('Camisa', 'Camisa de algodón', 20.0)
    gestor.crear_producto('Pantalón', 'Pantalón de mezclilla', 30.0)
    gestor.crear_producto('Zapatillas', 'Zapatillas deportivas', 50.0, 'Nike')

    # Mostrar todos los productos
    print("Productos actuales:")
    mostrar_productos(gestor.productos)

    # Actualizar un producto
    try:
        gestor.actualizar_producto('Zapatillas', precio=55.0, marca='Adidas')
        print("\nProducto actualizado: Zapatillas")
    except ValueError as e:
        print(e)

    # Mostrar todos los productos
    print("\nProductos después de actualización:")
    mostrar_productos(gestor.productos)

    # Borrar un producto
    try:
        gestor.borrar_producto('Camisa')
        print("\nProducto borrado: Camisa")
    except ValueError as e:
        print(e)

    # Mostrar todos los productos
    print("\nProductos después de borrado:")
    mostrar_productos(gestor.productos)


if __name__ == "__main__":
    main()
