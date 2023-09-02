'''printing the pattern 11
             A
           A B
         A B C
       A B C D
                 '''

n=5
for i in range(1,n+1):
    p=65
    for j in range(1,n+1):
        if(i+j>=n+1):
            print(chr(p),end=" ")
            p=p+1
        else:
            print(" ",end=" ")
    print(" ")