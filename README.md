# Juegos en Python 🎮

## Descripción

Este repositorio contiene una colección de juegos clásicos implementados en Python. Los juegos incluidos son:

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
- Juego rápido y fácil con opción a modo ampliado.
- Resultados mostrados después de cada ronda.
- Interacción sencilla a través de la consola.

### Hundir la Flota 🚢
- Dos modos de juego: jugador contra jugador y jugador contra computadora.
- Colocación de barcos en diferentes orientaciones (vertical y horizontal).
- Sistema de disparos con marcadores visuales para indicar agua, aciertos y hundimientos.
- Interfaz gráfica con emojis.

## Tecnologías Utilizadas 💻

- Python 3.11
- Librerías (NumPy, Random, Time, OS, TermColor)

## Estructura del proyecto 📂

        ├── main.py              # Ejecución principal
        ├── .txt                 # Archivos de texto con recursos para los juegos de texto
        ├── src/                 # Scripts de todos los juegos y recursos
        ├── README.md            # Descripción del proyecto

## Instalación 🛠️

1. Asegúrate de tener Python 3.11 instalado en tu sistema.
2. Clona este repositorio o descarga el archivo del código.
3. Navega al directorio del proyecto en tu terminal.
4. Ejecuta el juego con el siguiente comando:

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

1. Al iniciar el juego, se le pedirá a cada jugador que elija un modo de juego.
2. En cada ronda, se le pedirá al jugador que elija su opción (piedra, papel o tijera para el clásico).
3. El resultado se determina según las reglas del juego.
4. Se mostrará el resultado de cada ronda.
5. El juego puede repetirse para múltiples rondas.

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
- **Modo dos jugadores**: Implementar de forma sencilla un modo de dos jugadores
- **Diseño** Mejoras en la interfaz gráfica podrían elevar bastante la experiencia de juego.
- **Máquina** Implementar una manera donde la máquina pueda aprender sobre tu forma de jugar y actuar en consecuencia (Añadir una base de datos por jugador u otro método de aprendizaje por experiencia).

### Hundir la Flota 🚢
- **Mejorar la máquina**: Implementar un algoritmo capaz de disparar de forma eficiente (actualmente es aleatorio).
- **Interfaz gráfica**: Desarrollar una interfaz gráfica para mejorar la experiencia del usuario.
- **Niveles de dificultad**: Añadir diferentes niveles de dificultad para que los jugadores puedan elegir.
- **Carga interactiva**: Añadir una pequeña animación para simular el pensamiento de la máquina.

## Conclusiones ✍️
En este proyecto se han programados varios juegos clásicos con métodos aprendidos en python, de tal forma que ha servido como una puesta en práctica de los conocimientos adquiridos, además de una manera de visualizar cómo funciona nuestro proceso de pensamiento, ya que este tipo de proyectos tiene infinidad de formas de realizarse. Además de que cada uno de los juegos es diferente del anterior, por lo que uno ha de buscar enfoques diferentes para cada uno de ellos. En definitiva un buen proyecto con mucho margen para implementarle mejoras y detalles.

## 🤝 Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un pull request o una issue.
