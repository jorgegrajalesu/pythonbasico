#las listas, estructuran datos
lista_mes = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
print(lista_mes)
print(len(lista_mes))

persona= ["Jorge", "Grajales", 48, "1976"]
print(persona)
#para mostrar un valor, ej el 48
print(persona[2])
#mostrar cada elemento de la lista persona
print(persona[0])
print(persona[1])
print(persona[2])
print(persona[3])
print(persona[-1])
print(persona[-2])
print(persona[-3])
print(persona[-4])

#la lista se puede asignar
nombre, apellido, edad, fecha = persona
print(edad)