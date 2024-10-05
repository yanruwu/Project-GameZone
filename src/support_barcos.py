import numpy as np
from os import system
import time

class Boats:
    def __init__(self) -> None:
        self.sea = np.full((10,10), "🟦")
        self.menu_text = '''

         .-. .-..-. .-..-. .-. ,'|"\   ,-.,---.    ,-.      .--.    ,---.,-.    .---.  _______  .--.           
         | | | || | | ||  \| | | |\ \  |(|| .-.\   | |     / /\ \   | .-'| |   / .-. )|__   __|/ /\ \          
____.___ | `-' || | | ||   | | | | \ \ (_)| `-'/   | |    / /__\ \  | `-.| |   | | |(_) )| |  / /__\ \____.___ 
`----==='| .-. || | | || |\  | | |  \ \| ||   (    | |    |  __  |  | .-'| |   | | | | (_) |  |  __  |`----==='
         | | |)|| `-')|| | |)| /(|`-' /| || |\ \   | `--. | |  |)|  | |  | `--.\ `-' /   | |  | |  |)|         
         /(  (_)`---(_)/(  (_)(__)`--' `-'|_| \)\  |( __.'|_|  (_)  )\|  |( __.')---'    `-'  |_|  (_)         
        (__)          (__)                    (__) (_)             (__)  (_)   (_)                             
        '''

        self.boat_options = [["Portaaviones", "Acorazado", "Submarino", "Destructor", "Patrullero"],
                             ["🟫🟫🟫🟫🟫", "🟫🟫🟫🟫", "🟫🟫🟫",   "🟫🟫🟫",    "🟫🟫"]]

    def get_torpedo(self, x, y, board):
        board[x][y] = "x"

    def place_boat(self, boatid, orient, board, pos):
        c, r = pos.split(",")
        c = int(c)
        r = int(r)
        l = len(boatid)

        if orient == "d":
            board[r,c:c+l] = "🟫" # HR
        elif orient == "s":
            board[r:c+l,c] = "🟫" # VD
        elif orient == "a":
            board[r,c-(l-1):c+1] = "🟫" # HL
        elif orient == "w":
            board[r-(l-1):r+1,c] = "🟫" # VU
        ## Diccionario (?)
        return board

    def menu_colocar(self, player_sea, turn):
        _ = system("cls")
        print(self.menu_text)
        self.welcome()
        for i in range(len(player_sea)):
            if turn == 0:
                time.sleep(0.3)
            print("".join(player_sea[i]))

        for y in range(len(self.boat_options[0])):
            time.sleep(0.15)
            print(f'{self.boat_options[0][y]}: {self.boat_options[1][y]}')

    # def current_sea(self, player_sea, turn):
    #     _ = system("cls")
    #     print(self.menu_text)
    #     if turn == 0:
    #         self.welcome()
    #     for i in range(len(player_sea)):
    #         if turn == 0:
    #             time.sleep(0.3)
    #         print("".join(player_sea[i]))
    #     if turn == 0:
    #         print("\n")
    #         for y in range(len(self.boat_options[0])):
    #             time.sleep(0.15)
    #             print(f'{self.boat_options[0][y]}: {self.boat_options[1][y]}')

    def welcome(self):
        print("Bienvenido a Hundir la flota")

    def options_print(self):
        for boat in self.boat_options:
            print(f'{len(boat)}')

    def jugar(self):
        # _ = system("cls")
        # print(self.menu_text)
        user_sea = self.sea
        pc_sea = self.sea
        user_boats = self.boat_options[1]
        pc_boats = self.boat_options[1]
        turno = 0
        for i in range(1,5):
            self.menu_colocar(user_sea, turn = turno)
            turno += 1
            id_barco = user_boats[int(input("Qué barco quieres colocar?"))-1]
            dir = input("Dirección? (wasd)").lower()
            user_choice_pos = input("Posición?")
            user_sea = self.place_boat(id_barco, dir, user_sea, user_choice_pos)
            self.menu_colocar(user_sea, turn = turno)


Boats().jugar()