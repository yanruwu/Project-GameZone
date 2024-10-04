import re
import random as rand
import time
from os import system

with open("questions.txt", encoding = "UTF-8") as archivo:
    trivia_text = archivo.read()

class Trivia:
    def __init__(self, complete_string):
        time.sleep(0.5)
        print("Bienvenido al preguntados!")
        time.sleep(1)
        print("Vamos a comenzar")
        time.sleep(1)
        pattern_q = r"(.*?)%(.*?)%(.*?)%(.*?)%(.*?)%"
        self.q_set = re.findall(pattern = pattern_q, string = complete_string)

    def generate(self):
        index = rand.randint(0,len(self.q_set)-1)
        question = list(self.q_set[index])[0]
        answer = list(self.q_set[index])[1]
        inc1 = list(self.q_set[index])[2]
        inc2 = list(self.q_set[index])[3]
        inc3 = list(self.q_set[index])[4]
        return [question, answer, inc1, inc2, inc3]
    
    def jugar_trivia(self):

        play_again = "y"
        while play_again.lower() == "y":
            points = 0
            while True:
                try:
                    rondas = int(input("Cuántas rondas quieres jugar?"))
                    break
                except:
                    continue
            if rondas == 0:
                break
            i = 1
            while i<=rondas:
                q_set_round = self.generate()
                q_set_options = q_set_round[1::]
                q_set_options_rand = rand.sample(q_set_options, k = 4)
                if i == rondas:
                    print("Ronda final")
                else:
                    print(f"Ronda {i}")
                print(q_set_round[0])
                print(f'1: {q_set_options_rand[0]} 2: {q_set_options_rand[1]} 3: {q_set_options_rand[2]} 4: {q_set_options_rand[3]}')

                user_choice = int(input("Escoja una opción (1-4)"))

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
                i+=1
            print(f'Puntuación final: {points}')
            time.sleep(1)
            if points == rondas:
                print("Has ganado!! 🥳🎉")
            else:
                print("Perdedor...")
            time.sleep(2)

            play_again = input("Quieres jugar de nuevo? (y/n)")
            _ = system("cls")

Trivia(trivia_text).jugar_trivia()
