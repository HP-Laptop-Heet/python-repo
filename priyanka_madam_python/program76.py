# class with init(constructor) function

class Person:
    def __init__(xy,fname,lname):    # in python always __init__ fuction work as a constructor
        xy.n = fname                # in place of self we can write anything
        xy.a = lname                # using self is compulsory in __init__ function
                                    # if we want to print anything in __init__ function then we need use self word

    def display_name(self):         # here self is xy variable of __init__ function
        print("Hello my name is "+self.n+self.a)
                               # if we creating a __init__ function it means we need to use init function first variable in all other function in the class as a first variable

    def print_x(abc):      # here abc is xy variable of __init__ function
        x=100
        print(x)

p =Person("Heet","kumar")
p.display_name()
p.print_x()
'''print(p.n)
print(p.a) '''