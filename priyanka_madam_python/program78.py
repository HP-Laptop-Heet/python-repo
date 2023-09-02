# Inheritance

class rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth

class square(rectangle):
    def __init__(self,length1,breadth1,side):
        rectangle.__init__(self,length1,breadth1)
        self.s=side
    def area_s(self):
        area_s=self.s**2
        print(area_s)
    def area(self):
        a_rectangle=self.l*self.b
        print(a_rectangle)

x=square(10,50,20)
x.area()
x.area_s()