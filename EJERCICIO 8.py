#8)Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo=0
venta1=0
venta2=0
venta3=0

sueldo=int(input("Dime tu sueldo: "))
venta1=int(input("Dime cuanto ganaste con tu primera venta: "))
venta2=int(input("Dime cuanto ganaste con tu segunda venta: "))
venta3=int(input("Dime cuanto ganaste con tu tercera venta: "))

print("Tu dinero obtenido de las tres ventas es: ",(venta1+venta2+venta3)*1.1,"€")

#print("El dinero total obtenido de todo es: ", ((venta1+venta2+venta3)*1.1)+sueldo ," €")
print(f"El dinero total obtenido de todo es: {((venta1+venta2+venta3)*1.1)+sueldo } €")