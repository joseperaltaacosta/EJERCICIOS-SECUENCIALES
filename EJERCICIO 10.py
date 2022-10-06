#Un alumno desea saber cual será su calificación final en la materia de algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

parcial1=0
parcial2=0
partial3=0
nota_ex_final=0
nota_trab_final=0

parcial1=int(input("¿Qué nota sacastes en el parcial 1?: "))
parcial2=int(input("¿Qué nota sacastes en el parcial 2?: "))
parcial3=int(input("¿Qué nota sacastes en el parcial 3?: "))
#((parcial1+parcial2+parcial3)/3)*0,55
nota_ex_final=int(input("Dime tu nota del examen final: "))
#nota_ex_final*0,3
nota_trab_final=int(input("Dime tu nota en el trabajo final: "))
#nota_trab_final*0,15
print("Tu calificación total es de: ", (((parcial1+parcial2+parcial3)/3)*0.55)+nota_ex_final*0.3+nota_trab_final*0.15)