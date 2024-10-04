import time
from src.support_trivia import Trivia
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
                                                                                                
                                                                                                

class juegos:
    def __init__(self):
        self.lista_juegos = [Trivia(trivia_text), 0, 0, 0, 0]
    
    def jugar(self):
        _ = system("cls")
        while True:
            print(menu_msg)
            print("1: Preguntados")
            print("2: Tres en raya")
            print("3: Ahorcado")
            print("4: Piedra-papel-tijera")
            print("5: Hundir la flota")
            print("\n0 : Salir\n")
            game_index = input("Seleccione juego: ")
            if game_index == "" or game_index == "0":
                break
            if int(game_index) in [1,2,3,4,5]:
                time.sleep(1)
                self.lista_juegos[int(game_index)-1].jugar()
                time.sleep(1)


juegos().jugar()
