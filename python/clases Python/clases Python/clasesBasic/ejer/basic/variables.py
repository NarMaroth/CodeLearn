print("Escuela de atletismo Los Canguros")

nombre = input("Bienvenido/a. Ingrese su nombre:")

salto1 = float(input(nombre + " ingrese su 1er salto:"))
salto2 = float(input("Ingrese su 2ndo salto:"))
salto3 = float(input("Ingrese su 3er salto:"))

promedio = (salto1+salto2+salto3)/3

print("salto promedio de " + nombre + ":" + str(promedio))