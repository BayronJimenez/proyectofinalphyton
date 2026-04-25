import tkinter as tk
from tkinter import font

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Programa para subir a repositorio")
ventana.geometry("600x300")  # Ventana más grande para texto grande

# Crear una fuente grande y estilizada
fuente_linda = font.Font(family="Comic Sans MS", size=20, weight="bold", slant="italic")

# Crear un label con colores llamativos
etiqueta = tk.Label(
    ventana,
    text="Este programa es de Bayron Jimenez Lerma",
    font=fuente_linda,
    fg="yellow",     # Color del texto
    bg="darkblue",   # Fondo llamativo
    padx=20,
    pady=20
)
etiqueta.pack(expand=True, fill='both')

# Ejecutar la ventana
ventana.mainloop()