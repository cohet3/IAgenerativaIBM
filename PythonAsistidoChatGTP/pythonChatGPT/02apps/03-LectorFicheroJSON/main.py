import tkinter as tk
from tkinter import ttk
import json


def cargar_productos():
    with open('productos.json', 'r', encoding='utf-8') as file:
        productos = json.load(file)
    return productos


def mostrar_producto(event):
    item = tabla.selection()[0]
    producto = tabla.item(item, "values")

    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("Detalles del Producto")
    ventana_emergente.geometry("400x200")

    # Mostrar la información del producto
    etiquetas = ["ID", "NOMBRE", "DESCRIPCION", "PRECIO"]
    for i, (etiqueta, valor) in enumerate(zip(etiquetas, producto)):
        tk.Label(ventana_emergente, text=f"{etiqueta}: {valor}", anchor='w').pack(fill='x')


def crear_tabla(productos):
    global tabla

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Productos")
    ventana.geometry("800x400")

    # Crear un Frame para la tabla
    frame_tabla = tk.Frame(ventana)
    frame_tabla.pack(expand=True, fill='both')

    # Crear la tabla
    columnas = ("ID", "NOMBRE", "DESCRIPCION", "PRECIO")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show='headings')

    # Definir encabezados
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, minwidth=0, width=150)

    # Insertar los datos en la tabla
    for producto in productos:
        tabla.insert('', tk.END,
                     values=(producto["ID"], producto["NOMBRE"], producto["DESCRIPCION"], producto["PRECIO"]))

    # Crear un scrollbar vertical y horizontal
    scrollbar_vertical = ttk.Scrollbar(frame_tabla, orient='vertical', command=tabla.yview)
    scrollbar_horizontal = ttk.Scrollbar(frame_tabla, orient='horizontal', command=tabla.xview)
    tabla.configure(yscroll=scrollbar_vertical.set, xscroll=scrollbar_horizontal.set)

    # Empaquetar la tabla y los scrollbars
    tabla.pack(side='left', expand=True, fill='both')
    scrollbar_vertical.pack(side='right', fill='y')
    scrollbar_horizontal.pack(side='bottom', fill='x')

    # Bind doble clic en la tabla
    tabla.bind("<Double-1>", mostrar_producto)

    # Ejecutar la aplicación
    ventana.mainloop()


if __name__ == "__main__":
    productos = cargar_productos()
    crear_tabla(productos)
