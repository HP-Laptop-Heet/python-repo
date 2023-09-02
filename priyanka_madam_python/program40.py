'''printing the pattern 22

A B C D E F G F E D C B A
A B C D E F   F E D C B A
A B C D E       E D C B A
A B C D           D C B A
A B C               C B A
A B                   B A
A                       A
                            '''
#Enter no of rows
n=9
for i in range(1,n+1):
    t=65
    for j in range(1,n+1):
        if(i+j<=n+1):
            print(chr(t),end=" ")      #Name : Heet kumar
            t=t+1                      #Reg. no.: 19BCE10301
        else:                          #Question no.: 6
            print(" ",end=" ")
    t=65+n-2
    for j in range(n + 1, 2 * n):
        if (j-i>=n-1):
            print(chr(t), end=" ")
            t = t - 1
        else:
            print(" ", end=" ")
            t = t - 1
    print("\r")