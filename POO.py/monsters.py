class Monster: 

    def __init__(self, nombre, categoria):
        self.nombre = nombre 
        self.categoria = categoria

    def myFunc(self):
        print("Yo soy", self.nombre, "y mi categoria es", self.categoria)    

mounstrito = Monster("Sullivan", "Asustador")
print(mounstrito.nombre)
mounstrito.myFunc()