
print("Enter Electricity units :")
x=int(input())
total=0
if (x <= 50):                               # Name : Heet kumar
    total = total + (x * 0.5)               # Reg. no.: 19BCE10301
else:                                       # Question no. : 6
    x = x - 50
    total = total + (50 * 0.5)
    if (x <= 100):
        total = total + (x * 0.75)
    else:
        x = x - 100
        total = total + (100 * 0.75)
        if (x <= 100):
            total = total + (x * 1.20)
        else:
            x = x - 100
            total = total + (100 * 1.20)
            if (x > 0):
                total = total + (x * 1.50)
total=total+(total*0.2)                      # Additional Surcharges 20%
print("Total Bill : ",total)