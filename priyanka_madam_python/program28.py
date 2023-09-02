'''printing the pattern 12
             1
           2 2 2
         3 3 3 3 3
       4 4 4 4 4 4 4
     5 5 5 5 5 5 5 5 5   '''
n=6
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i+j>=n+1):
            print(i,end=" ")
        else:
            print(" ",end=" ")
    for j in range(n+1,2*n):
        if(j-i<=n-1):
            print(i,end=" ")
    print("\r")