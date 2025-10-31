# Reinforcement Learning Snake Game

> **Estado del repositorio:** el código fuente definitivo todavía no está versionado. Este repositorio contiene la planificación y documentación del proyecto, con carpetas para las fases posteriores del desarrollo.

## Tabla de contenidos
- [Descripción general](#descripción-general)
- [Objetivos de aprendizaje por refuerzo](#objetivos-de-aprendizaje-por-refuerzo)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Cómo empezar](#cómo-empezar)
- [Entrenamiento del agente](#entrenamiento-del-agente)
- [Evaluación y métricas](#evaluación-y-métricas)
- [Roadmap](#roadmap)
- [Contribución](#contribución)
- [Recursos recomendados](#recursos-recomendados)
- [Licencia](#licencia)

## Descripción general
El objetivo de este proyecto es construir un agente inteligente capaz de jugar al clásico juego de la serpiente empleando **aprendizaje por refuerzo (RL)**. A lo largo del desarrollo se irán aplicando técnicas como *Deep Q-Learning*, *experience replay* y *epsilon-greedy*, con el fin de que el agente aprenda una política que maximice la puntuación sin colisionar consigo mismo ni con los límites del tablero.

## Objetivos de aprendizaje por refuerzo
- Formular el entorno de Snake como un proceso de decisión de Markov (MDP).
- Implementar un agente basado en redes neuronales que aproxime la función de valor de acción \(Q(s, a)\).
- Experimentar con estrategias de exploración/explotación y técnicas de estabilización del aprendizaje.
- Medir el desempeño del agente a través de métricas reproducibles, como la puntuación media y la longitud media de episodios.

## Estructura del proyecto
Actualmente el repositorio incluye los siguientes elementos:

```
Reinforcement-Learning-Snake-Game/
├── Phase 2            # Espacio reservado para el código de la Fase 2 (entorno y agente base)
├── Phase 3            # Espacio reservado para el código de la Fase 3 (mejoras y experimentos)
└── README.md          # Documentación principal del proyecto
```

Cada carpeta `Phase N` se añadirá al control de versiones cuando la implementación de esa etapa esté lista. Hasta entonces actúan como marcadores de posición de los entregables planificados.

## Requisitos
Para poder ejecutar el futuro entorno de entrenamiento se recomienda tener instalado:

- Python 3.9 o superior.
- [pipenv](https://pipenv.pypa.io/) o `venv` para gestionar entornos virtuales.
- Librerías científicas habituales: `numpy`, `pandas`, `matplotlib` y `scikit-learn`.
- Librerías de deep learning: `torch` (recomendado) o `tensorflow`.
- Herramientas de desarrollo: `black`, `flake8` y `pytest` para mantener la calidad del código.

> Cuando el código esté disponible se documentarán dependencias adicionales en un fichero `requirements.txt` o `Pipfile`.

## Cómo empezar
1. Clona el repositorio:
   ```bash
   git clone https://github.com/<usuario>/Reinforcement-Learning-Snake-Game.git
   cd Reinforcement-Learning-Snake-Game
   ```
2. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows usa .venv\Scripts\activate
   ```
3. Instala las dependencias una vez se publique el fichero de requisitos.

## Entrenamiento del agente
El plan de trabajo contempla los siguientes hitos:

1. **Fase 1 – Entorno básico (no versionada):** prototipo local del juego de Snake y definición de recompensas.
2. **Fase 2 – Agente inicial:** subida prevista en la carpeta `Phase 2`. Implementará un agente DQN mínimo con *experience replay* y *target network*.
3. **Fase 3 – Mejoras y experimentación:** exploración de arquitecturas más profundas, ajustes de hiperparámetros, *curriculum learning* y recopilación de métricas.

Cada fase incluirá scripts de entrenamiento (`train.py`) y evaluación (`evaluate.py`), así como notebooks explicativos para análisis de resultados.

## Evaluación y métricas
- **Puntuación media:** promedio de manzanas consumidas por episodio.
- **Duración media:** número de pasos antes de una colisión.
- **Tasa de exploración final:** valor de epsilon cuando el entrenamiento converge.
- **Repetibilidad:** fijar semillas aleatorias y registrar parámetros de entrenamiento en archivos YAML o JSON.

Se recomienda registrar los experimentos utilizando herramientas como [Weights & Biases](https://wandb.ai/) o [TensorBoard](https://www.tensorflow.org/tensorboard).

## Roadmap
- [ ] Subir el entorno de juego y los scripts iniciales (Fase 2).
- [ ] Documentar dependencias y añadir instrucciones de ejecución paso a paso.
- [ ] Implementar un agente DQN con mejoras como *Double DQN* o *Prioritized Experience Replay*.
- [ ] Publicar resultados comparativos y gráficas.
- [ ] Añadir modos de juego humano vs. IA y una interfaz gráfica simplificada.

## Contribución
1. Haz un fork del repositorio y crea una rama descriptiva (`feature/dqn-agent`).
2. Sigue las guías de estilo indicadas en el futuro archivo `CONTRIBUTING.md`.
3. Abre un *pull request* detallando los cambios, resultados y pruebas realizadas.

## Recursos recomendados
- [Reinforcement Learning: An Introduction (Sutton & Barto)](http://incompleteideas.net/book/the-book.html)
- [Deep Q-Learning Explained (DeepMind)](https://deepmind.com/learning-resources)
- Tutoriales de [Sentdex](https://www.youtube.com/user/sentdex) sobre juegos con PyGame y RL.

## Licencia
A definir. Si contribuyes, añade una propuesta de licencia (por ejemplo, MIT o Apache-2.0) en tu pull request.
