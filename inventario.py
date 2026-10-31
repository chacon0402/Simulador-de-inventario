"""
Inventario día a día con demanda fija y política de pedido (punto de reorden).

Avance del sábado 31 de octubre - Proyecto Corte 2, Programación II (167003).

Orden de los eventos en cada día:
  1. Llega el pedido si hoy es su día de llegada.
  2. Se atiende la demanda del día. Si no alcanza, se vende lo que hay
     y la demanda que falta se pierde (el día cuenta como "día sin producto").
  3. Se revisa la política: si las existencias quedan en el punto de reorden
     o por debajo, y no hay otro pedido en camino, se pide la cantidad fija.
     El pedido llega `tiempo_entrega` días después.
"""


def simular_inventario(demanda_diaria, dias, existencias_iniciales,
                       punto_reorden, cantidad_pedido, tiempo_entrega):
    """Simula el inventario día por día y devuelve un registro de cada día.

    demanda_diaria: unidades que se piden cada día (fija en este avance).
    dias: cantidad de días a simular (por ejemplo, 30 para un mes).
    existencias_iniciales: unidades en bodega el día 1.
    punto_reorden: si las existencias bajan a este valor, se hace un pedido.
    cantidad_pedido: unidades que se piden cada vez.
    tiempo_entrega: días que tarda el proveedor en entregar.
    """
    existencias = existencias_iniciales
    dia_llegada = None  # día en que llega el pedido en camino (None si no hay)
    registro = []

    for dia in range(1, dias + 1):
        inicial = existencias

        # 1. Llegada del pedido
        llego = 0
        if dia_llegada == dia:
            llego = cantidad_pedido
            existencias += llego
            dia_llegada = None

        # 2. Atender la demanda
        vendido = min(demanda_diaria, existencias)
        faltante = demanda_diaria - vendido
        existencias -= vendido

        # 3. Política de pedido
        pidio = False
        if existencias <= punto_reorden and dia_llegada is None:
            dia_llegada = dia + tiempo_entrega
            pidio = True

        registro.append({
            "dia": dia,
            "inicial": inicial,
            "llego": llego,
            "demanda": demanda_diaria,
            "vendido": vendido,
            "faltante": faltante,
            "final": existencias,
            "pidio": pidio,
            "llega_el_dia": dia_llegada if pidio else None,
        })

    return registro


def resumen(registro):
    """Calcula los indicadores básicos de la simulación."""
    dias = len(registro)
    dias_sin_producto = sum(1 for d in registro if d["faltante"] > 0)
    existencias_promedio = sum(d["final"] for d in registro) / dias
    pedidos = sum(1 for d in registro if d["pidio"])
    unidades_faltantes = sum(d["faltante"] for d in registro)
    return {
        "dias_sin_producto": dias_sin_producto,
        "existencias_promedio": existencias_promedio,
        "pedidos": pedidos,
        "unidades_faltantes": unidades_faltantes,
    }


def imprimir_tabla(registro):
    print(f"{'Día':>4} {'Inicial':>8} {'Llegó':>6} {'Demanda':>8} "
          f"{'Vendido':>8} {'Faltó':>6} {'Final':>6}  Pedido")
    for d in registro:
        pedido = f"sí (llega día {d['llega_el_dia']})" if d["pidio"] else ""
        print(f"{d['dia']:>4} {d['inicial']:>8} {d['llego']:>6} "
              f"{d['demanda']:>8} {d['vendido']:>8} {d['faltante']:>6} "
              f"{d['final']:>6}  {pedido}")


if __name__ == "__main__":
    # Datos de ejemplo de un producto
    parametros = {
        "demanda_diaria": 20,
        "dias": 30,
        "existencias_iniciales": 100,
        "punto_reorden": 60,
        "cantidad_pedido": 150,
        "tiempo_entrega": 3,
    }

    print("Simulación de inventario con demanda fija")
    for nombre, valor in parametros.items():
        print(f"  {nombre}: {valor}")
    print()

    registro = simular_inventario(**parametros)
    imprimir_tabla(registro)

    r = resumen(registro)
    print()
    print(f"Días sin producto:     {r['dias_sin_producto']}")
    print(f"Unidades faltantes:    {r['unidades_faltantes']}")
    print(f"Existencias promedio:  {r['existencias_promedio']:.1f}")
    print(f"Pedidos realizados:    {r['pedidos']}")
