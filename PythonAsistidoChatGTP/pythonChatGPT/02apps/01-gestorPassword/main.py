# Crea un programa gráfico con Tkinter para generar una contraseña aleatoria, que acepte
# minúsculas, mayúsculas, números y caracteres especiales a partir de una longitud
# establecida préviamente por el usuario.Crea un programa gráfico con Tkinter para generar una contraseña aleatoria, que acepte
# minúsculas, mayúsculas, números y caracteres especiales a partir de una longitud
# establecida préviamente por el usuario.

import tkinter as tk
from tkinter import messagebox
import random
import string


def generar_contrasena():
    try:
        longitud = int(entry_longitud.get())
    except ValueError:
        messagebox.showerror("Error", "La longitud debe ser un número entero.")
        return

    if longitud <= 0:
        messagebox.showerror("Error", "La longitud debe ser mayor que cero.")
        return

    caracteres = ""
    if var_minusculas.get():
        caracteres += string.ascii_lowercase
    if var_mayusculas.get():
        caracteres += string.ascii_uppercase
    if var_numeros.get():
        caracteres += string.digits
    if var_especiales.get():
        caracteres += string.punctuation

    if not caracteres:
        messagebox.showerror("Error", "Debe seleccionar al menos un tipo de carácter.")
        return

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    entry_contrasena.delete(0, tk.END)
    entry_contrasena.insert(0, contrasena)


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("400x300")

# Etiqueta y entrada para la longitud de la contraseña
tk.Label(ventana, text="Longitud de la contraseña:").pack(pady=5)
entry_longitud = tk.Entry(ventana)
entry_longitud.pack(pady=5)

# Checkbuttons para seleccionar el tipo de caracteres
var_minusculas = tk.BooleanVar()
var_mayusculas = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_especiales = tk.BooleanVar()

tk.Checkbutton(ventana, text="Incluir minúsculas", variable=var_minusculas).pack(anchor='w')
tk.Checkbutton(ventana, text="Incluir mayúsculas", variable=var_mayusculas).pack(anchor='w')
tk.Checkbutton(ventana, text="Incluir números", variable=var_numeros).pack(anchor='w')
tk.Checkbutton(ventana, text="Incluir caracteres especiales", variable=var_especiales).pack(anchor='w')

# Botón para generar la contraseña
tk.Button(ventana, text="Generar contraseña", command=generar_contrasena).pack(pady=10)

# Entrada para mostrar la contraseña generada
tk.Label(ventana, text="Contraseña generada:").pack(pady=5)
entry_contrasena = tk.Entry(ventana, width=50)
entry_contrasena.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
