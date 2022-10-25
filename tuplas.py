from typing import Tuple


tuplas = ("Luis", "Pedro", "Maria","Luis")
print(type(tuplas))
print(tuplas)

print(tuplas.count("Luis"))
print(tuplas.index("Luis"))

print(tuplas[3])

#transformar una tupla en una lista

lista = list(tuplas)
print(lista)

lista.append("Juan")
print(lista)

#tupla1 = Tuple(lista)

rango = range(100)
print(rango)



