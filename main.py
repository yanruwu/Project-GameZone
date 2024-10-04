import time

while True:
    print("1: Preguntados")
    print("2: Tres en raya")
    print("3: Ahorcado")
    print("4: Piedra-papel-tijera")
    print("5: Hundir la flota")
    game_index = input("Seleccione juego o pulse enter para salir:")
    if game_index == "":
        break
    for i in range(1,6):
        if int(game_index) == i:
            time.sleep(3)
            print(i)
            time.sleep(5)
            break
