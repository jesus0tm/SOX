class TratamientoFichero():

    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero


    def write_file(self, line_to_write):
        f = open(self.nombre_fichero, "a")
        f.write("Now the file has more content!")
        f.close()


    def read_file(self):
        f = open (self.nombre_fichero, "r")
        print(f.read)




if __name__ == "__main__":
    f = TratamientoFichero("prueba")
    f.write_file("Pepito 10")
    f.read_file()

    print("hola")