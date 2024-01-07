class cuenta:
    def __init__(self, numero_cuenta=0, dni_cliente=0, saldo=0.0, interes_anual=0.0):
        self.numero_cuenta = numero_cuenta
        self.dni_cliente = dni_cliente
        self.saldo = saldo
        self.interes_anual = interes_anual



    def actualizar_saldo(self):
        interes_diario = (self.interes_anual / 100) / 365
        self.saldo += self.saldo * interes_diario

    def ingresar(self, cantidad ):
        self.saldo += cantidad




    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad

    def mostrar_datos(self):
        print("Número de cuenta:", self.numero_cuenta)
        print("DNI del cliente:", self.dni_cliente)
        print("Saldo actual:", self.saldo)
        print("Interés anual:", self.interes_anual)



mi_cuenta = cuenta(numero_cuenta=976134862, dni_cliente=43482440, saldo=0, interes_anual=5.0)

import os

while True:
    
    print ("bienvenido\n\
    \n\
    ¿Que opcion deseas seleccionar ?\n\
    \n\
    1. Ingreso:\n\
    2. Retirar:\n\
    3. Mostrar:\n\
    4. Salir:\n ")
    
    opcion=int(input())
    if opcion==1:
        ingreso=float(input("¿ Cuanto dinero desea ingresar ?"))
        mi_cuenta.ingresar(ingreso)
        print("Ingreso realizado con exito")
    if opcion==2:
        retirada=float(input("¿ Cuanto dinero desea retirar ?"))
        mi_cuenta.retirar(retirada)
    if opcion==3:
            quit (mi_cuenta.mostrar_datos())
    if opcion==4:
        break



