#    Coleciones = Arrays/Vectores

# 4 Tipode de Coleciones:
# -Listas: []
# -Tuplas: ()
# -Biblioteca: {}
# -sets {}

# CUANDO USAR CUAL:
"""
When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast lookup for your data, based on a custom key.
- When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does not need random access. Try to choose lists when you
  need a simple, iterable collection that is modified frequently.
- Use a set if you need uniqueness for the elements.
- Use tuples when your data cannot change.

Many times, a tuple is used in combination with a dictionary, for example, a tuple might represent a key, 
because it's immutable.
"""

#------  LISTAS: ------ 
# Como declarar una Lista:
nombreLista = [ "obj1","obj2","obj3",2,True,2.5 ]

# Concatenar listas (+):
alumnos4A = ["Jose"]
alumnos4B = ["Juan"]

alumnosDe4to = alumnos4A + alumnos4B    
print(alumnosDe4to)

# Repetir Listas(*)
print(alumnosDe4to *2)

# Lenght: Len //Largo de algo (array,string,etc)
print( len(alumnosDe4to) )

# Max & Min :Retorna el valor de la lista con el Mayor/Menor valor
# max(lista)
# min(lista)

# Append (Agrega la variable elemento a la lista en el último índice.)
#lista.append(variable)   

# Insert (Agrega la variable en un índice determinado.)
#lista.insert(indice,variable)

# Extend (Igual que concatenar. Añade a la lista el contenido de la otra )
#lista.extend ([lista2])

# Index (Como saber en que posicion se encuentra un elemento)
#lista.index("Elemento") //Ejemplo: print(alumnos4A.index("Jose"))  Output=0

# Count (Indica la cantidad de veces que se repite una variable en la lista)
#lista.count(variable) 

# Pop (Borra la variable que ocupa el indice pedido)
#lista.pop(indice)

# Remove (Borra de la lista la variable indicada. Solo borra una variable, de estar repetida solo borrara la 1era)
#lista.remove(variable)

# Clear (Borra todo el contenido de la lista, pero no la lista)
# lista.clear()

# Reverse (Invierte el orden de los elementos de una lista)
#lista.reverse( ) 

# Sort (ordena los elementos de la lista alfabéticamente o de menor a mayor)
#lista.sort( )

# Indicar parte de una lista: print(lista[min:max]) 
#     print(lista[:max]) imprimira desde el inicio de la lista hast el valor max indicado
#     print(lista[min:]) imprimita desde el minimo indicado hasta el final de la lista

# * DEL lista elimina la lista del programa

# * Como saber si un elemento esta en una lista.
# print( "Jose" not in alumnos4B )  //Output= True


#------  TUPLAS: ------
# Las tuplas son inmodificables. Se puede ver el contenido que tiene, pero no se puede modificar de ninguna 
#forma.

# Declarar Tupla (Es igual a una Lista salvo que se usan Parentesis)
# alumnos= ("Perez","Gomez","Lopez")

# * Se puede declarar una Lista y pasarla a una Tupla
# alumnos4A= tuple(alumnos4A)
#   o viceversa
# alumnos4A= list(alumnos4A)



#------  Bibliotecas: ------

# Tambien almacenan informacion pero permiten claves/keys a valores.

# 1ero: los elementos de la biblioteca debe de estar contenidos en llaves {}
# 2ndo:   key : Value 
# (lo que este a la izquierda de los 2 puntos es la palabra clave o el identificador del valor)
# ( y lo que esta a la derecha es el valor)

# ages = {"Dave":24,"Mary":42,"John":58}
# print(ages["Dave"])
#   Output: 24

# * Para asignar un valor al diccionario es igual que en una lista salvo que el key es la posicion
#       ages[8] = 64
#       print(ages)
#   output: "dave":24,"mary":42,"john":58,8:64
