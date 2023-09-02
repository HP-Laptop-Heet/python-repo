'''printing the pattern 21
          *
         * *
        * * *
       * * * *
        * * *
         * *
          *     '''
# with no. of columns
n=7
for i in range(1,n+1):
    for j in range(1,n+1):      #Name : Heet kumar
        if(i+j>=n+1):           #Reg. no.: 19BCE10301
            print("*",end=" ")  #Question no.: 3
        else:
            print(end=" ")
    print("\r")
for i in range(n+1,2*n+1):
    for j in range(1,n+1):
        if(i-j<=n-1):
            print("*",end=" ")
        else:
            print(end=" ")
    print("\r")