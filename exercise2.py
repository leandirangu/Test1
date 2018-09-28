
class Person:
  
  def __init__(self):
    self.s = ""
    
  def getName(self):
    self.s=input("enter name:")
    
  def printName(self):
    print (self.s.upper())
my_object = Person()
my_object.getName()
my_object.printName()    