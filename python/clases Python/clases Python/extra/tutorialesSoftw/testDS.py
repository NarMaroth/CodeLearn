# Importar Tkinter:
from tkinter import*
from PIL import ImageTk,Image

# Crear ventana del GUI
root = Tk()
root.geometry("1000x600")

channels_Frame = LabelFrame(root, padx=1, pady=1)
images_Frame = LabelFrame(root, padx=1, pady=1)

channels = StringVar()
channels.set("Default")

category = OptionMenu(channels_Frame, channels, "Channel_1", "Channel_2")




channels_Frame.grid(row=0, column=0)
images_Frame.grid(row=0,column=1)

category.grid(row=0, column=0)

#Loop principal que hace que el progama funcione (Siempre debe de ir al final)
root.mainloop()