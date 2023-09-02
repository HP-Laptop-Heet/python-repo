'''printing the pattern 17
     * * * * *
      * * * *
       * * *
        * *
         *     '''
n=5
p=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j):
            for k in range(p,0,-1):
                print("*",end=" ")
        else:
            print(end=" ")
    p=p-1
    print("\r")