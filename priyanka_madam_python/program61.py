# program to calculate no. of upper case and lower case in string

def no_l_u(s):
    countl,countu=0,0
    for i in s:
        if(i>="a" and i<="z"):
            countl+=1
        if(i>="A" and i<="Z"):
            countu+=1
    return countl,countu

st=str(input("Enter the string : "))
l,u=no_l_u(st)
print("No. of lowercase : ",l)
print("No. of uppercase : ",u)
