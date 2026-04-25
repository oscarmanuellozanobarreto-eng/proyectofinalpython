# programa python en repositorio mejorado
import tkinter as tk

ventana = tk.Tk()
ventana.title("programa para subir a repositorio")
ventana.geometry("400x250")
ventana.configure(bg="#1e1e2f")  # color de fondo oscuro

# Fuente personalizada
fuente = ("Helvetica", 14, "bold")

etiqueta = tk.Label(
    ventana,
    text="Este programa es de\nAngel Montiel y Oscar Lozano",
    font=fuente,
    fg="#ffffff",      # color del texto (blanco)
    bg="#1e1e2f",      # mismo fondo que la ventana
    justify="center"
)

etiqueta.pack(pady=40)

ventana.mainloop()