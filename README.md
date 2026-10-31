# Simulador de inventario

Proyecto del segundo corte de Programación II (167003), Grupo AR, Universidad de Pamplona.

Simulador que ayuda a decidir cuándo y cuánto pedir de un producto para no quedarse sin existencias. Los requerimientos están en [REQUIREMENTS.md](REQUIREMENTS.md).

## Estado actual

- `inventario.py`: inventario día a día con **demanda fija** y política de pedido por **punto de reorden** (RF3). Cuando las existencias quedan en el punto de reorden o por debajo y no hay otro pedido en camino, se pide una cantidad fija que llega después del tiempo de entrega.
- `interfaz.py`: ventana hecha con **tkinter** (RF1). Permite escribir el producto y sus datos, definir la política de pedido y simular. Muestra la gráfica de existencias de matplotlib dentro de la ventana, la tabla día a día y un resumen con los días sin producto, las unidades faltantes, las existencias promedio y los pedidos.

Se escogió tkinter porque viene incluido con Python y matplotlib se integra con él mediante `FigureCanvasTkAgg`.

## Requisitos

- Python 3.10 o superior
- numpy y matplotlib

```bash
pip install numpy matplotlib
```

## Cómo abrir la interfaz

```bash
python interfaz.py
```

También se puede ver la simulación en la consola con `python inventario.py`.
