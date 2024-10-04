import re
import random as rand
import time
from os import system

with open("questions.txt", encoding = "UTF-8") as archivo:
    trivia_text = archivo.read()

class Trivia:
    """
    Clase para gestionar una trivia a partir de preguntas leídas de un archivo de texto.

    Atributos:
    ----------
    q_set : list
        Lista de tuplas que contiene las preguntas, respuestas correctas y respuestas incorrectas extraídas del archivo de texto.
    """

    def __init__(self, complete_string):
        """
        Inicializa la clase Trivia extrayendo preguntas y respuestas a partir de un string dado.
        
        Parámetros:
        -----------
        complete_string : str
            String que contiene todas las preguntas y respuestas en un formato específico,
            donde cada bloque está separado por el carácter '%' con el siguiente formato:
            pregunta%respuesta_correcta%respuesta_incorrecta1%respuesta_incorrecta2%respuesta_incorrecta3%.
        """
        pattern_q = r"(.*?)%(.*?)%(.*?)%(.*?)%(.*?)%"
        self.q_set = re.findall(pattern = pattern_q, string = complete_string)
        self.menu_text = '''
          _____   _____   ______  _____  _    _  _   _  _______         _____    ____    _____        
         |  __ \ |  __ \ |  ____|/ ____|| |  | || \ | ||__   __| /\    |  __ \  / __ \  / ____|       
  ______ | |__) || |__) || |__  | |  __ | |  | ||  \| |   | |   /  \   | |  | || |  | || (___  ______ 
 |______||  ___/ |  _  / |  __| | | |_ || |  | || . ` |   | |  / /\ \  | |  | || |  | | \___ \|______|
         | |     | | \ \ | |____| |__| || |__| || |\  |   | | / ____ \ | |__| || |__| | ____) |       
         |_|     |_|  \_\|______|\_____| \____/ |_| \_|   |_|/_/    \_\|_____/  \____/ |_____/        
                                                                                                      
                                                                                                      
'''
        self.victoria = '''

 $$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$\ $$$$$$$$\ $$$$$$$$\ 
$$  __$$\ $$  __$$\ $$$\  $$ |$$  __$$\ $$  __$$\\__$$  __|$$  _____|
$$ /  \__|$$ /  $$ |$$$$\ $$ |$$ /  $$ |$$ /  \__|  $$ |   $$ |      
$$ |$$$$\ $$$$$$$$ |$$ $$\$$ |$$$$$$$$ |\$$$$$$\    $$ |   $$$$$\    
$$ |\_$$ |$$  __$$ |$$ \$$$$ |$$  __$$ | \____$$\   $$ |   $$  __|   
$$ |  $$ |$$ |  $$ |$$ |\$$$ |$$ |  $$ |$$\   $$ |  $$ |   $$ |      
\$$$$$$  |$$ |  $$ |$$ | \$$ |$$ |  $$ |\$$$$$$  |  $$ |   $$$$$$$$\ 
 \______/ \__|  \__|\__|  \__|\__|  \__| \______/   \__|   \________|
                                                                     
                                                                     
                                                                     
'''
        self.perdida = '''

     _ __        ,----.                             .=-.-.  ,-,--.  ,--.--------.     ,----.                 
  .-`.' ,`.   ,-.--` , \  .-.,.---.    _,..---._   /==/_ /,-.'-  _\/==/,  -   , -\ ,-.--` , \                
 /==/, -   \ |==|-  _.-` /==/  `   \ /==/,   -  \ |==|, |/==/_ ,_.'\==\.-.  - ,-./|==|-  _.-`                
|==| _ .=. | |==|   `.-.|==|-, .=., ||==|   _   _\|==|  |\==\  \    `--`\==\- \   |==|   `.-.                
|==| , '=',|/==/_ ,    /|==|   '='  /|==|  .=.   ||==|- | \==\ -\        \==\_ \ /==/_ ,    /                
|==|-  '..' |==|    .-' |==|- ,   .' |==|,|   | -||==| ,| _\==\ ,\       |==|- | |==|    .-'                 
|==|,  |    |==|_  ,`-._|==|_  . ,'. |==|  '='   /|==|- |/==/\/ _ |      |==|, | |==|_  ,`-._ .=.  .=.  .=.  
/==/ - |    /==/ ,     //==/  /\ ,  )|==|-,   _`/ /==/. /\==\ - , /      /==/ -/ /==/ ,     /:=; ::=; ::=; : 
`--`---'    `--`-----`` `--`-`--`--' `-.`.____.'  `--`-`  `--`---'       `--`--` `--`-----``  `=`  `=`  `=`  

'''

    def welcome(self):
        """
        Muestra un mensaje de bienvenida al jugador con un breve retraso entre líneas.
        """
        _ = system("cls")
        time.sleep(0.5)
        print(self.menu_text)
        time.sleep(0.5)
        print("Bienvenido al preguntados!")
        time.sleep(1)
        print("Vamos a comenzar")
        time.sleep(1)

    def generate(self):
        """
        Selecciona una pregunta aleatoria del conjunto de preguntas.

        Retorna:
        --------
        list : 
            Lista que contiene la pregunta, la respuesta correcta, y tres respuestas incorrectas.
        """
        index = rand.randint(0, len(self.q_set)-1)
        question = list(self.q_set[index])[0]
        answer = list(self.q_set[index])[1]
        inc1 = list(self.q_set[index])[2]
        inc2 = list(self.q_set[index])[3]
        inc3 = list(self.q_set[index])[4]
        return [question, answer, inc1, inc2, inc3]

    def jugar(self):
        """
        Controla el flujo principal del juego, permitiendo al usuario jugar rondas de trivia.

        - Se pregunta al jugador cuántas rondas quiere jugar.
        - Para cada ronda, selecciona una pregunta aleatoria y las respuestas correspondientes.
        - Muestra las opciones en orden aleatorio.
        - Evalúa si la respuesta del jugador es correcta o incorrecta, actualizando la puntuación.
        - Ofrece al jugador la posibilidad de jugar de nuevo tras finalizar las rondas.

        Retorna:
        --------
        None
        """
        self.welcome()
        play_again = "y"
        while play_again.lower() == "y":
            points = 0
            while True:
                try:
                    rondas = int(input("Cuántas rondas quieres jugar? "))
                    break
                except:
                    continue
            if rondas == 0:
                break
            i = 1
            while i <= rondas:
                q_set_round = self.generate()
                q_set_options = q_set_round[1::]
                q_set_options_rand = rand.sample(q_set_options, k=4)
                if i == rondas:
                    print("Ronda final")
                else:
                    print(f"Ronda {i}")
                print(q_set_round[0])
                print(f'1: {q_set_options_rand[0]} 2: {q_set_options_rand[1]} 3: {q_set_options_rand[2]} 4: {q_set_options_rand[3]}')
                while True:
                    try:
                        user_choice = int(input("Escoja una opción (1-4): "))
                        if int(user_choice) == 0:
                            continue
                        break
                    except:
                        continue

                if q_set_options_rand[user_choice-1] == q_set_options[0]:
                    print("CORRECTO!!")
                    points += 1
                else:
                    print("INCORRECTO!")
                    time.sleep(1)
                    print(f"La respuesta correcta era: {q_set_options[0]}")
                self.q_set.pop(self.q_set.index(tuple(q_set_round)))
                time.sleep(1)
                if i == rondas:
                    time.sleep(1)
                    break
                print(f"Puntuación actual: {points}")
                time.sleep(1)
                i += 1
            print(f'Puntuación final: {points}')
            time.sleep(1)
            if points == rondas:
                print(self.victoria)
            else:
                print(self.perdida)
            time.sleep(2)

            play_again = input("Quieres jugar de nuevo? (y/n): ")
            _ = system("cls")
            print(self.menu_text)
        _ = system("cls")