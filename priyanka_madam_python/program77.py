# creating class without init (constructor) function

class person:                          # in python in class by default everything is public
    x=100
    def display_name(xyz,mname,age):         #  _ (single underscored means before variable or method(function) will be) protected
        xyz._a=age                           # __ (double underscored means before variable or method(function) will be) private
        xyz.m=mname                          #   (without underscored means before variable or method(function) will be) public
        print("Hello my name is "+ xyz.m)
        print(xyz.x)

a=person()
a.display_name("Heet",19)
print(a._a)

'''protected members will be called only in inherited class and in main function and also can be called when that
    particular class is called only
    
   private members will be called within the class only outside the class it cannot be called
    
   public members can be called anywhere in the program '''
