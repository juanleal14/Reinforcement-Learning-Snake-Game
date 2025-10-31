# Reinforcement Learning Snake Game

## Descripción
Proyecto académico que implementa el juego de la serpiente controlado mediante **Q-Learning**. El entorno está construido con PyGame y se han experimentado dos configuraciones ("Phase 2" y "Phase 3") que amplían progresivamente el espacio de estados y las señales de recompensa para mejorar el comportamiento aprendido por el agente.

## Estructura del repositorio
- `Phase 2/`: versión con un vector de estado de 8 características binarias que describen la posición relativa de la comida y la seguridad de los movimientos disponibles.
  - `SnakeGame.py`: bucle principal del juego, configuración de episodios y renderizado opcional.
  - `snake_env.py`: implementación del entorno y la lógica de recompensas.
  - `q_learning.py`: algoritmo Q-Learning y gestión de la tabla de valores.
  - `q_table_phase2.txt`: tabla Q persistente para esta configuración.
- `Phase 3/`: versión avanzada con una característica adicional para detectar bucles y penalizarlos, junto con recompensas más estrictas para evitar estancamiento.
  - Archivos análogos a la fase 2 (`SnakeGame.py`, `snake_env.py`, `q_learning.py`, `q_table_phase3.txt`).

## Requisitos previos
- Python 3.9 o superior.
- Dependencias de Python: `pygame`, `numpy`.

Puedes instalarlas manualmente con:
```bash
pip install pygame numpy
```

## Puesta en marcha
1. Clona el repositorio y sitúate en la raíz del proyecto.
2. (Opcional) Crea y activa un entorno virtual.
3. Ejecuta una de las fases:

   ```bash
   cd "Phase 2"
   python SnakeGame.py
   ```
   o bien
   ```bash
   cd "Phase 3"
   python SnakeGame.py
   ```

   Por defecto `render_game = True`, por lo que se abrirá una ventana de PyGame con la serpiente moviéndose según la política almacenada.

## Entrenamiento del agente
- Cada `SnakeGame.py` permite alternar entre modo inferencia y entrenamiento mediante la variable booleana `training`. Establécela en `True` para actualizar la tabla Q durante la ejecución.
- Ajusta el número de episodios con la variable `num_episodes` y los hiperparámetros (`alpha`, `gamma`, `epsilon`, etc.) en `q_learning.py` si necesitas experimentar con diferentes configuraciones de aprendizaje.
- Tras cada episodio la tabla Q se guarda automáticamente en `q_table_phase*.txt`. Borra o renombra este archivo si deseas reiniciar el entrenamiento desde cero.

## Personalización del entorno
- Modifica `FRAME_SIZE_X` y `FRAME_SIZE_Y` para cambiar el tamaño del tablero.
- Controla si la serpiente crece al comer ajustando `growing_body` en cada fase.
- En la fase 3 puedes utilizar la característica `loop` para castigar movimientos repetitivos y acelerar la convergencia.

## Consejos y solución de problemas
- Si la ventana de PyGame no responde, asegúrate de cerrar correctamente el proceso con la "X" o `Ctrl+C` en la terminal.
- Para depurar el comportamiento del agente, imprime los estados y recompensas dentro del bucle principal o ajusta los valores de recompensa en `snake_env.py`.
- Recuerda que al renderizar y entrenar simultáneamente el aprendizaje será más lento; si buscas velocidad, fija `render_game = False`.
