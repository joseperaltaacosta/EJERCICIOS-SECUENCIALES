def ejercicio1(nombre:str):
    print("Ejercicio 1:")
    print ("Buenos días", nombre)
ejercicio1("Jose")
def ejercicio2(base:int,altura:int):
    print("Ejercicio 2:")
    print ("El perímetro del rectángulo es:", (2*base)+(2*altura))
    print ("El area del rectángulo es:", base*altura)
ejercicio2(5,8)
def ejercicio3(CATETO1:int,CATETO2:int):
    print("Ejercicio 3:")
    import math
    HIPOTE = math.sqrt((CATETO1*CATETO1)+(CATETO2*CATETO2))
    print("La hipotenusa del triángulo rectángulo es:", HIPOTE)
ejercicio3(3,4)
def ejercicio4(NUM1:int,NUM2:int):
    print("Ejercicio 4:")
    print("La suma de los dos números es:",NUM1+NUM2 )
    print("La resta de los dos números es:",NUM1-NUM2 )
    print("La división de los dos números es:",NUM1/NUM2 )
    print("La multiplicación de los dos números es:",NUM1*NUM2 )
ejercicio4(2,2)
def ejercicio5(VALOR:int):
    print("Ejercicio 5:")
    print("Ese valor en grados Celsius equivale a",(VALOR-32)*5/9 )
ejercicio5(255)
def ejercicio6(num:int,num2:int,num3:int):
    print("Ejercicio 6:")
    print("La media de tus tres número es: ",(num+num2+num3)/3)
ejercicio6(2,4,3)
def ejercicio7(minutos:int):
    print("Ejercicio 7:")
    print(f"Horas: {int(minutos/60)} Minutos: {minutos%60}")
ejercicio7(130)
def ejercicio8(sueldo:int,venta1:int,venta2:int,venta3:int):
    print("Ejercicio 8:")
    print("Tu dinero obtenido de las tres ventas es: ",(venta1+venta2+venta3)*1.1,"€")
    print(f"El dinero total obtenido de todo es: {((venta1+venta2+venta3)*1.1)+sueldo } €")
ejercicio8(1000,200,100,125)
def ejercicio9(compra:int):
    print("Ejercicio 9:")
    print("El dinero total que tienes que pagar es de:", compra*0.85,"€ aplicando el descuento del 15%")
ejercicio9(70)
def ejercicio10(parcial1:int,parcial2:int,parcial3:int,nota_ex_final:int,nota_trab_final:int):
    print("Ejercicio 10:")
    print("Tu calificación total es de: ", (((parcial1+parcial2+parcial3)/3)*0.55)+nota_ex_final*0.3+nota_trab_final*0.15)
ejercicio10(8,9,7,6,7)
def ejercicio20(moneda1:int,moneda2:int,moneda50:int,moneda20:int,moneda10:int):
    print("Ejercicio 20:")
    print("Tienes una cantidad de: ", moneda1+(moneda2*2)+(moneda50*0.5)+(moneda20*0.2)+(moneda10*0.1),"€")
    print("Tienes una cantidad de: ", (moneda1*100)+(moneda2*200)+(moneda50*50)+(moneda20*20)+(moneda10*10),"céntimos")
ejercicio20(3,2,4,5,10)