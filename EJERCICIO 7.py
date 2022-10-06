#7)Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.Por ejemplo: 1000 minutos son 16 horas y 40 minutos

min=0

minutos = int(input("Dime los minutos: "))

print(f"Horas: {int(minutos/60)} Minutos: {minutos%60}")