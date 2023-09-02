'''printing the pattern 19
             *
           * *
         * * *
       * * * *
         * * *
           * *
             *     '''
# with no. of rows
n=9
for i in range(1,((n+1)//2)+1):
    for j in range(1,((n+1)//2)+1):
        if(i+j>=((n+1)//2)+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\r")
for i in range(((n+1)//2)+1,n+1):
    for j in range(1,((n+1)//2)+1):
        if(i-j<=((n+1)//2)-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\r")