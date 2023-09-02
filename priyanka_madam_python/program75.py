#creating a class

class Person:
    def __init__(xy,fname,lname):    # in python always __init__ fuction work as a constructor
        xy.n = fname                # in place of self we can write anything
        xy.a = lname                # using self is compulsory in __init__ function
        print(xy.n,xy.a)            # if we want to print anything in __init__ function then we need use self word

p =Person("Heet","kumar")
print(p.n)
print(p.a)