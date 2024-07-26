# Hazme un programa con Tkinter donde en un formular o eructurado en una pequena
# cuaonicula, escribas tres numeros y me cacu e una teol ot ves elve ellos al presionar un
# boton con el texto Calcular
import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        num3 = float(entry_num3.get())

        suma = num1 + num2 + num3
        producto = num1 * num2 * num3
        promedio = suma / 3

        resultado_texto = f"Suma: {suma}\nProducto: {producto}\nPromedio: {promedio}"
        messagebox.showinfo("Resultado", resultado_texto)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x200")

# Crear y posicionar las etiquetas y entradas
tk.Label(ventana, text="Número 1:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Número 2:").grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Número 3:").grid(row=2, column=0, padx=10, pady=10)
entry_num3 = tk.Entry(ventana)
entry_num3.grid(row=2, column=1, padx=10, pady=10)

# Crear y posicionar el botón
btn_calcular = tk.Button(ventana, text="Calcular", command=calcular)
btn_calcular.grid(row=3, columnspan=2, pady=20)

# Ejecutar la aplicación
ventana.mainloop()
