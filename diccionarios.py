#ejemplos de diccionarios

diccionario = {
    "nombre":"Luis",
    "apellido":"Lopez",
    "edad":23,
    "ciudad":"Quito"
}
print(type(diccionario))
print(diccionario)

print(diccionario["edad"])
print("La edad de ", diccionario["nombre"], "es ", diccionario["edad"], "años")

print(diccionario.get("ciudad"))

diccionario["ciudad"] ="Latacunga"
print(diccionario)

diccionario["altura"]="1.68"
print(diccionario)

diccionario.pop("altura")
print(diccionario)

diccionario.popitem()
print(diccionario)

diccionario.popitem()
print(diccionario)

del diccionario["nombre"]
print(diccionario)

