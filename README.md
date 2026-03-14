#Estructura del Diagrama (Basado en tu código)
Inicio (Óvalo): Punto de partida del programa.
Menú de Opciones (Rombo/Decisión): "¿Qué desea hacer el usuario?".
Opción 1 (Registrar):
Entrada (Paralelogramo): Leer nombre.
Bucle de Validación (Rombo): "¿Es el precio un número válido?".
No: Mostrar error y volver a pedir precio.
Sí: Continuar.
Bucle de Validación (Rombo): "¿Es la cantidad un número entero?".
No: Mostrar error y volver a pedir cantidad.
Sí: Continuar.
Proceso (Rectángulo): costo_total = int(precio * cantidad).
Proceso (Rectángulo): Guardar producto en la lista inventario.
Flecha de retorno: Regresa al Menú de Opciones.
Opción 2 (Ver):
Salida (Paralelogramo): Mostrar lista de productos guardados.
Flecha de retorno: Regresa al Menú de Opciones.
Opción 3 (Salir):
