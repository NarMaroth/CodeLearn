print("//////////////////// Inicio del Programa /////////////////////")

n1 = 10

n2 = 10
 
n3 = 7

promedio = (n1+n2+n3)/3

if (promedio >= 9 ):
    print("Aprobado con Exelencia")
    pass #se emplea cuando queres que el programa no mande error al leer una linea. Ejemplo: Al dejar el cuerpo de un IF vacio daria error pero su pones unicamente PASS no

elif (promedio>=7 and promedio<9):
    print("Aprobado")

elif (promedio > 4 and promedio < 7):
    print("Desaprobado: Diciembre")

else:
    print("Desaprobado: Marzo")



print("//////////////////// Fin del Programa /////////////////////")