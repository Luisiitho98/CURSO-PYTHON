from ssl import ALERT_DESCRIPTION_ILLEGAL_PARAMETER


class Carro:

    def __init__(self, color, cilindraje, marca) :
        self.color = color
        self.cilindraje = cilindraje
        self.marca = marca

    def acelerrar (self):
        print("El carro", self.marca, "puede acelerar")

    def frenar(self):
        print("El carro", self.marca, "puede frenar")

    def girarAlaDerecha(self):
        print("El carro", self.marca, "puede girar a la derecha")            
        
    def girarAlaIzquierda(self):
        print("El carro", self.marca, "puede girar a la izquierda")

carro1 = Carro("Suzuki")
print(carro1.marca)
carro1.acelerar

