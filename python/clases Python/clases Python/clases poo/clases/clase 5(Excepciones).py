
#                               EXCEPCIONES
# Una excepcion es un error que se da mientras se esta ejecutando el programa

try:
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))

    promedio = n1/n2
    print(promedio)

#  En el caso de que se intente dividir por 0 y salga un error por ello(ZeroDivisionError) ejecutara el cuerpo 
# de la exepcion evitando que se detenga el programa
except ZeroDivisionError: 
    print("No se puede dividir por cero")

# De ingresarse algo que no sea un integer en n1 o n2 saltara el error ValueError
except ValueError:
    print("Ingrese un numero entero")

# Para cualquier error, no especificar en el except
except:
    print("Se a producido un error")


# El Finally siempre se ejecuta al final, sin importar que haya habido error o no
finally:
    print("El programa continua")


#                           EXCEPCIONES MAS COMUNES:

#  - ValueError: Cuando se ingresa un tipo de dato erroneo

#  - TypeError: Cuando se tipo de variable que se emplea en algo no es correspondiente para eso
#   Ejemplo:
#       nombre = input("Ingrese un nombre")
#       try:
#           for i in nombre:            // Se necesita una string en este caso
#               print(i)                // de ingresarse un numero no funcionaria el for
#       except TypeError:
#           nombre = str(nombre)
#           for i in nombre
#               print(i)

#   - NameError: Se ingreso un nombre de variable o de funcion erroneo (no existe)

#   - IndexError: Cuendo se intenta acceder a un espacio de memoria de un array que no tiene asignada

#   - KeyError: Cuando se desea conocer la pos. en la que se encuentra un elemento dentro de un array, pero
#              este elemento no existe dentro del array. Ejemplo: lista.index("Elemento")

