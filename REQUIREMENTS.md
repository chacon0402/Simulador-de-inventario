# Simulador de inventario para no quedarse sin producto

**Proyecto del segundo corte · Programación II (167003) · Grupo AR · 2026-II**
Universidad de Pamplona · Docente: Ing. Juan Sebastián Galindo Lizcano

| Integrante | Usuario de GitHub |
|---|---|
| Laura Valentina Alarcón Corredor | alarconcorredorlauraestela-spec |
| Carlos Esteban Chacón Clavijo | (pendiente) |
| Yarilenny Cárdenas Arteaga | yari-car |

**Entrega final:** miércoles 11 de noviembre de 2026. El programa se presenta funcionando en clase y la documentación se envía al correo del docente.

---

## 1. Descripción

El grupo desarrollará en Python, con numpy y matplotlib, un simulador que ayuda a un negocio a decidir cuándo y cuánto pedir de un producto para no quedarse sin existencias sin llenar la bodega. La demanda de cada día es aleatoria, así que el simulador repite muchos meses posibles y compara políticas de pedido.

## 2. Requerimientos funcionales

- **RF1. Interfaz gráfica.** Todo el programa se maneja desde ventanas, no desde la consola: escoger el producto y sus datos, definir la política de pedido, simular y comparar políticas con sus gráficas. El grupo escoge la librería (por ejemplo, tkinter, customtkinter o PySide6) y justifica la elección en el pendón. Las gráficas de matplotlib se muestran dentro de la ventana (con tkinter, por ejemplo, con `FigureCanvasTkAgg`).
- **RF2. Demanda aleatoria.** La demanda diaria es una variable aleatoria generada con `np.random.default_rng` y una semilla, de modo que la simulación se pueda repetir. El grupo escoge la distribución, la explica en el pendón y la muestra en un histograma.
- **RF3. Política de pedido.** El simulador usa un punto de reorden y una cantidad a pedir: cuando las existencias bajan del punto, se hace un pedido que llega después del tiempo de entrega del proveedor.
- **RF4. Muchas corridas.** Se simulan varios meses muchas veces (como mínimo 1000 corridas) y se miden los días sin producto, las existencias promedio y el costo (de pedir, de guardar y de no tener).
- **RF5. Comparar políticas.** Desde la interfaz se prueban varios puntos de reorden y cantidades, y el programa muestra en una gráfica cómo cambian los días sin producto y el costo, y recomienda la mejor política.

## 3. Lo que debe verse de la Unidad 5 en el código

La lógica del programa se construye con lo visto en clase y en las guías de aprendizaje de la unidad.

| Tema | Qué se exige |
|---|---|
| Variables aleatorias | La demanda como variable aleatoria, con su media y su variabilidad |
| Generar números aleatorios | `np.random.default_rng` con semilla |
| Simulación | Muchas corridas y resultados promedio, como en la guía 03 de la unidad |
| Gráficas | Histogramas y comparación de políticas con matplotlib |

La Unidad 5 se dicta en clase del 14 al 21 de noviembre, después de la entrega: el grupo trabaja desde ahora con las guías 01 a 03 de esa unidad (`Clases\Unidad 5\`). La interfaz gráfica y la teoría de inventarios (punto de reorden) no se vieron en clase: el grupo los investiga y cita sus fuentes en las referencias del pendón.

## 4. Avances esperados

El docente suministra el repositorio de GitHub del grupo, y todo el trabajo se sube a ese repositorio y a ningún otro. Esta tabla indica lo que se espera que el repositorio tenga en cada fecha. El proyecto se construye por partes y cada avance se sube a medida que se hace. Los avances deben cumplirse, porque de ellos pueden salir notas de actividades del corte. Cada integrante sube sus propios commits, con mensajes que digan qué se hizo (por ejemplo, "Agrega la demanda aleatoria con semilla").

| Fecha | Avance esperado en el repositorio |
|---|---|
| Sábado 31 de octubre | Este documento de requerimientos y el inventario día a día con demanda fija, con su política de pedido |
| Miércoles 4 de noviembre | Demanda aleatoria con semilla y su histograma; primera ventana |
| Sábado 7 de noviembre | Muchas corridas y comparación de políticas, todo desde la interfaz |
| Miércoles 11 de noviembre | Programa completo; documentación final: pendón, diapositivas y Kahoot |

## 5. Entregables

1. **Programa funcionando**, presentado en clase el miércoles 11 de noviembre. Cada integrante explica una parte del código.
2. **Repositorio de GitHub suministrado por el docente**, con el código, este `REQUIREMENTS.md`, un `README.md` propio del grupo y los commits de los tres integrantes. El `README.md` lo escribe el grupo y explica qué hace el programa, la versión de Python, las librerías que hay que instalar y el comando para abrir la interfaz.
3. **Correo a sebastian.galindo@unipamplona.edu.co**, con el asunto "Proyecto Corte 2 - 167003 - Grupo 4", que contenga el enlace al repositorio, el pendón en PDF, las diapositivas de presentación y el enlace del Kahoot.
4. **Pendón**, que no se imprime: se entrega en PDF y se elabora con base en los ejemplos compartidos en el grupo de WhatsApp. Lleva estas secciones: introducción, marco teórico, metodología, gráficos y visualizaciones (gráficas producidas por el programa y capturas de la interfaz), análisis y discusión, conclusiones y recomendaciones, y referencias.
5. **Diapositivas de presentación**, que el grupo usa para exponer el proyecto en clase.
6. **Kahoot de 5 preguntas**, que se juega con el curso al terminar la exposición. Las preguntas tienen que ver con que los compañeros presten atención cuando ustedes estén exponiendo.

## 6. Exposición

La exposición se hace en clase el miércoles 11 de noviembre y la nota es grupal. La clase se graba.

## 7. Calificación

| Componente | Valor |
|---|---|
| Simulador de inventario: programa funcionando, documentación y exposición | 3,5 |
| Respuestas a los Kahoot de los compañeros | 1,5 |
| **Total** | **5,0** |

La nota del proyecto es **0** y **no se permite presentar el parcial** en cualquiera de estos casos:

- el programa no se presenta funcionando;
- se presenta un proyecto distinto del asignado;
- los avances están en un repositorio distinto del que suministra el docente.
