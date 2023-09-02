def squareroot(a,b,c):
    if(a==0):
        print("Invalid Input")
    else:
       x=(-b+((b**2)-4*a*c)**0.5)/(2*a)                  # Name : Heet kumar
       y=(-b-((b**2)-4*a*c)**0.5)/(2*a)                 # Reg.no. : 19BCE10301
       d=(b**2)-4*a*c                                    # Question no.: 5
    if(d>0):
        print("Roots are real and different :")
        print("Root1 : ",x)
        print("Root2 : ",y)
    elif(d==0):
        print("Roots are real and same :")
        print("Root1 : ", x)
        print("Root2 : ", y)
    else:
        print("Roots are complex :")
        print("Root1 : ", x)
        print("Root2 : ", y)

print("Enter the co-efficient of x^2 :")
a=int(input())
print("Enter the co-efficient of x :")
b=int(input())
print("Enter the constant value :")
c=int(input())
squareroot(a,b,c)