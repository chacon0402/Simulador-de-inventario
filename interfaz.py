"""
Interfaz gráfica del simulador de inventario (RF1).

Se usa tkinter porque viene incluido con Python (no hay que instalar nada
extra para las ventanas) y matplotlib se integra con FigureCanvasTkAgg.

Ejecutar con:  python interfaz.py
"""

import tkinter as tk
from tkinter import ttk, messagebox

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from inventario import simular_inventario, resumen


# Campos del formulario: (clave, texto, valor por defecto, valor mínimo)
CAMPOS = [
    ("demanda_diaria", "Demanda diaria (unidades)", 20, 0),
    ("dias", "Días a simular", 30, 1),
    ("existencias_iniciales", "Existencias iniciales", 100, 0),
    ("punto_reorden", "Punto de reorden", 60, 0),
    ("cantidad_pedido", "Cantidad a pedir", 150, 1),
    ("tiempo_entrega", "Tiempo de entrega (días)", 3, 0),
]

COLUMNAS = [
    ("dia", "Día", 45),
    ("inicial", "Inicial", 70),
    ("llego", "Llegó", 60),
    ("demanda", "Demanda", 70),
    ("vendido", "Vendido", 70),
    ("faltante", "Faltó", 60),
    ("final", "Final", 60),
    ("pedido", "Pedido", 150),
]


class AppInventario(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de inventario")
        self.geometry("1100x650")
        self.minsize(900, 550)

        self.entradas = {}
        self.crear_panel_datos()
        self.crear_panel_resultados()
        self.simular()

    # ---------- Panel izquierdo: producto y política ----------
    def crear_panel_datos(self):
        panel = ttk.Frame(self, padding=12)
        panel.pack(side="left", fill="y")

        ttk.Label(panel, text="Producto", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        self.producto = tk.StringVar(value="Arroz x 500 g")
        ttk.Entry(panel, textvariable=self.producto, width=28).pack(anchor="w", pady=(2, 12))

        datos = ttk.LabelFrame(panel, text="Datos y política de pedido", padding=10)
        datos.pack(fill="x")
        for fila, (clave, texto, defecto, _) in enumerate(CAMPOS):
            ttk.Label(datos, text=texto).grid(row=fila, column=0, sticky="w", pady=4)
            var = tk.StringVar(value=str(defecto))
            ttk.Spinbox(datos, from_=0, to=100000, textvariable=var, width=8).grid(
                row=fila, column=1, padx=(8, 0), pady=4)
            self.entradas[clave] = var

        ttk.Button(panel, text="Simular", command=self.simular).pack(fill="x", pady=12)

        caja = ttk.LabelFrame(panel, text="Resumen", padding=10)
        caja.pack(fill="x")
        self.textos_resumen = {}
        for clave, texto in [
            ("dias_sin_producto", "Días sin producto"),
            ("unidades_faltantes", "Unidades faltantes"),
            ("existencias_promedio", "Existencias promedio"),
            ("pedidos", "Pedidos realizados"),
        ]:
            fila = ttk.Frame(caja)
            fila.pack(fill="x", pady=2)
            ttk.Label(fila, text=texto).pack(side="left")
            valor = ttk.Label(fila, text="-", font=("Segoe UI", 10, "bold"))
            valor.pack(side="right")
            self.textos_resumen[clave] = valor

    # ---------- Panel derecho: gráfica y tabla ----------
    def crear_panel_resultados(self):
        pestañas = ttk.Notebook(self)
        pestañas.pack(side="right", fill="both", expand=True, padx=(0, 12), pady=12)

        marco_grafica = ttk.Frame(pestañas)
        pestañas.add(marco_grafica, text="Gráfica")
        self.figura = Figure(figsize=(7, 4.5), dpi=100)
        self.ejes = self.figura.add_subplot(111)
        self.lienzo = FigureCanvasTkAgg(self.figura, master=marco_grafica)
        self.lienzo.get_tk_widget().pack(fill="both", expand=True)

        marco_tabla = ttk.Frame(pestañas)
        pestañas.add(marco_tabla, text="Tabla día a día")
        self.tabla = ttk.Treeview(marco_tabla, columns=[c[0] for c in COLUMNAS],
                                  show="headings")
        for clave, texto, ancho in COLUMNAS:
            self.tabla.heading(clave, text=texto)
            self.tabla.column(clave, width=ancho, anchor="center")
        self.tabla.tag_configure("faltante", background="#f8d7da")
        self.tabla.tag_configure("pedido", background="#fff3cd")
        barra = ttk.Scrollbar(marco_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=barra.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")

    # ---------- Lógica ----------
    def leer_datos(self):
        """Lee y valida los datos del formulario. Devuelve None si hay error."""
        datos = {}
        for clave, texto, _, minimo in CAMPOS:
            try:
                valor = int(self.entradas[clave].get())
            except ValueError:
                messagebox.showerror("Dato inválido", f"'{texto}' debe ser un número entero.")
                return None
            if valor < minimo:
                messagebox.showerror("Dato inválido", f"'{texto}' debe ser al menos {minimo}.")
                return None
            datos[clave] = valor
        return datos

    def simular(self):
        datos = self.leer_datos()
        if datos is None:
            return
        registro = simular_inventario(**datos)
        self.mostrar_resumen(resumen(registro))
        self.mostrar_tabla(registro)
        self.mostrar_grafica(registro, datos["punto_reorden"])

    def mostrar_resumen(self, r):
        self.textos_resumen["dias_sin_producto"].config(text=str(r["dias_sin_producto"]))
        self.textos_resumen["unidades_faltantes"].config(text=str(r["unidades_faltantes"]))
        self.textos_resumen["existencias_promedio"].config(text=f"{r['existencias_promedio']:.1f}")
        self.textos_resumen["pedidos"].config(text=str(r["pedidos"]))

    def mostrar_tabla(self, registro):
        self.tabla.delete(*self.tabla.get_children())
        for d in registro:
            pedido = f"Sí (llega día {d['llega_el_dia']})" if d["pidio"] else ""
            etiqueta = "faltante" if d["faltante"] > 0 else ("pedido" if d["pidio"] else "")
            self.tabla.insert("", "end", tags=(etiqueta,), values=(
                d["dia"], d["inicial"], d["llego"], d["demanda"],
                d["vendido"], d["faltante"], d["final"], pedido))

    def mostrar_grafica(self, registro, punto_reorden):
        ax = self.ejes
        ax.clear()
        dias = [d["dia"] for d in registro]
        finales = [d["final"] for d in registro]

        ax.step(dias, finales, where="mid", color="#1f77b4", linewidth=2,
                label="Existencias al final del día")
        ax.axhline(punto_reorden, color="#ff7f0e", linestyle="--",
                   label=f"Punto de reorden ({punto_reorden})")

        pedidos = [d for d in registro if d["pidio"]]
        ax.scatter([d["dia"] for d in pedidos], [d["final"] for d in pedidos],
                   marker="v", s=70, color="#ff7f0e", zorder=3, label="Se hace pedido")
        llegadas = [d for d in registro if d["llego"] > 0]
        ax.scatter([d["dia"] for d in llegadas], [d["final"] for d in llegadas],
                   marker="^", s=70, color="#2ca02c", zorder=3, label="Llega pedido")
        faltas = [d for d in registro if d["faltante"] > 0]
        ax.scatter([d["dia"] for d in faltas], [0] * len(faltas),
                   marker="x", s=70, color="#d62728", zorder=3, label="Día sin producto")

        ax.set_title(f"Inventario día a día - {self.producto.get()}")
        ax.set_xlabel("Día")
        ax.set_ylabel("Unidades")
        ax.set_ylim(bottom=0)
        ax.grid(alpha=0.3)
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=3, fontsize=8)
        self.figura.tight_layout()
        self.lienzo.draw()


if __name__ == "__main__":
    AppInventario().mainloop()
