#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).
moneda1=0
moneda2=0
moneda50=0
moneda20=0
moneda10=0

moneda1=int(input("Dime cuantas monedas de 1€ tienes: "))
moneda2=int(input("Dime cuantas monedas de 2€ tienes: "))
moneda50=int(input("Dime cuantas monedas de 50 cent tienes: "))
moneda20=int(input("Dime cuantas monedas de 20 cent tienes: "))
moneda10=int(input("Dime cuantas monedas de 10 cent tienes: "))

print("Tienes una cantidad de: ", moneda1+(moneda2*2)+(moneda50*0.5)+(moneda20*0.2)+(moneda10*0.1),"€")
print("Tienes una cantidad de: ", (moneda1*100)+(moneda2*200)+(moneda50*50)+(moneda20*20)+(moneda10*10),"céntimos")