# What to do :
# Open the slides of last class and:
# (1) Make Animal an abstract class
# (2) Cerate an abstract method to Animal - eat()
# (3) implement it inside Dog

"""
class Animal():
    def run(self):
        print('Im running')

class Dog(Animal):
    def bark(self):
        print('Waf!')


d = Dog()
d.bark()
"""


from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def print_hi(self):
        print('hi')

# Remember - we cannot create instances
# if abstract classes
##d=Animal()
        
class Dog(Animal):
    #When we inerit from abstrct classes
    # like when we inherit from Animal
    # we have to implement all the abstract
    # methods of the super class

    def bark(self):
        print('Waf')
    def eat(self):
        print("hi")
    

d = Dog()
d.bark()
d.eat()
d.print_hi()
