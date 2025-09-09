#condicional simple
edad=int(input("Cual es tu edad? "))

if edad>=18:
    print ("Mayor de edad")

else:
    print("Menor de edad")

#condicion anidada o con el elif
if edad>=18 and edad<=59:
    print ("Mayor de edad")
elif edad>=60 and edad>=90:
    print("Adulto mayor")
else:
    print("Menor de edad")