#3)Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math
CATETO1=0
CATETO2=0
CATETO1 = (int)(input("Dime el cateto 1:"))
CATETO2 = (int)(input("Dime el cateto 2:"))
HIPOTE = math.sqrt((CATETO1*CATETO1)+(CATETO2*CATETO2))
print("La hipotenusa del triángulo rectángulo es:", HIPOTE)