"""
Generators: Son listas en las cuales solo se puede iterar una vez


Yield: es como RETURN pero retorna Generators
"""

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i


mygenerator = createGenerator() # create a generator

print(mygenerator) # mygenerator is an object!

for i in mygenerator:
    print(i)

"""
To master yield, you must understand that when you call the function, the code you 
have written in the function body does not run. The function only returns the generator 
object, this is a bit tricky :-)

Then, your code will continue from where it left off each time for uses the generator.

Now the hard part:

The first time the for calls the generator object created from your function, it will 
run the code in your function from the beginning until it hits yield, then it'll return 
the first value of the loop. Then, each subsequent call will run another iteration of 
the loop you have written in the function and return the next value. This will continue 
until the generator is considered empty, which happens when the function runs without 
hitting yield. That can be because the loop has come to an end, or because you no longer 
satisfy an "if/else".
"""

def plus(n):
    yield n                 #Si es la 1era vez que se ejecuta esta funcion corre esta l.
    yield from plus(n+1)    #Sino corre esta

# como es yield entregara una variable generator que solo se podra leer 1na vez
