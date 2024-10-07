import time
from os import system
import random as rand
from termcolor import colored
import numpy as np

with open("texto_ahorcado.txt", encoding = "UTF-8") as archivo:
    es_opt = archivo.read().split(",")

with open("hangman_text.txt", encoding = "UTF-8") as archivo:
    en_opt = archivo.read().split(",")


class Hanged:
    """
    Clase que representa el juego del Ahorcado.
    Contiene los textos de menú, dibujos del ahorcado, y mensajes de victoria y derrota.
    """
    def __init__(self) -> None:
        self.menu_text = r'''
 ▄▄▄       ██░ ██  ▒█████   ██▀███   ▄████▄   ▄▄▄      ▓█████▄  ▒█████  
▒████▄    ▓██░ ██▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ▀█  ▒████▄    ▒██▀ ██▌▒██▒  ██▒
▒██  ▀█▄  ▒██▀▀██░▒██░  ██▒▓██ ░▄█ ▒▒▓█    ▄ ▒██  ▀█▄  ░██   █▌▒██░  ██▒
░██▄▄▄▄██ ░▓█ ░██ ▒██   ██░▒██▀▀█▄  ▒▓▓▄ ▄██▒░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░
 ▓█   ▓██▒░▓█▒░██▓░ ████▓▒░░██▓ ▒██▒▒ ▓███▀ ░ ▓█   ▓██▒░▒████▓ ░ ████▓▒░
 ▒▒   ▓▒█░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ 
  ▒   ▒▒ ░ ▒ ░▒░ ░  ░ ▒ ▒░   ░▒ ░ ▒░  ░  ▒     ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░ 
  ░   ▒    ░  ░░ ░░ ░ ░ ▒    ░░   ░ ░          ░   ▒    ░ ░  ░ ░ ░ ░ ▒  
      ░  ░ ░  ░  ░    ░ ░     ░     ░ ░            ░  ░   ░        ░ ░  
                                    ░                   ░               
'''
        self.lives_str = [r"""
                    +--+
                    |  |
                        |
                        |
                        |
                        |
                    =====""",
                    r"""
                    +--+
                    |  |
                    O  |
                        |
                        |
                        |
                    =====""",
                    r"""
                    +--+
                    |  |
                    O  |
                    |  |
                        |
                        |
                    =====""",
                    r"""
                    +--+
                    |  |
                    O  |
                    /|  |
                        |
                        |
                    =====""",
                    r"""
                    +--+
                    |  |
                    O  |
                    /|\ |
                        |
                        |
                    =====""",
                    r"""
                    +--+
                    |  |
                    O  |
                    /|\ |
                    /   |
                        |
                    =====""",
                    r"""
                    +--+
                    |  |
                    O  |
                    /|\ |
                    / \ |
                    ====="""]
        self.winning_text = r'''
  _   _      _      ____           ____      _      _   _       _      ____      U  ___ u  _    
 |'| |'| U  /"\  u / __"| u     U /"___|uU  /"\  u | \ |"|  U  /"\  u |  _"\      \/"_ \/U|"|u  
/| |_| |\ \/ _ \/ <\___ \/      \| |  _ / \/ _ \/ <|  \| |>  \/ _ \/ /| | | |     | | | |\| |/  
U|  _  |u / ___ \  u___) |       | |_| |  / ___ \ U| |\  |u  / ___ \ U| |_| |\.-,_| |_| | |_|   
 |_| |_| /_/   \_\ |____/>>       \____| /_/   \_\ |_| \_|  /_/   \_\ |____/ u \_)-\___/  (_)   
 //   \\  \\    >>  )(  (__)      _)(|_   \\    >> ||   \\,-.\\    >>  |||_         \\    |||_  
(_") ("_)(__)  (__)(__)          (__)__) (__)  (__)(_")  (_/(__)  (__)(__)_)       (__)  (__)_) 
'''
        self.losing_text = r'''
 ▄▀▀▄ ▄▄   ▄▀▀█▄   ▄▀▀▀▀▄      ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄   ▄▀▀█▀▄    ▄▀▀█▄▄   ▄▀▀▀▀▄       
█  █   ▄▀ ▐ ▄▀ ▀▄ █ █   ▐     █   █   █ ▐  ▄▀   ▐ █   █   █ █ ▄▀   █ █   █  █  █ ▄▀   █ █      █      
▐  █▄▄▄█    █▄▄▄█    ▀▄       ▐  █▀▀▀▀    █▄▄▄▄▄  ▐  █▀▀█▀  ▐ █    █ ▐   █  ▐  ▐ █    █ █      █      
   █   █   ▄▀   █ ▀▄   █         █        █    ▌   ▄▀    █    █    █     █       █    █ ▀▄    ▄▀      
  ▄▀  ▄▀  █   ▄▀   █▀▀▀        ▄▀        ▄▀▄▄▄▄   █     █    ▄▀▄▄▄▄▀  ▄▀▀▀▀▀▄   ▄▀▄▄▄▄▀   ▀▀▀▀  ▄ ▄ ▄ 
 █   █    ▐   ▐    ▐          █          █    ▐   ▐     ▐   █     ▐  █       █ █     ▐                
 ▐   ▐                        ▐          ▐                  ▐        ▐       ▐ ▐                      
'''

    def print_man(self, lives, guess_string):
        """
        Muestra el estado del juego, incluyendo el ahorcado y las vidas restantes.
        
        Args:
            lives (int): Número de vidas restantes.
            guess_string (str): Representación actual de la palabra adivinada.
        """
        time.sleep(0.2)
        _ = system("cls")
        if lives == 0:
            print(colored(self.menu_text, "red"))
        else:
            print(self.menu_text)
        print(self.lives_str[-lives-1])
        print("\n")
        if lives != 0:
            print("Vidas restantes:   " + "💖"*lives+"🖤"*(6-lives))
        else:
            print(colored("Vidas restantes:   " + "💀"*6, "red"))
        
        print("         \n"+guess_string)
    
    def guess_board(self, correct_word, guess_list, word_pool, choice):
        """
        Verifica si la letra elegida está en la palabra correcta y actualiza
        la lista de letras adivinadas.

        Args:
            correct_word (list): La palabra correcta en forma de lista de caracteres.
            guess_list (list): Lista de caracteres adivinados.
            word_pool (list): Lista de letras disponibles para adivinar.
            choice (str): La letra elegida por el jugador.

        Returns:
            bool: True si la letra está en la palabra, False si no.
        """
        if choice not in word_pool:
            return None
        else:
            word_pool.pop(word_pool.index(choice))
        if choice in correct_word:
            indices = list(np.where(np.array(correct_word) == choice)[0])
            # print("Indices correctos:", indices)
            for i in indices:
                # print(guess_list[i], choice)
                guess_list[i] = choice
            return  True
        else:
            return False
        
    def win_check(self, correct_word, guess_list):
        """
        Verifica si el jugador ha ganado, es decir, si ha adivinado todas las letras de la palabra.

        Args:
            correct_word (list): La palabra correcta en forma de lista de caracteres.
            guess_list (list): Lista de caracteres adivinados.

        Returns:
            bool: True si el jugador ha ganado, False si no.
        """

        if correct_word == guess_list:
            return True
        else:
            return False


    def jugar(self):
        """
        Inicia el ciclo del juego, gestiona el flujo del juego, incluyendo
        la selección de idioma, adivinanza de letras y condiciones de victoria/derrota.
        """
        _ = system("cls")
        print(self.menu_text)
        play_again = True
        while play_again:
            hp = 6
            abcs = [*"qwertyuiopasdfghjklñzxcvbnm"]
            time.sleep(0.6)
            print("1: ES   2: EN   3: Personal   0: Salir")
            time.sleep(0.3)
            word = None
            win = False
            used = []
            while word == None:
                lang = input("Selecciona idioma\n")
                if lang == "0":
                    play_again = False
                    break
                word = [*rand.choice(es_opt)] if lang == "1" else [*rand.choice(en_opt)]if lang == "2" else None
                if lang == "3":
                    word = [*input("Introdce una palabra:\n").lower()]
                list_guesses = [*"_"*len(word)]
                # print(word, len(word), list_guesses)
                time.sleep(1)
                guess_str = " ".join(list_guesses)
                # print(guess_str)
            while hp > 0 and win == False:
                if play_again == False:
                    break
                time.sleep(1)
                guess_str = " ".join(list_guesses)
                self.print_man(lives = hp, guess_string = guess_str)
                time.sleep(0.3)
                print(f'\nYa usadas: {", ".join(used)}')
                correct = None
                while correct == None:
                    time.sleep(1)
                    letter_choice = input("\nSelecciona una letra:").lower()
                    correct = self.guess_board(correct_word = word, guess_list = list_guesses, word_pool = abcs, choice = letter_choice)
                    if correct == True:
                        time.sleep(1)
                        print("Correcto!!")
                        used.append(letter_choice)
                        win = self.win_check(correct_word = word, guess_list = list_guesses)
                        break
                    elif correct == False:
                        time.sleep(1)
                        print("Incorrecto...")
                        hp -= 1
                        used.append(letter_choice)
                        break
                        # print(correct)
                    else:
                        print("Valor introducido no válido")
                        time.sleep(0.5)
            if win == True:
                _ = system("cls")
                print(self.menu_text)
                time.sleep(1.2)
                print(self.winning_text)
            elif win == False:
                try:
                    self.print_man(hp, guess_str)
                    time.sleep(1.2)
                    print(self.losing_text)
                except:
                    pass

            answer = None
            while answer == None:
                if play_again == False:
                    break
                answer = input("Quieres jugar de nuevo? (y/n)").lower()
                play_again = True if answer == "y" else False if answer == "n" else None
