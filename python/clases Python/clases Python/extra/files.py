
"""

OPEN A FILE:----------------------------------------------

myFile = open("Directorio del archivo")

(En el caso de que el archivo se encuentre en el mismo directorio en el que se esta trabajando basta con solo
ingresar el nombre del archivo necesario)

* Puedes indicar el modo en el que deseas abrir el archico como 2ndo argumento:

    -Modo Lectura:
    open("Filename.txt","r")

    -Modo Escitura: (Para sobrescribir el contenido de un archivo)
    open("Filename.txt","w")

    -Modo Append: (Para añadir nuevo contenido al final del archivo)
    open("Filename.txt","a")

    -Modo Binario: (Que se emplea para archivos que no son de texto como imagenes o sonidos)
    open("Filename.txt","b")

    -Modo Escritura Binaria:
    open("Filename.txt","wb")


* Una vez que un archivo fue abierto debe ser Carrado con el metodo Close()

    myFile.Close()



READ FILE:----------------------------------------------

* Leer el contenido de un archivo de texto:

    file = open("filename.txt", "r")
    cont = file.read()
    print(cont)
    file.close()

Se puede indicar cuanto se desea leer de un archivo de texto: (one character is one byte)
    file = open("filename.txt", "r")
    print(file.read(16))
    file.close()

El metodo readlines() permite separar el contenido del texto en las lineas de cada una.
    file = open("filename.txt", "r")
    print(file.readlines())
    file.close()
    OUTPUT: ['Line 1 text \n', 'Line 2 text \n', 'Line 3 text']
    
    Ademas se puede emplear para iterar por cada linar mediante un For:
    file = open("filename.txt", "r")

    for line in file:
        print(line)

    file.close() 

    OUTPUT:
        Line 1 text

        Line 2 text

        Line 3 text

WRITE FILES:

    Para escribir en un archivo se emplea el metodo Write() y se debe de abrir en archivo en modo escitura

    file = open("newfile.txt", "w")
    file.write("This has been written to a file")
    file.close()

    file = open("newfile.txt", "r")
    print(file.read())
    file.close()

    ** IMPORTATE ** 
    Cuando se habre un archivo en modo de escritura, todo el contenido que tubiese hasta ese momento se borra


EXTRA:

    Para asegurar que se cierre un archivo es buena practica usar Try y Finally:

        try:
        f = open("filename.txt")
        print(f.read())
        finally:
        f.close()

    Otra forma de hacerlo es empleando With.
    
        with open("filename.txt") as f:
            print(f.read())
            
    De esta forma se crea una variable temporal que solo durara lo que se emplee With.

"""