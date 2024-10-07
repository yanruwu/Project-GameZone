from os import system
import time
import random as rand
from src.loading_ani import loading_animation

class RPS:
    """
    Implementa el juego de Piedra, Papel, Tijera, y su versión ampliada
    que incluye Lagarto y Spock.
    """
    def __init__(self) -> None:
        """
        Inicializa los elementos esenciales del juego, como los textos de los
        menús, las representaciones de las opciones (Piedra, Papel, Tijera, etc.),
        y los gráficos que se muestran al ganar, perder o empatar.
        """
        self.rps_strings = [["🪨","📃","✂️"],["🪨","📃","✂️","🦎","🖖"]]
        # self.rps_strings2 = ["🪨","📃","✂️","🦎","🖖"]
        self.rps_text = [["Piedra", "Papel", "Tijera"],["Piedra", "Papel", "Tijera", "Lagarto", "Spock"]]
        # self.rps_text2 = ["Piedra", "Papel", "Tijera", "Lagarto", "Spock"]
        self.menu_text = r'''
        ____  _          _             ____                  _   _____ _  _                      
       |  _ \(_) ___  __| |_ __ __ _  |  _ \ __ _ _ __   ___| | |_   _(_)(_) ___ _ __ __ _       
  _____| |_) | |/ _ \/ _` | '__/ _` | | |_) / _` | '_ \ / _ \ |   | | | || |/ _ \ '__/ _` |_____ 
 |_____|  __/| |  __/ (_| | | | (_| | |  __/ (_| | |_) |  __/ |   | | | || |  __/ | | (_| |_____|
       |_|   |_|\___|\__,_|_|  \__,_| |_|   \__,_| .__/ \___|_|   |_| |_|/ |\___|_|  \__,_|      
                                                 |_|                   |__/                      '''
        self.extra_menu = r'''
                        _                 _                          _   
                        | |___ ___ ___ ___| |_ ___    ___ ___ ___ ___| |_ 
                        | | .'| . | .'|  _|  _| . |  |_ -| . | . |  _| '_|
                        |_|__,|_  |__,|_| |_| |___|  |___|  _|___|___|_,_|
                            |___|                      |_|              '''
        self.winning_text = r'''
    __  _____   _____    _________    _   _____    ____  ____  __
   / / / /   | / ___/   / ____/   |  / | / /   |  / __ \/ __ \/ /
  / /_/ / /| | \__ \   / / __/ /| | /  |/ / /| | / / / / / / / / 
 / __  / ___ |___/ /  / /_/ / ___ |/ /|  / ___ |/ /_/ / /_/ /_/  
/_/ /_/_/  |_/____/   \____/_/  |_/_/ |_/_/  |_/_____/\____(_)                                                                 
'''
        self.losing_text = r'''
  _                                    _ _     _            
 | |                                  | (_)   | |           
 | |__   __ _ ___   _ __   ___ _ __ __| |_  __| | ___       
 | '_ \ / _` / __| | '_ \ / _ \ '__/ _` | |/ _` |/ _ \      
 | | | | (_| \__ \ | |_) |  __/ | | (_| | | (_| | (_) | _ _ 
 |_| |_|\__,_|___/ | .__/ \___|_|  \__,_|_|\__,_|\___(_|_|_)
                   | |                                      
                   |_|                                      
'''
        self.draw_text = r'''
  ______ __  __ _____     _______ ______ 
 |  ____|  \/  |  __ \ /\|__   __|  ____|
 | |__  | \  / | |__) /  \  | |  | |__   
 |  __| | |\/| |  ___/ /\ \ | |  |  __|  
 | |____| |  | | |  / ____ \| |  | |____ 
 |______|_|  |_|_| /_/    \_\_|  |______|                                                                                 
'''
    def title_menu(self, gamemode):
        """
        Muestra el menú principal del juego con diferentes configuraciones
        según el modo de juego elegido.

        Args:
            gamemode (int): El modo de juego (1: Clásico, 2: Ampliado).
        """
        _ = system("cls")
        print(self.menu_text)
        if gamemode == 2:
            print(self.extra_menu)

    def user_choice(self, strings, gamemode):
        """
        Permite al jugador seleccionar una opción entre Piedra, Papel, Tijera (modo clásico)
        o entre Piedra, Papel, Tijera, Lagarto, Spock (modo ampliado).

        Args:
            strings (list): Las representaciones gráficas de las opciones.
            gamemode (int): El modo de juego (1: Clásico, 2: Ampliado).

        Returns:
            int: La elección del jugador, representada como un número.
        """
        if gamemode == 1:
            choice = None
            while choice == None:
                try:
                    choice = int(input(f"1: Piedra{strings[0]}   2: Papel{strings[1]}   3: Tijera{strings[2]}\n"))
                except:
                    pass
                if choice not in [1,2,3]:
                    choice = None
            return choice
        elif gamemode == 2:
            choice = None
            while choice == None:
                try:
                    choice = int(input(f"1: Piedra{strings[0]}   2: Papel{strings[1]}   3: Tijera{strings[2]}   4: Lagarto{strings[3]}   5: Spock{strings[4]}\n"))
                except:
                    pass
                if choice not in [1,2,3,4,5]:
                    choice = None
            return choice
    

    def pc_choice(self, gamemode):
        """
        pc_choice:
        Genera la elección de la computadora de manera aleatoria, dependiendo
        del modo de juego (clásico o ampliado).

        Args:
            gamemode (int): El modo de juego (1: Clásico, 2: Ampliado).

        Returns:
            int: La opción elegida por la computadora, representada como un número.
        """
        if gamemode == 1:
            return rand.choice([1,2,3])     
        elif gamemode == 2:
            return rand.choice([1,2,3,4,5])   
    
    def check_win(self, user, pc, gamemode):
        """
        Determina el resultado de la ronda, verificando si el jugador ha ganado, 
        perdido o si ha habido un empate.

        Args:
            user (int): La opción seleccionada por el jugador.
            pc (int): La opción seleccionada por la computadora.
            gamemode (int): El modo de juego (1: Clásico, 2: Ampliado).

        Returns:
            bool or None: Devuelve True si el jugador gana, False si pierde, y None si empatan.
        """
        if gamemode == 1:
            if user == pc:
                return None
            elif (user == 1 and pc == 3) or (user == 2 and pc == 1) or (user == 3 and pc == 2):
                return True
            else:
                return False
        elif gamemode == 2:
            win_cond = {
                1: [3, 4],  # Piedra gana a: Tijera y Lagarto
                2: [1, 5],  # Papel gana a: Piedra y Spock (por alguna razón)
                3: [2, 4],  # Tijera gana a: Papel y Lagarto (tiene más lógica)
                4: [2, 5],  # Lagarto gana a: Papel y Spock (Qué)
                5: [1, 3]   # Spock gana a: Piedra y Tijera (Qué x2)
            }
            if user == pc:
                return None
            else:
                return (pc in win_cond[user])
    

    def jugar(self):
        """
        Gestiona el flujo principal del juego, desde la selección del modo
        de juego hasta las rondas y la evaluación de las puntuaciones.
        Permite jugar varias rondas y reiniciar el juego si el jugador lo desea.
        """
        play_again = True
        while play_again == True:
            user_points = 0
            pc_poits = 0
            ronda = 0
            rondas = None
            while rondas == None:
                self.title_menu(1)
                try:
                    time.sleep(1)
                    modo = int(input("Modo de juego?\n1: Clásico   2: Ampliado   0: Salir\n"))
                    if modo not in [1,2,0]:
                        raise ValueError
                    elif modo == 0:
                        break
                    rondas = int(input("Cuántas rondas quieres jugar?\n"))
                except:
                    rondas = None
            if modo == 0:
                break
            while ronda < rondas:
                # if rondas == 0:
                #     break
                self.title_menu(modo)
                if ronda == rondas-1:
                    print("Ronda Final")
                else:
                    print(f'Ronda {ronda+1}')
                time.sleep(0.7)
                print("Turno del jugador")
                time.sleep(0.5)
                choice = self.user_choice(self.rps_strings[modo-1], gamemode = modo)
                time.sleep(0.5)
                print(f'Has elegido: {self.rps_text[modo-1][choice-1]}{self.rps_strings[modo-1][choice-1]}')
                time.sleep(1.6)
                self.title_menu(modo)
                if ronda == rondas-1:
                    print("Ronda Final")
                else:
                    print(f'Ronda {ronda+1}')
                time.sleep(0.7)
                print("Turno de la máquina")
                pc_c = self.pc_choice(modo)
                loading_animation(rand.choice([0.5,0.7,0.4]), "Pensando")
                time.sleep(0.3)
                print(f'La máquina eligió: {self.rps_text[modo-1][pc_c-1]}{self.rps_strings[modo-1][pc_c-1]}')
                time.sleep(1.2)
                win = self.check_win(choice, pc_c, modo)
                if win == True:
                    print("Ganaste la ronda")
                    user_points += 1
                elif win == False:
                    print("Perdiste la ronda")
                    pc_poits += 1
                elif win == None:
                    print("Empate!")
                ronda += 1
                time.sleep(1.5)
                self.title_menu(modo)
                time.sleep(0.7)
                print("\u0332".join("Puntuaciones"))
                time.sleep(0.3)
                print(f"Jugador: {user_points}")
                time.sleep(0.2)
                print(f"PC: {pc_poits}")
                input("Introduzca cualquier tecla para continuar.")
            if rondas != 0:
                if user_points > pc_poits:
                    print(self.winning_text)
                elif user_points < pc_poits:
                    print(self.losing_text)  
                elif user_points == pc_poits:
                    print(self.draw_text)    
            answer = input("Quieres jugar de nuevo? (y/n)").lower()  
            play_again = True if answer == "y" else False if answer == "n" else None