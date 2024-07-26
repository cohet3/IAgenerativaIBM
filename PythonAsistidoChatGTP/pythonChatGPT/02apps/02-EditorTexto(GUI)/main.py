# Crea un programa con Tkinter para editar texto que permita abrir ficheros de extensión txt
# usando un cuadro de dialogo, moditicar su contenido y guardarlo de nuevo.
import tkinter as tk
from tkinter import filedialog, messagebox


def abrir_archivo():
    filepath = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if not filepath:
        return
    text_area.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_area.insert(tk.END, text)
    ventana.title(f"Editor de Texto - {filepath}")


def guardar_archivo():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_area.get(1.0, tk.END)
        output_file.write(text)
    ventana.title(f"Editor de Texto - {filepath}")


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Editor de Texto")
ventana.geometry("600x400")

# Crear un Frame para el área de texto
frame_texto = tk.Frame(ventana)
frame_texto.pack(expand=True, fill='both')

# Crear el área de texto con Scrollbar
text_area = tk.Text(frame_texto, wrap='word')
scroll = tk.Scrollbar(frame_texto, command=text_area.yview)
text_area.configure(yscrollcommand=scroll.set)
text_area.pack(side='left', expand=True, fill='both')
scroll.pack(side='right', fill='y')

# Crear el menú
menu_bar = tk.Menu(ventana)
ventana.config(menu=menu_bar)

# Añadir opciones al menú
menu_archivo = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir...", command=abrir_archivo)
menu_archivo.add_command(label="Guardar como...", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Ejecutar la aplicación
ventana.mainloop()
