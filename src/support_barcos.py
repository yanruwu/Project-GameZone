import numpy as np
from os import system
import time
import random as rand

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
    """
    Clase que representa un juego de Hundir la flota, con funcionalidad para colocar barcos,
    disparar torpedos y gestionar el flujo del juego.
    
    Atributos:
    ----------
    menu_text : str
        Texto ASCII para la pantalla de inicio.
    sea : numpy.ndarray
        Matriz que representa el tablero del mar para el jugador.
    numbers_row : str
        Cadena que contiene los números de las columnas como emojis para el tablero.
    boat_options : list
        Lista con los nombres de los diferentes tipos de barcos.
    boat_lens : list
        Lista con las longitudes de cada tipo de barco.
    water_marker : str
        Símbolo que representa un disparo fallido en el tablero.
    hit_marker : str
        Símbolo que representa un disparo acertado en el tablero.
    sunk_marker : str
        Símbolo que representa un barco hundido.
    boat_marker : list
        Lista de símbolos que representan los diferentes barcos en el tablero.
    thrown_markers : list
        Lista de símbolos que indican disparos fallidos, acertados y hundidos en el tablero.
    """

    def __init__(self) -> None:
        """
        Inicializa los atributos necesarios para el juego, como el tablero del mar, las opciones
        de barcos y los marcadores para agua, impacto y hundimiento.
        """
        self.menu_text = '''
         .-. .-..-. .-..-. .-. ,'|"\   ,-.,---.    ,-.      .--.    ,---.,-.    .---.  _______  .--.           
         | | | || | | ||  \| | | |\ \  |(|| .-.\   | |     / /\ \   | .-'| |   / .-. )|__   __|/ /\ \          
____.___ | `-' || | | ||   | | | | \ \ (_)| `-'/   | |    / /__\ \  | `-.| |   | | |(_) )| |  / /__\ \____.___ 
`----==='| .-. || | | || |\  | | |  \ \| ||   (    | |    |  __  |  | .-'| |   | | | | (_) |  |  __  |`----==='
         | | |)|| `-')|| | |)| /(|`-' /| || |\ \   | `--. | |  |)|  | |  | `--.\ `-' /   | |  | |  |)|         
         /(  (_)`---(_)/(  (_)(__)`--' `-'|_| \)\  |( __.'|_|  (_)  )\|  |( __.')---'    `-'  |_|  (_)         
        (__)          (__)                    (__) (_)             (__)  (_)   (_)                             
        '''
        self.sea = np.full((10, 11), "🟦")
        numbers_column = np.array("0,1,2,3,4,5,6,7,8,9".split(","))
        self.numbers_row = " 0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣"
        self.sea[:, 0] = numbers_column
        self.boat_options = ["Portaaviones", "Acorazado", "Submarino", "Destructor", "Patrullero"]
        self.boat_lens = [5, 4, 3, 3, 2]
        self.water_marker = "💧"
        self.hit_marker = "🔥"
        self.sunk_marker = "💀"
        self.boat_marker = ["⬛", "🟫", "🟪", "🟩", "🟨"]
        self.thrown_markers = [self.water_marker, self.hit_marker, self.sunk_marker]

        # self.boat_tester = [np.array([np.array([0, 0]), np.array([0, 1]), np.array([0, 2]), np.array([0, 3]), np.array([0, 4])], dtype=object),
        #             np.array([np.array([1, 0]), np.array([2, 0]), np.array([3, 0]), np.array([4, 0])],
        #                 dtype=object),
        #             np.array([np.array([1,1]), np.array([1,2]), np.array([1,3])], dtype=object),
        #             np.array([np.array([2,1]), np.array([3,1]), np.array([4,1])], dtype=object),
        #             np.array([np.array([2,2]), np.array([2, 3])], dtype=object)]

    def check_int(self, mensaje):
        """
        Solicita al usuario ingresar un número entero, manejando posibles errores de entrada.

        Parámetros:
        -----------
        mensaje : str
            El mensaje que se mostrará al usuario para pedir la entrada.
        is_placemenu : bool, opcional
            Indica si el número ingresado es para el menú de colocación. Por defecto es False.

        Retorna:
        --------
        int
            El número entero ingresado por el usuario.
        """
        while True:
            checking = input(mensaje)
            if checking == "":
                break
            try:
                checking = int(checking)
                return checking  
            except ValueError:
                print("Error: eso no es un número válido. Intenta nuevamente.") 

    def check_positions(self, check_pos, board):
        """
        Verifica si las posiciones proporcionadas en el tablero están disponibles.

        Parámetros:
        -----------
        check_pos : numpy.ndarray
            Arreglo con las posiciones que se desean verificar.
        board : numpy.ndarray
            El tablero donde se verifican las posiciones.

        Retorna:
        --------
        bool
            Retorna True si todas las posiciones están disponibles, False en caso contrario.
        """
        bool_array = board == "🟦"
        for pos in check_pos:
            i, j = pos  
            if (i < 0 or i >= board.shape[0] or 
                j < 1 or j >= board.shape[1] or
                not bool_array[i,j]):
                return False  
        return True  
    
    def check_hitmiss(self, shot_pos, opponent_sea):
        hit = opponent_sea[shot_pos[0],shot_pos[1]] != "🟦"
        return hit
    
    def check_sunk(self, total_shots, boat_pos):
        shots_copy = [tuple(shot) for shot in total_shots]  
        boat_copy = np.array(boat_pos.copy(), dtype=object)
        # print(shots_copy)
        # print(boat_copy)
        result = np.array([all(tuple(item) in shots_copy for item in sub_array) for sub_array in boat_copy])
        # print("Result sunk;", result)
        return result
        # total_copy = total_shots.copy()
        # boat_copy = boat_pos.copy()
        # print("Boat_copy:", boat_pos)
        # for i in range(len(boat_copy)):
        #     for pos in total_copy:
        #         # print(pos)
        #         # print(boat_copy[i])
        #         if all(np.array_equal(arr, np.array(pos)) for arr in boat_copy[i]):
        #             boat_copy = np.delete(boat_copy, i, axis = 0)
        #     if len(boat_copy[i]) == 0:
        #         boat_copy[i] = True
        #     else:
        #         boat_copy[i] = False
        # if all(boat_copy):
        #     return 
        # else:
        #     return boat_copy


    def get_torpedo_user(self, opponent_sea, op_sea_4user):
        """
        Pide al usuario ingresar una coordenada para disparar un torpedo al tablero del oponente.

        Parámetros:
        -----------
        opponent_sea : numpy.ndarray
            El tablero del oponente.

        Retorna:
        --------
        numpy.ndarray
            La posición ingresada por el usuario para disparar el torpedo.
        """
        while True:
            self.print_board(op_sea_4user)
            r = self.check_int(f"Fila de disparo:\n")
            c = self.check_int(f"Columna de disparo:\n")
            c += 1
            shot_pos = np.array([[r,c]])
            if self.check_positions(shot_pos, op_sea_4user):
                break
            else:
                print("\nValor no válido\n")
                continue
        if not self.check_hitmiss(shot_pos[0], opponent_sea):
            # self.print_board(op_sea_4user)
            time.sleep(1)
            print("Agua! 💦")
            op_sea_4user[shot_pos[0][0], shot_pos[0][1]] = self.water_marker
            time.sleep(1.5)
            self.print_board(op_sea_4user)

            
        else:
            # self.print_board(op_sea_4user)
            time.sleep(1)
            print("Tocado! 🔥")
            op_sea_4user[shot_pos[0][0], shot_pos[0][1]] = self.hit_marker
            time.sleep(1)
            self.print_board(op_sea_4user)

        
        return [shot_pos[0][0], shot_pos[0][1]+1]
    



    def get_torpedo_pc(self, user_sea, user_sea_4pc):
        """
        Método vacío para la lógica de disparo de la computadora. 
        (Pendiente de implementación)
        
        Parámetros:
        -----------
        opponent_sea : numpy.ndarray
            El tablero del oponente.
        """
        while True:
            r = rand.randint(0, 9)
            c = rand.randint(1, 10)
            shot_pos = np.array([[r,c]])
            if self.check_positions(shot_pos, user_sea_4pc):
                break

        if not self.check_hitmiss(shot_pos[0], user_sea):
            print("Agua! 💦")
            user_sea[shot_pos[0][0], shot_pos[0][1]] = self.water_marker
            time.sleep(1)
            user_sea_4pc[shot_pos[0][0], shot_pos[0][1]] = self.water_marker
            
   
        else:
            print("Tocado! 🔥")
            user_sea[shot_pos[0][0], shot_pos[0][1]] = self.hit_marker
            time.sleep(1)
            user_sea_4pc[shot_pos[0][0], shot_pos[0][1]] = self.hit_marker
        self.print_board(user_sea)
        time.sleep(1.3)

        
        return [shot_pos[0][0], shot_pos[0][1]+1]

    def titlescreen(self):
        """
        Muestra la pantalla de inicio con el arte ASCII y el menú principal.
        """
        _ = system("cls")
        print(self.menu_text)

    def print_board(self, player_board):
        self.titlescreen()
        print(self.numbers_row)
        for k in range(len(player_board)):
            print("".join(player_board[k]))
    
    def colocar(self, player_sea):
        """
        Coloca los barcos en el tablero del jugador, pidiendo las coordenadas y orientaciones.

        Parámetros:
        -----------
        player_sea : numpy.ndarray
            El tablero del jugador donde se colocarán los barcos.
        """
        exit = False
        i = 0
        all_pos = []
        while i < 5 and exit == False:
            if i == 0:
                self.welcome()
                print(self.numbers_row)
                for j in range(len(player_sea)):
                    time.sleep(0.3)
                    print("".join(player_sea[j]))
            while True:
                r = self.check_int(f"Fila para el {self.boat_options[i]} (Longitud: {self.boat_lens[i]}):\n")
                c = self.check_int(f"Columna para el {self.boat_options[i]} (Longitud: {self.boat_lens[i]}):\n")
                if r is None or c is None:
                    exit = True
                    break
                c += 1
                dir = input("Dirección? (wasd)").lower()
                pos = np.array([r, c])
                pos_chain = BoatUnit(self.boat_lens[i]).coords(pos, orient=dir)
                if self.check_positions(pos_chain, player_sea):
                    break
                else:
                    continue
            if exit:
                break
        
            for pos_coord in pos_chain:
                player_sea[pos_coord[0], pos_coord[1]] = self.boat_marker[i]
            all_pos.append(pos_chain)
            i += 1
            self.print_board(player_sea)
        return all_pos

    def welcome(self):
        """
        Muestra un mensaje de bienvenida al jugador.
        """
        time.sleep(0.5)
        print("Bienvenido a Hundir la flota")
        time.sleep(0.5)
        print("\nEs hora de colocar a tu flota.")
        time.sleep(0.3)
        print("Usa los números en tu teclado y wasd para la ubicación.")
        time.sleep(0.7)


    def machine_board_gen(self, machine_sea):
        """
        Coloca los barcos en el tablero de la máquina de manera automática.

        Parámetros:
        -----------
        machine_sea : numpy.ndarray
            El tablero de la máquina donde se colocarán los barcos.
        """
        all_pos = []
        for i in range(len(self.boat_options)):
            placed = False
            while not placed:
                r = rand.randint(0, 9)
                c = rand.randint(1, 10) 
                dir = rand.choice("w,a,s,d".split(","))
                pos = np.array([r, c])
                pos_chain = BoatUnit(self.boat_lens[i]).coords(pos, orient=dir)

                if self.check_positions(pos_chain, machine_sea):
                    for pos_coord in pos_chain:
                        machine_sea[pos_coord[0], pos_coord[1]] = self.boat_marker[i]
                    placed = True
                    all_pos.append(pos_chain)

        return all_pos



    def jugar(self):
        """
        Inicia el ciclo principal del juego, mostrando el tablero y gestionando los turnos.
        """
        self.titlescreen()
        user_sea = np.copy(self.sea)
        pc_sea = np.copy(self.sea)
        pc_sea_4player = np.copy(self.sea)
        user_sea_4pc = np.copy(self.sea)
        turno = 0
        user_boats = self.colocar(user_sea)
        # boats_pc = self.boat_tester
        boats_pc = self.machine_board_gen(pc_sea)
        user_shots = []
        pc_shots = []
        while True:
            if turno%2 == 0:
                _ = system("cls")
                print(self.menu_text)
                print("\nTURNO DEL JUGADOR:\n")
                time.sleep(1.5)
                current_shot = self.get_torpedo_user(pc_sea,pc_sea_4player)
                user_shots.append([current_shot[0], current_shot[1]-1])
                # print("User shots:", user_shots)
                sunk_conds = self.check_sunk(user_shots, boats_pc)
            else:
                _ = system("cls")
                print(self.menu_text)
                print("\nTURNO DEL PC:\n")
                time.sleep(1.5)
                pc_now_shot = self.get_torpedo_pc(user_sea, user_sea_4pc)
                pc_shots.append([pc_now_shot[0], pc_now_shot[1]])
                sunk_conds = self.check_sunk(pc_shots, user_boats)               
            if all(sunk_conds):
                self.titlescreen()
                self.print_board(pc_sea_4player)
                if turno%2 == 0:
                    print("VICTORIA!!!")
                else:
                    print("has perdido...")
                break
            else:
                # print("sunk conds", sunk_conds)
                if any(sunk_conds):
                    indices_true = np.where(sunk_conds)
                    # print("algún indice true:", type(indices_true))
                    for k in range(len(indices_true[0])):
                        ind = indices_true[0][k]
                        print(indices_true)
                        pos_chain = boats_pc[ind]
                        # print(pos_chain)
                        if turno%2 == 0:
                            for pos_coord in pos_chain:
                                pc_sea_4player[pos_coord[0], pos_coord[1]] = self.sunk_marker
                        else:
                            for pos_coord in pos_chain:
                                user_sea[pos_coord[0], pos_coord[1]] = self.sunk_marker
                    self.titlescreen()
                    if turno%2 == 0:
                        self.print_board(pc_sea_4player)
                        print(f"Hundidos 💣: {len(indices_true[0])}")
                    else:
                        self.print_board(user_sea)
            time.sleep(3)
            turno += 1
        # self.print_board(pc_sea)
        # print(user_shots)
        




Boats().jugar()