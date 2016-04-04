import random

class Jugador(object):
    def __init__(self,nombre):
        self.nombre = nombre
        self.puntos = 0
        self.correctas = 0
        self.incorrectas = 0

def ejercicio(b):
     num1 = random.randint(1, 10)
     num2 = random.randint(1, 10)
     print("ingrese el resultado de la suma de " + str(num1) + "+" + str(num2) + "\n")
     result = int(input("-  "))
     if result == num1+num2:
         print("muy bien!")
         player[b].puntos = player[b].puntos +3
         player[b].correctas = player[b].correctas +1
     else:
         print("te equivocaste")
         player[b].incorrectas = player[b].incorrectas +1
         if player[b].puntos <= 0:
             print("\ntienes puntaje 0 de momento!")
         else:
            player[b].puntos = player[b].puntos - 1


print("\nBienvenidos al juego de sumas y restas!\nCuantos jugadores desean jugar?: \n")
x = int(input())
player = []
validate = True
for i in range(x):
    name = raw_input("Ingrese el nombre del jugador " + str(i+1) + " ")
    player.append(Jugador(name))

i = 0
for i in range(x):
    print("\n\nEs tu turno ")
    print(player[i].nombre)
    for a in range(3):
        ejercicio(i)
    print(player[i].nombre + " obtiene " + str(player[i].puntos) + "ptos\n")
    print("correctas: " + str(player[i].correctas) + " incorrectas: " + str(player[i].incorrectas) )
