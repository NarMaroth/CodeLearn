# Importar Tkinter:
from tkinter import*
from PIL import ImageTk,Image

# Crear ventana del GUI
root = Tk()
#root.geometry("640x480")

wich_Image = 0

image_Frame = LabelFrame(root, padx=1, pady=1)

#Define UI:
#image1 = ImageTk.PhotoImage(Image.open("tutorialesSoftw\\images\\frenchDog\\1.jpg")) muy grandes
#image2 = ImageTk.PhotoImage(Image.open("tutorialesSoftw\\images\\frenchDog\\2.jpg"))
image3 = ImageTk.PhotoImage(Image.open("tutorialesSoftw\\images\\frenchDog\\3.jpg"))
image4 = ImageTk.PhotoImage(Image.open("tutorialesSoftw\\images\\frenchDog\\4.png"))
image5 = ImageTk.PhotoImage(Image.open("tutorialesSoftw\\images\\frenchDog\\5.jpg"))
image6 = ImageTk.PhotoImage(Image.open("tutorialesSoftw\\images\\frenchDog\\6.jpg"))
image7 = ImageTk.PhotoImage(Image.open("tutorialesSoftw\\images\\frenchDog\\7.jpg"))

my_Images = [image3,image4,image5,image6,image7]

image_Display = Label(image_Frame ,image=my_Images[wich_Image])


def changeImage(direcction):
    global my_Images
    global image_Display
    global wich_Image

    image_Display.grid_forget()

    wich_Image = wich_Image - direcction

    if (wich_Image < 0):
      wich_Image = len(my_Images)
    elif (wich_Image > 5):
        wich_Image = 0

    image_Display = Label(image_Frame ,image=my_Images[wich_Image])
    image_Display.grid(row=0,column=1)

left_Button = Button(root, text="<<", command=lambda: changeImage(1))
right_Button = Button(root, text=">>", command=lambda: changeImage(-1))

exit_Button = Button(root, text="Exit", command=root.quit)


#SHOW UI:
image_Frame.grid(row=0,column=1)

image_Display.grid(row=0,column=0)

left_Button.grid(row=1,column=0)
exit_Button.grid(row=1,column=1)
right_Button.grid(row=1,column=2)



#Loop principal que hace que el progama funcione (Siempre debe de ir al final)
root.mainloop()