import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# =========================
# COLORES Y ESTILOS
# =========================
COLOR_FONDO = "#F4F6F9"
COLOR_CARD = "#FFFFFF"
COLOR_PRIMARIO = "#2563EB"
COLOR_HOVER = "#1D4ED8"
COLOR_TEXTO = "#1F2937"
COLOR_BORDE = "#D1D5DB"

FUENTE_TITULO = ("Arial", 20, "bold")
FUENTE_LABEL = ("Arial", 11, "bold")
FUENTE_INPUT = ("Arial", 11)
FUENTE_BOTON = ("Arial", 11, "bold")

# =========================
# FUNCIONES
# =========================
def abrir_registro_productos():

    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("500x550")
    reg.configure(bg=COLOR_FONDO)
    reg.resizable(False, False)

    # =========================
    # CONTENEDOR PRINCIPAL
    # =========================
    frame = tk.Frame(
        reg,
        bg=COLOR_CARD,
        bd=0,
        highlightbackground="#E5E7EB",
        highlightthickness=1
    )
    frame.place(relx=0.5, rely=0.5, anchor="center", width=420, height=480)

    # =========================
    # TITULO
    # =========================
    titulo = tk.Label(
        frame,
        text="Registro de Productos",
        font=FUENTE_TITULO,
        bg=COLOR_CARD,
        fg=COLOR_TEXTO
    )
    titulo.pack(pady=20)

    # =========================
    # FUNCION PARA CREAR CAMPOS
    # =========================
    def crear_campo(texto):

        contenedor = tk.Frame(frame, bg=COLOR_CARD)
        contenedor.pack(fill="x", padx=30, pady=8)

        label = tk.Label(
            contenedor,
            text=texto,
            font=FUENTE_LABEL,
            bg=COLOR_CARD,
            fg=COLOR_TEXTO
        )
        label.pack(anchor="w")

        entry = tk.Entry(
            contenedor,
            font=FUENTE_INPUT,
            relief="flat",
            bg="#F9FAFB",
            highlightthickness=1,
            highlightbackground=COLOR_BORDE,
            highlightcolor=COLOR_PRIMARIO
        )
        entry.pack(fill="x", ipady=8, pady=5)

        return entry

    # =========================
    # CAMPOS
    # =========================
    txt_id = crear_campo("ID del Producto")
    txt_desc = crear_campo("Descripción")
    txt_precio = crear_campo("Precio")
    txt_categoria = crear_campo("Categoría")

    # =========================
    # GUARDAR PRODUCTO
    # =========================
    def guardar_producto():

        id_prod = txt_id.get().strip()
        descripcion = txt_desc.get().strip()
        precio = txt_precio.get().strip()
        categoria = txt_categoria.get().strip()

        # VALIDACIONES
        if not id_prod or not descripcion or not precio or not categoria:
            messagebox.showwarning(
                "Campos Vacíos",
                "Complete todos los campos."
            )
            return

        try:
            float(precio)
        except:
            messagebox.showerror(
                "Error",
                "El precio debe ser numérico."
            )
            return

        # GUARDAR
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(BASE_DIR, "productos.txt")

        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{id_prod}|{descripcion}|{precio}|{categoria}\n"
            )

        messagebox.showinfo(
            "Éxito",
            "Producto registrado correctamente."
        )

        # LIMPIAR CAMPOS
        txt_id.delete(0, tk.END)
        txt_desc.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_categoria.delete(0, tk.END)

    # =========================
    # EFECTO HOVER BOTON
    # =========================
    def entrar(e):
        btn_guardar["bg"] = COLOR_HOVER

    def salir(e):
        btn_guardar["bg"] = COLOR_PRIMARIO

    # =========================
    # BOTON GUARDAR
    # =========================
    btn_guardar = tk.Button(
        frame,
        text="Guardar Producto",
        command=guardar_producto,
        font=FUENTE_BOTON,
        bg=COLOR_PRIMARIO,
        fg="white",
        activebackground=COLOR_HOVER,
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=20,
        height=2
    )

    btn_guardar.pack(pady=30)

    btn_guardar.bind("<Enter>", entrar)
    btn_guardar.bind("<Leave>", salir)


def abrir_registro_ventas():
    messagebox.showinfo(
        "Registro de Ventas",
        "Aquí irá el módulo de ventas."
    )


def abrir_reportes():
    messagebox.showinfo(
        "Reportes",
        "Aquí irá el módulo de reportes."
    )


def abrir_acerca_de():
    messagebox.showinfo(
        "Acerca de",
        "LMShop\nSistema Punto de Venta\nVersión 2.0"
    )


# =========================
# VENTANA PRINCIPAL
# =========================
ventana = tk.Tk()
ventana.title("LMShop - Punto de Venta")
ventana.geometry("550x700")
ventana.configure(bg=COLOR_FONDO)
ventana.resizable(False, False)

# =========================
# LOGO
# =========================
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    imagen = Image.open(os.path.join(BASE_DIR, "logo.png"))
    imagen = imagen.resize((220, 220))

    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(
        ventana,
        image=img_logo,
        bg=COLOR_FONDO
    )
    lbl_logo.pack(pady=20)

except:
    lbl_logo = tk.Label(
        ventana,
        text="LMShop",
        font=("Arial", 28, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    lbl_logo.pack(pady=30)

# =========================
# TITULO
# =========================
titulo = tk.Label(
    ventana,
    text="Sistema Punto de Venta",
    font=("Arial", 22, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO
)

titulo.pack(pady=10)

# =========================
# BOTONES MODERNOS
# =========================
def crear_boton(texto, comando):

    boton = tk.Button(
        ventana,
        text=texto,
        command=comando,
        font=FUENTE_BOTON,
        fg="white",
        bg=COLOR_PRIMARIO,
        activebackground=COLOR_HOVER,
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        width=25,
        height=2
    )

    # Hover
    boton.bind(
        "<Enter>",
        lambda e: boton.config(bg=COLOR_HOVER)
    )

    boton.bind(
        "<Leave>",
        lambda e: boton.config(bg=COLOR_PRIMARIO)
    )

    return boton

btn_reg_prod = crear_boton(
    "Registro de Productos",
    abrir_registro_productos
)
btn_reg_prod.pack(pady=12)

btn_reg_ventas = crear_boton(
    "Registro de Ventas",
    abrir_registro_ventas
)
btn_reg_ventas.pack(pady=12)

btn_reportes = crear_boton(
    "Reportes",
    abrir_reportes
)
btn_reportes.pack(pady=12)

btn_acerca = crear_boton(
    "Acerca de",
    abrir_acerca_de
)
btn_acerca.pack(pady=12)

# =========================
# FOOTER
# =========================
footer = tk.Label(
    ventana,
    text="© 2026 LMShop - Todos los derechos reservados",
    font=("Arial", 9),
    bg=COLOR_FONDO,
    fg="gray"
)

footer.pack(side="bottom", pady=20)

# =========================
# INICIO
# =========================
ventana.mainloop()