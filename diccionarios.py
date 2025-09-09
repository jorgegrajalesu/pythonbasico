#diccionario y sets se definen igual
persona = {"Nombre":"Jorge","Apellido":"Grajales", "Edad":49, 1:"php"}
print(persona)

programas = {
    "Lenguajes": {"HTML", "Python", "C#"},
    "bases_de_datos":{"postgress", "sql server", "mysql"},
    
}

print(programas)
#para acceder a los diccionarios
print(persona["Nombre"])

#agregar elementos a los diccionarios
persona["Calle"] = "Calle 45 # 52-19"
print(persona)