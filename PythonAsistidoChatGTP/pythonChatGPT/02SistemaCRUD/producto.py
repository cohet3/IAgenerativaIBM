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
