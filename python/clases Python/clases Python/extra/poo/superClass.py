# Super Clases contienen caracteristicas que comparten barias clases, estas se las puede asigar a una clase
#indicandola al principio en la declaracion entre parentesis

class Animal: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

class Cat(Animal):
  def purr(self):
    print("Purr...")
        
class Dog(Animal):
  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()