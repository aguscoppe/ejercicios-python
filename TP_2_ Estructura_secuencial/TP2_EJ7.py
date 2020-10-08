#EJERCICIO 7

totalSegundos = int(input("Ingrese los segundos "))
seg = totalSegundos % 60
minu = (totalSegundos // 60) % 60
hor = ((totalSegundos // 60) //  60) % 24
dias = ((totalSegundos // 60) //  60) // 24
print(totalSegundos, "segundos equivalen a", dias, "días",
hor, "horas", minu, "minutos y", seg, "segundos")