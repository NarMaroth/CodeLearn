
from tkinter import *

root = Tk()
root.title("Simple Calculator")

infoFIeld = Entry(root, width=50, borderwidth=5)
infoFIeld.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

number = ""
total = 0
lastOperation = ''

#var made so operations cannot be performed until it finds a number on which to perform them
start = False 


def buttonPresed(num):
    global start
    global number
    global total

    currentText= infoFIeld.get()

    # Prevent de number start with a 0
    if start == True and currentText == "0":
        start = False
        textDisplay= str(num)
    else:
        textDisplay= currentText + str(num)

    # Delete the content in the inputfield and add the knew one
    infoFIeld.delete(0,END) 
    infoFIeld.insert(0, textDisplay) 

    number = f"{number}{num}"

    # If non operation get done, the number will be the total
    if start == False:
        total = int(number)

def clearButton():
    global start
    global number
    global numero

    # When the clear button is pressed, all reset

    start = False
    lastOperation = ''
    number = ""
    total = 0

    infoFIeld.delete(0,END)

def equal():
    global total
    global number
    global lastOperation

    if start == True:

        if(lastOperation == '+'):
            total += int(number)
        elif(lastOperation == '-'):
            total -= int(number)

        infoFIeld.delete(0,END)
        infoFIeld.insert(0, total)
        
        number = ""
        lastOperation = ''
        
        
def add():
    global start
    global number
    global total 
    global lastOperation


    textDisplay= f"{infoFIeld.get()} + "
    infoFIeld.delete(0,END) 
    infoFIeld.insert(0, textDisplay) 

    if start == False:
        start = True
    
    if lastOperation == '+':
        total += int(number)
    elif lastOperation == '-':
        total -= int(number)

    number = ""
    lastOperation = '+'


def subtract():
    global start
    global number
    global total 
    global lastOperation

    textDisplay= f"{infoFIeld.get()} - "
    infoFIeld.delete(0,END) 
    infoFIeld.insert(0, textDisplay) 

    if start == False:
        start = True

    if lastOperation == '+':
        total += int(number)
    elif lastOperation == '-':
        total -= int(number)

    number = ""
    lastOperation = '-'




#   Buttons:

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonPresed(1) )
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonPresed(2) )
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonPresed(3) )
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonPresed(4) )
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonPresed(5) )
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonPresed(6) )
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonPresed(7) )
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonPresed(8) )
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonPresed(9) )
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonPresed(0) )

button_add = Button(root, text="+", padx=40, pady=20, command=add)
button_minus = Button(root, text="-", padx=40, pady=20, command=subtract)
button_equal = Button(root, text="=", padx=40, pady=20, command= equal)
button_clear = Button(root, text="Clr", padx=40, pady=20, command= clearButton)


#   Buttons Position:

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=1)

button_clear.grid(row=0, column=3)
button_add.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_equal.grid(row=3, column=3)




# Main Loop
root.mainloop()