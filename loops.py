#while
num = 0

while num < 10 :
    print(num)
    num += 1
else:
    print(num, "es mayor o igual")
print("el programa sigue")

#for
persona= ["Jorge", "Grajales", 48, "1976"]
for elemento in persona:
    print(elemento)
print("continua programa")

lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]
for i in lista:
    for j in i:
        print(j)