class vehicle:
    def __init__(self,mileage,price):
        self.vmilage=mileage
        self.vprice=price-(price*0.18)
class car(vehicle):
    def __init__(self,ocost,warr,scap,ftype,milage):
        super().__init__(milage,ocost)
        self.ocost=ocost
        self.warr=warr
        self.scap=scap
        self.ftype=ftype
class bike(vehicle):
    def __init__(self,ocost,ncylinder,ngears,ctype,wtype,ftsize,milage):
        super().__init__(milage,ocost)
        self.ocost=ocost
        self.ncylinder=ncylinder
        self.ngears=ngears
        self.ctype=ctype
        self.wtype=wtype
        self.ftsize=ftsize
class audi(car):
    def __init__(self,ocost,warr,scap,ftype,milage,mtype):
        super().__init__(ocost,warr,scap,ftype,milage)
        self.mtype=mtype

    def showall(self):
        print(self.ocost,self.warr,self.scap,self.ftype,self.vmilage,self.vprice,self.mtype)

class ford(car):
    def __init__(self,ocost,warr,scap,ftype,milage,mtype):
        super().__init__(ocost,warr,scap,ftype,milage)
        self.mtype=mtype

    def showall(self):
        print(self.ocost,self.warr,self.scap,self.ftype,self.vmilage,self.vprice,self.mtype)
class bajaj(bike):
    def __init__(self,mtype,ocost,ncylinder,ngears,ctype,wtype,ftsize,milage):
        super().__init__(ocost,ncylinder,ngears,ctype,wtype,ftsize,milage)
        self.mtype=mtype

    def showall(self):
        print(self.mtype,self.ocost,self.ncylinder,self.ngears,self.ctype,self.wtype,self.ftsize,self.vmilage,self.vprice)
class tvs(bike):
    def __init__(self,mtype,ocost,ncylinder,ngears,ctype,wtype,ftsize,milage):
        super().__init__(ocost,ncylinder,ngears,ctype,wtype,ftsize,milage)
        self.mtype=mtype

    def showall(self):
        print(self.mtype,self.ocost,self.ncylinder,self.ngears,self.ctype,self.wtype,self.ftsize,self.vmilage,self.vprice)

audi = audi(5000000, "4 Years", "6","Petrol" ,"20 L","i8")
ford = ford(2300000, "3 Years", "4","Diseal","25 L","X7")
tvs = tvs("iron",40000,5,3, "liquid", "alloy", "19 L","3km")
bajaj = bajaj("iron",30000,5,3, "air", "spokes", "13 L","3km")
print(audi.showall())
print(ford.showall())
print(tvs.showall())
print(bajaj.showall())