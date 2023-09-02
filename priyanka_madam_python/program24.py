'''printing the pattern 8
      1 1 1 1
      2 2 2
      3 3
      4        '''
n=5
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(i,end=" ")
    print("")