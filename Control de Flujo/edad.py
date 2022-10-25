"""
Calcular la edad de una persona
Si es menor de 18 años imprimir "menor de 18 años"
Si es mayor de 18 años imprimir "menor de 18 años"
Si es mayor de 50 años imprimir "mayor de 50 años"
"""
edad = -80

if edad < 18 and edad > 1:
    print("es menor de 18")
elif edad > 18 and edad < 50:
    print("es mayor a 18")
elif edad > 50:
    print("Es mayor a 50")
else :
    print("ingrese valores enteros")    