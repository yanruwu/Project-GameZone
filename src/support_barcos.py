import numpy as np
from os import system
import time

class BoatUnit:
    def __init__(self, boatlen : int) -> None:
        self.boatlen = boatlen
        self.boatstring = "🟫"*boatlen

    def coords(self, pos, orient:str):
        coord = np.empty(self.boatlen, dtype=object)
        coord[0] = pos
        r, c = pos
        l = self.boatlen
        for i in range(1,l):
            if orient == "d":
                coord[i] = np.array([r,c+i]) # R
            elif orient == "s":
                coord[i] = np.array([r+i,c]) # D
            elif orient == "a":
                coord[i] = np.array([r,c-i]) # L
            elif orient == "w":
                coord[i] = np.array([r-i,c]) # U
        return coord
        
    
    def string(self):
        return self.boatstring


class Boats:
    def __init__(self) -> None:
        self.menu_text = '''

         .-. .-..-. .-..-. .-. ,'|"\   ,-.,---.    ,-.      .--.    ,---.,-.    .---.  _______  .--.           
         | | | || | | ||  \| | | |\ \  |(|| .-.\   | |     / /\ \   | .-'| |   / .-. )|__   __|/ /\ \          
____.___ | `-' || | | ||   | | | | \ \ (_)| `-'/   | |    / /__\ \  | `-.| |   | | |(_) )| |  / /__\ \____.___ 
`----==='| .-. || | | || |\  | | |  \ \| ||   (    | |    |  __  |  | .-'| |   | | | | (_) |  |  __  |`----==='
         | | |)|| `-')|| | |)| /(|`-' /| || |\ \   | `--. | |  |)|  | |  | `--.\ `-' /   | |  | |  |)|         
         /(  (_)`---(_)/(  (_)(__)`--' `-'|_| \)\  |( __.'|_|  (_)  )\|  |( __.')---'    `-'  |_|  (_)         
        (__)          (__)                    (__) (_)             (__)  (_)   (_)                             
        '''

        self.sea = np.full((10,10), "🟦")
        self.boat_options = ["Portaaviones", "Acorazado", "Submarino", "Destructor", "Patrullero"]
        self.boat_lens = [5,4,3,3,2]                    
        self.water_marker = "💧"
        self.hit_marker = "🔥"
        self.sunk_marker = "❌"
        self.boat_marker = ["⬛","🟫","🟪","🟩","🟨"]
        self.thrown_markers = [self.water_marker, self.hit_marker, self.sunk_marker]
    def check_int(self, mensaje):
            while True:
                checking = input(mensaje)  
                try:
                    checking = int(checking)
                    return checking  
                except ValueError:
                    print("Error: eso no es un número válido. Intenta nuevamente.") 

    def check_positions(self, check_pos, board):
        bool_array = board == "🟦"
        for pos in check_pos:
            i, j = pos  
            if not bool_array[i, j]:  
                return False  
        return True  


            
    def get_torpedo_user(self, opponent_sea):
        non_hit_mask = opponent_sea == "🟦"
        while True:
            torp_pos_str = input("Dónde quieres disparar?")
            torp_pos = np.array(torp_pos_str.split(","))
            allowed = non_hit_mask[torp_pos]
            if allowed:
                break
            else:
                continue
        return torp_pos
    
    def get_torpedo_pc(self, opponent_sea):
        pass
        
    def titlescreen(self):
        _ = system("cls")
        print(self.menu_text)

    def colocar(self, player_sea):
        for i in range(5):
            if i == 0:
                self.welcome()
                for j in range(len(player_sea)):
                    time.sleep(0.3)
                    print("".join(player_sea[j]))
            while True:
                pos_string = input(f"Coordenadas para el {self.boat_options[i]} (Longitud: {self.boat_lens[i]}):\n")
                pos = np.array(list(map(int, pos_string.split(","))))
                dir = input("Dirección? (wasd)").lower()
                pos_chain = BoatUnit(self.boat_lens[i]).coords(pos, orient = dir)
                if self.check_positions(pos_chain, player_sea):
                    break
                else:
                    continue
                    
        
            for pos_coord in pos_chain:
                player_sea[pos_coord[0], pos_coord[1]] = self.boat_marker[i]
            _ = system("cls")
            print(self.menu_text)
            for k in range(len(player_sea)):
                print("".join(player_sea[k]))


    
    def welcome(self):
        print("Bienvenido a Hundir la flota")

    def options_print(self):
        for boat in self.boat_options:
            print(f'{len(boat)}')

    def jugar(self):
        self.titlescreen()
        user_sea = self.sea
        pc_sea = self.sea
        turno = 0
        self.colocar(user_sea)

Boats().jugar()