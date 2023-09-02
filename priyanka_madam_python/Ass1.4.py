
print("Enter the measurments of three sides of a triangle :")
x=int(input())
y=int(input())                         # Name : Heet kumar
z=int(input())                         # Reg. no.: 19BCE10301
if(x==y==z):                           # Question no. : 4
    print("Equilateral Triangle")
elif(x==y or y==z):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")