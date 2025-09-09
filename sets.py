persona = {}
persona = {49, "Jorge", "Grajales"}
print(persona)
print(len(persona))
# añadir elementos
persona.add("Usuga")
print(persona)# estructura desordenada
persona.add("Usuga")
print(persona)#no admite repetidos
#no se puede acceder como en las listas y tuplas
#forma correcta de comprobar que un elemento existe en un set es con in
print(49 in persona)