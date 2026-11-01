#inheritance-is a concept in oop that allows a class (child/sub/derived)
#to inherit methods and properties from another class(parent)

#parent class
class Animal:
    #attributes-name,habitat,sound,offspring
    #constructor
    def __init__(self,name,habitat,age):
        self.name=name
        self.habitat=habitat
        self.age=age
        
    def __str__(self):
        return f"The animal is {self.name} and is {self.age} years old,found in {self.habitat}. "
    def speek (self):
        return f"{self.name} makes a sound"
#child class-inherits from animal class
class Dog(Animal):
    def __init__ (self,name,habitat,age,breed):
        Animal.__init__(self,name,age,habitat)
        self.breed=breed
    def speek(self):
        return f"{self.name} barks barks" #method overiding
    def info (self):
        return f"{self.name} ia a {self.breed}"
#cat class that inherits from animal class
class Cat(Animal):
    def __init__(self,name,habitat,age,color):
        Animal.__init__(self,name,age,habitat)
        self.color=color
    def speek(self):
        return f"{self.name} meows meows"
    def info(self):
        return f"{self.name} is a {self.color} cat"
#creating a dog object
dog1=Dog("Squishy",5,"land","Rotweiler")
print(dog1.name)
print(dog1.age)
print(dog1.habitat)
print(dog1.__str__())
#calling the speek 
print(dog1.speek())
print(dog1.info())
#creating a cat object
cat1=Cat("Axel",3,"land","black")
print(cat1.name)
print(cat1.age)
print(cat1.habitat)
print(cat1.__str__())
print(cat1.speek())
print(cat1.info())
