
# Importar Tkinter:

from tkinter import *

root = Tk()

def onButtonCLicked():
    labelBC = Label(root, text = "Button Clicked")
    labelBC.grid(row=4,column=1)

#Creando texto para mostrar
myLabel = Label(root, text="Hello World")   
myLabel2 = Label(root, text="JAJAJAJAJ")

#Creando Boton:

button = Button(root, text="Click Me", command=onButtonCLicked) 
# - se puede desabilitar el boton añadiendo ",state = DISABLED"  
# - añadiendo (padx = algunvalor) indicas el largo del boton. Emplear padY para el ancho
# - anadiendo (,command = nombreFuncion) ejecura la funcion al clickear el boton
# - cambiar color texto (,fg = "Blue")
# - cambiar color fondo (,bg = "Yellow")

# Agregar cosas a a ventana de la forma mas simple
#   myLabel.pack()


# Agregar cosas con el sistema de Grids
myLabel.grid(row = 0, column=0)
myLabel2.grid(row = 1, column=1)
button.grid(row = 2, column = 0)
#   El tamaño de un grid lo determina el contenido de este

#Loop principal que hace que el progama funcione (Siempre debe de ir al final)
root.mainloop()