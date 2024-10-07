import re
import random as rand
import time
from os import system
from termcolor import colored

class Tictactoe:
    """
    Clase para gestionar el juego de Tres en Raya (Tic-Tac-Toe).
    """

    def __init__(self):
        """
        Inicializa el juego con un tablero vacío, un menú de bienvenida, 
        marcadores y combinaciones ganadoras.
        """
        self.board = [' '] * 9
        self.menu_text = '''
       .___________..______       _______      _______.    _______ .__   __.    .______           ___   ____    ____  ___            
       |           ||   _  \     |   ____|    /       |   |   ____||  \ |  |    |   _  \         /   \  \   \  /   / /   \           
 ______`---|  |----`|  |_)  |    |  |__      |   (----`   |  |__   |   \|  |    |  |_)  |       /  ^  \  \   \/   / /  ^  \   ______ 
|______|   |  |     |      /     |   __|      \   \       |   __|  |  . `  |    |      /       /  /_\  \  \_    _/ /  /_\  \ |______|
           |  |     |  |\  \----.|  |____ .----)   |      |  |____ |  |\   |    |  |\  \----. /  _____  \   |  |  /  _____  \        
           |__|     | _| `._____||_______||_______/       |_______||__| \__|    | _| `._____|/__/     \__\  |__| /__/     \__\       
                                                                                                                                     

'''
        self.markers = ["X", "O"]
        self.winning_combos = [(0,1,2), (3,4,5), (6,7,8),
                               (0,3,6), (1,4,7), (2,5,8),
                               (0,4,8), (2,4,6)] ## Cambiar a función para check independientemente del size del tablero

    def welcome(self):
        """
        Muestra un mensaje de bienvenida y espera un momento antes de continuar.
        """
        time.sleep(0.5)
        print("Bienvenido al tres en raya!")
        time.sleep(1)

    def print_board(self):
        """
        Limpia la pantalla y muestra el estado actual del tablero de juego.
        """
        _ = system("cls")
        print(self.menu_text)
        print(f'''
           |     |     
        {self.board[0]}  |  {self.board[1]}  |  {self.board[2]}  
      _____|_____|_____
           |     |     
        {self.board[3]}  |  {self.board[4]}  |  {self.board[5]}  
      _____|_____|_____
           |     |     
        {self.board[6]}  |  {self.board[7]}  |  {self.board[8]}  
           |     |     
''')

    def get_move(self, playerid, marker):
        """
        Permite al jugador seleccionar una casilla válida en el tablero.

        Args:
            playerid (str): Identificador del jugador (Jugador 1 o Jugador 2).
            marker (str): El marcador del jugador actual ('X' o 'O').

        El método solicita la entrada del jugador hasta que se elige una
        casilla válida, y luego actualiza el tablero.
        """
        while True:
            try:
                pos = int(input(f'Selecciona casilla, {playerid}\n')) - 1
                if pos in [x for x in range(9)] and self.board[pos] == " ":
                    self.board[pos] = marker
                    break
                else:
                    self.print_board()
                    print("Casilla no válida")
            except ValueError:
                print("Valor no válido")
    
    def check_winner(self, marker):
        """
        Verifica si el marcador actual ha ganado el juego.

        Args:
            marker (str): El marcador a verificar ('X' o 'O').

        Returns:
            tuple or None: Si el jugador ha ganado, devuelve la combinación ganadora;
            de lo contrario, devuelve None.
        """
        for combo in self.winning_combos:
            if all(self.board[pos] == marker for pos in combo):
                return combo

    def jugar(self):
        """
        Inicia el flujo del juego de Tres en Raya. Permite al jugador seleccionar
        entre jugar contra la computadora o contra otro jugador, y gestiona el 
        flujo del juego hasta que se determina un ganador o se agotan los turnos.
        """
        _ = system("cls")
        print(self.menu_text)

        self.welcome()
        self.print_board()
        time.sleep(1)
        play_again = 1
        while play_again == 1:
            self.board = [' '] * 9 ## Crear local
            print("1: Contra PC  2: Contra un amigo  0: Salir")
            while True:
                try:
                    gamemode = int(input("Elige modo de juego:: "))
                    if gamemode in [1, 2]:
                        break
                    else:
                        continue
                except:
                    pass
            if gamemode == 0:
                break
            eleccion = "Contra PC" if gamemode == 1 else "Contra amigo"
            time.sleep(1)
            print(f"Has escogido: {eleccion}")
            user_marker = self.markers[0]
            friend_marker = self.markers[1]

            turno = 0
            for i in range(9):
                self.print_board()
                if turno % 2 == 0:
                    self.get_move("Jugador 1", user_marker)
                    if self.check_winner(user_marker):
                        winner_combo = self.check_winner(user_marker)
                        for pos in winner_combo:
                            self.board[pos] = "❌"
                        self.print_board()
                        print("Gana el Jugador 1!")
                        break
                else:
                    if gamemode == 2:
                        self.get_move("Jugador 2", friend_marker)
                        if self.check_winner(friend_marker):
                            winner_combo = self.check_winner(friend_marker)
                            for pos in winner_combo:
                                self.board[pos] = "⭕"
                            self.print_board()
                            print("Gana el jugador 2!")
                            break
                    else:
                        while True:
                            pospc = rand.choice([x for x in range(9)])
                            if self.board[pospc] == " ":
                                time.sleep(rand.choice([0.5, 0.75, 1, 1.25]))
                                self.board[pospc] = friend_marker
                                break
                            else:
                                continue
                                
                turno += 1
            while True:
                response = input("¿Quieres jugar de nuevo? (y/n)")
                if response.lower() == "y":
                    _ = system("cls")
                    break
                elif response.lower() == "n":
                    play_again = 0
                    _ = system("cls")
                    break
                else: 
                    continue
