
# Importar Tkinter:

from tkinter import *

root = Tk()

def onButtonCLicked():
    saludo = "Hola " + inputField.get()
    labelBC = Label(root, text= saludo)
    labelBC.pack()

#Creando texto para mostrar
myLabel = Label(root, text="Saludador :D")   

#Creando Boton:

button = Button(root, text="Ingrese un nombre", command=onButtonCLicked) 
# - se puede desabilitar el boton añadiendo ",state = DISABLED"  
# - añadiendo (padx = algunvalor) indicas el largo del boton. Emplear padY para el ancho
# - anadiendo (,command = nombreFuncion) ejecura la funcion al clickear el boton
# - cambiar color texto (,fg = "Blue")
# - cambiar color fondo (,bg = "Yellow")
# - cambiar tamaño del marco (, borderwidth = algunvalor)
# Agregar cosas a a ventana de la forma mas simple
myLabel.pack()

inputField = Entry(root, width= 50,borderwidth=5)
inputField.insert(0, "Nombre")  #insertar un texto en el inputField
inputField.pack()

button.pack()

#Loop principal que hace que el progama funcione (Siempre debe de ir al final)
root.mainloop()