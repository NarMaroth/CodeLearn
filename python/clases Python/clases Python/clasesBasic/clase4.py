
#          Funciones
#   Conjunto de lineas de codigo que se van a repetir durante el programa 

#   *Ventajas: -codigo / -errores / -Espacio / -Mantenimiento / +Eficiente / Estructuracion del codigo (Modularizar)

# DRY : Dont Repeat Yourself

# -  Definir funciones en infinitivos para que se diferencie de las variables
# -  Definir las funciones siempre al inicio del programa 

#           Definir Funcion:
#       "  def "nombreFuncion"():   (Cuando se deine los parametros que va a recibir la funcion solo hace falta un nombre, no hace falta el tipo de dato).

#           LLamar funcion:
#       "  nombreFuncion()  "

#   Todo lo que contenga la Funcion debe de estar identado


# EJEMPLOS:

def promediar():

    materia = input(alumno + ", ingresa la materia que deseas promediar: ")

    n1 = int(input(alumno + ", ingrese la nota del 1er trimestre de la materia " + materia + ": "))
    n2 = int(input(alumno + ", ingrese la nota del 2ndo trimestre de la materia " + materia + ": "))
    n3 = int(input(alumno + ", ingrese la nota del 3er trimestre de la materia " + materia + ": "))

    promedio = (n1+n2+n3)/3

    print(alumno + " tu promedio de " + materia + " es de " + str(promedio))

    if (promedio >= 7):
        print("Esta aprobado")
    else:
        print("Esta desaprobado")

    # Para hacer una funcion Recursiva

    opcion = input("Desea calcular otro Promedio (Y/N)")

    if (opcion.upper() == "Y"):
        promediar()
    else:
        print("Programa Finalizado ")

print("Calculadora de Promedios:")

alumno = input("Ingrese su Nombre: ")

promediar()