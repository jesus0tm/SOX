import random

# 1) Iniciar partido
#                                                Ranking     Tiradas
# 2) Ver resultado del ranking ---->    macia      1           2
#                                       juanjo     2           6
#                                       javier     3           8
# 3) Salir

import time
from random import randint

class Menu:
    def __init__(self):
        self.opcion_elgida = None

class Juego:
    def empezar(self):
        print("¡El juego ha comenzado!")
    

class Ranking:
    def __init__(self):
        self.registro_archivo = "registro_jugadores.txt"
        self.registro = self.cargar_registro()

    def cargar_registro(self):
        if os.path.exists(self.registro_archivo):
            with open(self.registro_archivo, "r") as file:
                registro = [line.strip() for line in file]
            return registro
        else:
            return []

    def guardar_registro(self, nombre_jugador, intentos):
        with open(self.registro_archivo, "a") as file:
            file.write(f"{nombre_jugador}: {intentos} intentos\n")

    def ver(self):
        print("Mostrando el ranking de jugadores:")
        for i, jugador in enumerate(self.registro, start=1):
            print(f"{i}. {jugador}")

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
            nombre_jugador = input("Ingrese su nombre: ")
            intentos = juego.empezar(nombre_jugador)
            ranking.guardar_registro(nombre_jugador, intentos)
        elif opcion == '2':
            ranking.ver()
        elif opcion == '3':
            print("Saliendo del programa.")
            sys.exit()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()

# Código del juego

