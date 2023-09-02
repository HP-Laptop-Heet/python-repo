'''printing the pattern 18
     A B C D E
      A B C D
       A B C
        A B
         A     '''
n=5
p=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j):
            t=65
            for k in range(p,0,-1):
                print(chr(t),end=" ")
                t=t+1
        else:
            print(end=" ")
    p=p-1
    print("\r")