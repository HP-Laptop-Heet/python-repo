# nested if program
print("Enter the number :")
x=int(input())               #type casting
if(x>0):
    if (x % 2 == 0):
        print("Even")
    else:
        print("ODD")
else:
    print("Negative number")