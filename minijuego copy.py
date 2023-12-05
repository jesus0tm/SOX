# 1) Iniciar partido
#                                                Ranking     Tiradas
# 2) Ver resultado del ranking ---->    macia      1           2
#                                       juanjo     2           6
#                                       javier     3           8
# 3) Salir
import time

class Menu:
    def __init__(self):
        self.opcion_elgida = None

class Juego:
    def empezar(self):
        print("¡El juego ha comenzado!")

class Ranking:
    def ver(self):
        print("Mostrando el ranking de jugadores.")

class TratamientoFichero:
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero

    def write_file(self, line_to_write):
        with open(self.nombre_fichero, "a") as f:
            f.write(line_to_write + "\n")

    def read_file(self):
        with open(self.nombre_fichero, "r") as f:
            print(f.read())


def mostrar_menu():
    print("Menú:")
    print("1. Empezar juego")
    print("2. Ver ranking")
    print("3. Salir")

import sys

def main():
    juego = Juego()
    ranking = Ranking()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")
        if opcion == '1':
            juego.empezar()
            break
        elif opcion == '2':
            ranking.ver()
            break
        elif opcion == '3':
            print("Saliendo del programa.")
            sys.exit()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()




 
from random import randint

numero_secreto = randint(0, 10)

while True:
    intento = int(input("Adivina el número (entre 0 y 10): "))


    if intento == numero_secreto:
        print("¡Correcto! Has adivinado el número.")
        break
    else:
        print("Incorrecto. Inténtalo de nuevo.")

