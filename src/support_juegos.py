import time
from tqdm import tqdm

from src.support_trivia import Trivia
from src.support_tres import Tictactoe
from src.support_barcos import Boats
from src.support_hanged import Hanged
from src.support_rps import RPS

from os import system

with open("questions.txt", encoding = "UTF-8") as archivo:
    trivia_text = archivo.read()

menu_msg = '''
__  ___ _____  _   _  _   _     ______ ______  _____  _   _  _____  _____ ______   ___   _     
|  \/  ||  ___|| \ | || | | |    | ___ \| ___ \|_   _|| \ | |/  __ \|_   _|| ___ \ / _ \ | |    
| .  . || |__  |  \| || | | |    | |_/ /| |_/ /  | |  |  \| || /  \/  | |  | |_/ // /_\ \| |    
| |\/| ||  __| | . ` || | | |    |  __/ |    /   | |  | . ` || |      | |  |  __/ |  _  || |    
| |  | || |___ | |\  || |_| |    | |    | |\ \  _| |_ | |\  || \__/\ _| |_ | |    | | | || |____
\_|  |_/\____/ \_| \_/ \___/     \_|    \_| \_| \___/ \_| \_/ \____/ \___/ \_|    \_| |_/\_____/
'''
                                                                                                
                                                                                                

class Juegos:
    def __init__(self):
        """
        Inicializa la clase Juegos, creando una lista de juegos disponibles.
        
        La lista de juegos incluye:
        - Trivia
        - Tres en Raya
        - Ahorcado
        - Piedra-Papel-Tijera
        - Hundir la Flota
        """
        self.lista_juegos = [Trivia(trivia_text), Tictactoe(), Hanged(), RPS(), Boats()]

    def useless_loading_bar(self):
        """
        Muestra una barra de carga innecesaria con descripciones variables.

        La barra de carga se actualiza en función de los pasos del progreso,
        mostrando diferentes mensajes y ajustando la velocidad de la carga
        a medida que avanza.
        """
        divisor = 2.2
        t = 0.1 / divisor
        print("\n\n\n\n\n")
        pbar = tqdm(range(500), desc=" ")
        
        for it in pbar:
            time.sleep(t)
            
            # Actualizar descripción variablemente
            if it < 5:
                new_desc = f"Iniciando... ({it}/500)"
            elif 5 <= it < 300:
                new_desc = f"Procesando... ({it}/500)"
            elif 300 <= it < 450:
                new_desc = f"Ya queda poco... ({it}/500)"
            elif 450 <= it < 470:
                new_desc = f"Casi terminando... ({it}/500)"
            else:
                new_desc = f"Finalizando... ({it}/500)"
            
            pbar.set_description(new_desc)
            
            # Cambios en los tiempos de espera
            if it == 5:
                t = 0.02 / divisor
            elif it == 300:
                t = 0.05 / divisor
            elif it == 450:
                t = 0.2 / divisor
            elif it == 470:
                t = 0.01

    def jugar(self):
        """
        Inicia el menú de juegos y permite al usuario seleccionar un juego para jugar.

        El menú se presenta en la consola y espera la entrada del usuario
        para iniciar el juego correspondiente.
        """
        _ = system("cls")
        self.useless_loading_bar()
        while True:
            _ = system("cls")
            time.sleep(0.3)
            print(menu_msg)
            time.sleep(0.6)
            print("1: Preguntados")
            time.sleep(0.2)
            print("2: Tres en raya")
            time.sleep(0.2)
            print("3: Ahorcado")
            time.sleep(0.2)
            print("4: Piedra-papel-tijera")
            time.sleep(0.2)
            print("5: Hundir la flota")
            time.sleep(0.3)
            print("\n0 : Salir\n")
            time.sleep(0.5)
            game_index = input("Seleccione juego: ")
            if game_index == "" or game_index == "0":
                break
            if int(game_index) in [1,2,3,4,5]:
                time.sleep(1)
                self.lista_juegos[int(game_index)-1].jugar()
                time.sleep(1)


Juegos().jugar()
