'''printing the pattern 21
          A
         A B
        A B C
       A B C D
        E F G
         H I
          J     '''
# with no. of columns
n=6
for i in range(1,n+1):
    t=65
    for j in range(1,n+1):
        if(i+j>=n+1):
            print(chr(t),end=" ")    #Name : Heet kumar
            t=t+1                    #Reg. no.: 19BCE10301
        else:                        #Question no.: 5
            print(end=" ")
    print("\r")
t=65+n
for i in range(n+1,2*n+1):
    for j in range(1,n+1):
        if(i-j<=n-1):
            print(chr(t),end=" ")
            t=t+1
        else:
            print(end=" ")
    print("\r")