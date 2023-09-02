'''printing the pattern 13
             1
           1 2 1
         1 2 3 2 1
       1 2 3 4 3 2 1
     1 2 3 4 5 4 3 2 1   '''
n=5
for i in range(1,n+1):
    t = 1
    for j in range(1,n+1):
        if(i+j>=n+1):
            print(t,end=" ")
            t=t+1
        else:
            print(" ",end=" ")
    t = i
    for j in range(n+1,2*n):
        if(j-i<=n-1):
            t=t-1
            print(t,end=" ")
    print("\r")