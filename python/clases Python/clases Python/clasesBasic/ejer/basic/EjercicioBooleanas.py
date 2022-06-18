
print("Sistema de ingresos deportivos")

generoUsuario = input("Ingrese su genero(M/F): ")

esHombre = (generoUsuario=="M")

print("Es Hombre: ",esHombre)   

edadUsuario = int(input("Ingrese su Edad: "))

esMayor = (edadUsuario >= 18)

print("Es Mayor: ",esMayor)

alturaUsuario = float(input("Ingrese su altura: "))

esAlto = (alturaUsuario > 1.8)

print("Es Alto: ",esAlto)

print("Puede jugar Hockey: ", not(esHombre))

print("Puede jugar Basket: ",(esHombre == True) and (esAlto == True))

print("Puede jugar volley: ",( (esHombre == True) and (esAlto == True) ) or (esHombre == False) )

print("Puede jugar rugby: ", 17< edadUsuario <56 )

print("Gracias por consultarnos :D ")
  
  