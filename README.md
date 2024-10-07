# Juegos en Python 🎮

## Descripción

Este repositorio contiene una colección de juegos clásicos implementados en Python. Los juegos incluidos son:

- **Preguntados** ❓: Un juego de preguntas y respuestas que desafía el conocimiento del jugador.
- **Tres en Raya** ❎: Un juego de estrategia para dos jugadores en un tablero 3x3.
- **Ahorcado** ⛓️: Un juego de adivinanza de palabras en el que los jugadores intentan descubrir una palabra oculta.
- **Piedra-Papel-Tijera** ✊✋✌️: Un clásico juego de manos para dos jugadores.
- **Hundir la Flota** 🚢: Un juego de estrategia donde los jugadores intentan hundir los barcos del oponente.

## Características

### Preguntados ❓
- Preguntas aleatorias seleccionadas de un archivo de texto.
- Sistema de puntuación para rastrear el rendimiento del jugador.
- Mensajes personalizados de bienvenida y finalización.

### Tres en Raya ❎
- Tablero 3x3 para dos jugadores.
- Sistema de detección de ganadores y empate.
- Interfaz simple y fácil de usar.

### Ahorcado ⛓️
- Palabras seleccionadas aleatoriamente de una lista.
- Sistema de vidas limitadas para aumentar la dificultad.
- Mensajes informativos sobre el progreso del jugador.

### Piedra-Papel-Tijera ✊✋✌️
- Juego rápido y fácil para dos jugadores.
- Resultados mostrados después de cada ronda.
- Interacción sencilla a través de la consola.

### Hundir la Flota 🚢
- Dos modos de juego: jugador contra jugador y jugador contra computadora.
- Colocación de barcos en diferentes orientaciones (vertical y horizontal).
- Sistema de disparos con marcadores visuales para indicar agua, aciertos y hundimientos.
- Interfaz gráfica con emojis.

## Tecnologías Utilizadas 💻

- Python 3.11
- Librerías (NumPy, Random, Time, ...)

## Instalación 🛠️

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Clona este repositorio o descarga el archivo del código.
3. Navega al directorio del proyecto en tu terminal.
4. Ejecuta el juego que desees iniciar con el siguiente comando:

   ```bash
   python main.py

## Cómo Jugar 🎲

### Preguntados ❓

1. Al iniciar el juego, se presentará un mensaje de bienvenida.
2. Las preguntas se seleccionan aleatoriamente de un archivo de texto.
3. El jugador debe seleccionar la respuesta correcta para acumular puntos.
4. La última ronda tiene puntuación doble, de tal forma que el jugador puede ganar aun habiendo fallado una pregunta.
5. El juego finaliza cuando se han respondido todas las preguntas, donde la victoria se decide por los puntos acumulados, o cuando el jugador decide salir.

### Tres en Raya ❎

1. Al iniciar el juego, se mostrará un tablero vacío.
2. Los jugadores alternan turnos para colocar su marca (X o O) en el tablero.
3. El juego continúa hasta que uno de los jugadores gane o el tablero se llene (empate).
4. El resultado se mostrará al final del juego.

### Ahorcado ⛓️

1. Al iniciar el juego, se seleccionará una palabra aleatoria de entre dos listas, una por idioma. El jugador también tiene la opción de escoger una palabra o salir.
2. El jugador debe adivinar las letras de la palabra dentro de un número limitado de intentos.
3. Se mostrará el progreso y el número de intentos restantes.
4. El juego termina cuando el jugador adivina la palabra o se queda sin intentos.

### Piedra-Papel-Tijera ✊✋✌️

1. Al iniciar el juego, se le pedirá a cada jugador que elija su opción (piedra, papel o tijera).
2. El resultado se determina según las reglas del juego.
3. Se mostrará el resultado de cada ronda.
4. El juego puede repetirse para múltiples rondas.

### Hundir la Flota 🚢

1. Al iniciar el juego, se mostrará un menú de inicio y se le pedirá al jugador que coloque sus barcos en el tablero.
2. Los barcos pueden ser colocados en diferentes posiciones y orientaciones.
3. Una vez colocados todos los barcos, el juego comienza con turnos alternos entre el jugador y la computadora.
4. Cada jugador dispara a las coordenadas del tablero del oponente para intentar hundir sus barcos.
5. El juego termina cuando un jugador hunde todos los barcos del oponente o viceversa.

## Next Steps 🚀

### Preguntados ❓
- **Agregar más preguntas**: Ampliar la base de datos de preguntas para incluir preguntas por temas y niveles de dificultad.
- **Sistema de puntuación**: Implementar un sistema de puntuación por temática, la cual podría dejarse almacenada, y seguir el rendimiento y ver qué temas se le dan mejor.
- **Modos de juego**: Añadir diferentes modos de juego, como cooperativo o competitivo.
- **Código**: Modularizar más el juego, de tal forma que futuras modificaciones y ampliaciones sean menos complicadas.

### Tres en Raya ❎
- **Mejorar la máquina**: Implementar un algoritmo capaz de realizar los movimientos más óptimos (actualmente es aleatorio).
- **Desafíos**: Crear desafíos con niveles de dificultad, o modos de juego donde se puedan cambiar de posición las fichas al final de la colocación inicial.
- **Diseño**: Corregir error en diseño donde las celdas se desalinean debido al uso de emoticonos para indicar la combinación ganadora.
- **Personalización**: Permitir al jugador modificar ciertas características del juego, como los marcadores o incluso el tamaño del tablero

### Ahorcado ⛓️
- **Ampliar vocabulario**: Incluir un mayor número de palabras de diferentes categorías y niveles de dificultad.
- **Estética**: Diseñar un conjunto de strings del monigote para darle un mejor aspecto al juego.
- **Temporizador**: Añadir un temporizador para aumentar la presión y la emoción del juego.

### Piedra-Papel-Tijera ✊✋✌️
- **Variantes del juego**: Incluir variantes del juego, como "Piedra-Papel-Tijera-Lagarto-Spock".
- **Estadísticas de juego**: Llevar un registro de las victorias y derrotas del jugador para mostrar el rendimiento.
- **Torneos**: Implementar un sistema de torneos para que los jugadores puedan competir entre sí.

### Hundir la Flota 🚢
- **Mejorar la máquina**: Implementar un algoritmo capaz de disparar de forma eficiente (actualmente es aleatorio).
- **Interfaz gráfica**: Desarrollar una interfaz gráfica para mejorar la experiencia del usuario.
- **Niveles de dificultad**: Añadir diferentes niveles de dificultad para que los jugadores puedan elegir.
