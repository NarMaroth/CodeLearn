
nombre = "Juan"

for i in nombre:  # I: Variable de iteracion/ nombre: Variable que recorrera i.
    print("Hola")

# Como Juan tiene 4 caracteres, imprimira 4 veces Hola

# Si se ingresa un Int dara error ya que el For no tiene una variable/lista que pueda recorrer

nombres = ["Juan","Pedro","Alberto"]

for i in nombres:
    print("Chau")

# Imprimira Chau tantas veces como elementos hallan en una lista. En este caso 3 veces

for i in nombres:
    print(i)

#Imprimira el elemento de esa iteracion. En el caso de una variale String, la letra de la iteracion.
#   Ejemplo:
#           for i in nombre:
#               print(i)        
# //OUTPUT:
# J
# u
# a
# n

mail = input("Ingrese su correo electronico:")

for i in mail:
    if (i == "@"):
        print("Correo Correcto")
        break
else:
    print("Mail incorrecto")    
    #Se ejecura lo que se encuentre en el cuerpo del Else cuando el For haya completado TODAS sus Iteraciones
    #de saltar el Brake en el If el For no podra recorrer toda la variable/lista y no pasara por el Else.

#---------------------

for i in mail:
    if i == "@":
        continue
    print(i)

# El Continue hace que pase el bucle pase a la siguiente iteracion sin que ejecute el resto del cuerpo

#-------------------

if 4 == 3:
    pass            # El Pass se emplea para que el compilador ignore que falta codigo en el cuerpo y ejecute
else:
    print("Pepe")

#-------------------

intentos = 3

for i in range(1,intentos):
    print(i)
