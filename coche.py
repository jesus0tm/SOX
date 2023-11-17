class coche:
    def  __init__(self, velocidad, motor, ruedas, puertas):
        self.motor = motor 
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
    

c1 = coche('V20', '4', '4', '120 km/h')

print (c1.motor)
print (c1.ruedas)
print (c1.puertas)
print (c1.velocidad)