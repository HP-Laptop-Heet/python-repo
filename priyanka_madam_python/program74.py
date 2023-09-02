#creating a class with init function
# function is called method
# class members is called data member

class Person:
    def __init__(self,name, age):    # in python always __init__ fuction work as a constructor
        self.name1 = name            # in place of self we can write anything
        self.age1 = age              # using self is compulsory in __init__ function
                                     # if we want to print anything in __init__ function then we need use self word
p =Person("Heet",19)
print(p.name1)
print(p.age1)