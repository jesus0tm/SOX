class Cancion:
    def __init__(self, titulo="", autor=""):
        self.titulo = titulo
        self.autor = autor

    def dame_titulo(self):
        return self.titulo

    def dame_autor(self):
        return self.autor

    def pon_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def pon_autor(self, nuevo_autor):
        self.autor = nuevo_autor



mi_cancion = Cancion(titulo="Maniaca", autor="Abraham Mateo")


print("Título:", mi_cancion.dame_titulo())
print("Autor:", mi_cancion.dame_autor())


mi_cancion.pon_titulo("Loco ")


print("Título actualizado:", mi_cancion.dame_titulo())
print("Autor:", mi_cancion.dame_autor())
