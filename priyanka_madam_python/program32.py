'''printing the pattern 16
             *
            * *
           * * *
          * * * *       '''
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i+j==n+1):
            for k in range(1,i+1):
                print("*",end=" ")
        else:
            print(end=" ")
    print("\r")