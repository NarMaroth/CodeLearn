# Importar Tkinter:
from tkinter import *
from PIL import ImageTk,Image
import sqlite3

# Crear ventana del GUI
root = Tk()
root.geometry("640x480")

#Base de datos


# Crear o conectarse a una base de datos
conn = sqlite3.connect('C:\\Users\\NarMaroth\\Desktop\\clases Python\\tutorialesSoftw\\baseDatosTest\\base_de_datos.db')  
#//si no existe lo crea

#Cursor: se encarga de la base de datos
cursor= conn.cursor()

'''
    #Create table
cursor.execute("""CREATE TABLE addresses (
        firs_Name text,
        last_Name text,
        address text,
        city text,
        state text,
        zipcode integer
    )
""")
#Solo toma 5 tipos de datos: text,integer,real(float),null,blob(imagenes/videos).
#//como ya se creo el archivo anulo esta parte del cod
'''



#Commit changes /hacer cambios en la bd
conn.commit()

#Cerrar la coneccion a la bd. No es necesario pero para asegurar
conn.close()


#Loop principal que hace que el progama funcione (Siempre debe de ir al final)
root.mainloop()