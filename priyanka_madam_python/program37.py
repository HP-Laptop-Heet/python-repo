'''printing the pattern 20
      * * * *
       * * *
        * *
         *
         *
        * *
       * * *
      * * * *   '''
#According to the no. of columns
n=6
p=n
for i in range(1,n+1):
    for j in range(1,n+1):           #Name : Heet kumar
        if(i==j):                    #Reg. no.: 19BCE10301
            for k in range(p,0,-1):  #Question no.: 2
                print("*",end=" ")
        else:
            print(end=" ")
    p=p-1
    print("\r")
p=1
for i in range(n+1,2*n+1):
    for j in range(1,n+1):
        if(i+j==2*n+1):
            for k in range(1,p+1):
                print("*",end=" ")
        else:
            print(end=" ")
    p=p+1
    print("\r")