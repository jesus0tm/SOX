import os
import time
from random import randint

class Menu:
    def __init__(self):
        self.opcion_elgida = None
    
class Juego:
    def empezar(self, nombre_jugador):
        print("Hola " + nombre_jugador + ", Bienvenido al juego de azar. Comencemos.")
        numero_secreto = randint(0, 10)

        intentos = 0
        while True:
            intento = int(input("Adivina el número (entre 0 y 10): "))
            intentos += 1

            if intento == numero_secreto:
                print("¡Correcto! Has adivinado el número en", intentos, "intentos.")
                return intentos
            else:
                print("Incorrecto. Inténtalo de nuevo.")

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

def mostrar_menu():
    print("Menú:")
    print("1. Empezar juego")
    print("2. Ver ranking")
    print("3. Salir")

def main():
    menu = Menu()
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
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
