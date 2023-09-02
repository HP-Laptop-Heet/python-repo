'''printing the pattern 15
             A
           A B A
         A B C A B
       A B C D A B C
     A B C D E A B C D   '''
n=5
for i in range(1,n+1):
    t = 65
    for j in range(1,n+1):
        if(i+j>=n+1):
            print(chr(t),end=" ")
            t=t+1
        else:
            print(" ",end=" ")
    t = 65
    for j in range(n+1,2*n):
        if(j-i<=n-1):
            print(chr(t),end=" ")
            t=t+1
    print("\r")