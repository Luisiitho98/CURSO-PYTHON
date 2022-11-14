class Perro:

    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
        

    def ladrar(self):
        print(f"Yo {self.nombre} puedo ladrar")

class Gato(Perro):

    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)

    def maullar(self):
        print(f"Yo soy {self.nombre}, y puedo maullar")

Roco = Perro("Roco", "ladrar")
print(Roco.nombre)
print(Roco.sonido)

Roco.ladrar()

print("-------------------------------------")

Pelusa = Gato("Pelusa", "maullar")
print(Pelusa.nombre)
print(Pelusa.sonido)

Pelusa.maullar()