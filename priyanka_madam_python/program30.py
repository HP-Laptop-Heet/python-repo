'''printing the pattern 14
             A
           A B A
         A B C B A
       A B C D C B A
     A B C D E D C B A   '''
n=5
for i in range(1,n+1):
    t = 65                          #Name : Heet kumar
    for j in range(1,n+1):          #Reg. no.: 19BCE10301
        if(i+j>=n+1):               #Question no.: 7
            print(chr(t),end=" ")
            t=t+1
        else:
            print(" ",end=" ")
    t = 65+i-1
    for j in range(n+1,2*n):
        if(j-i<=n-1):
            t=t-1
            print(chr(t),end=" ")
    print("\r")