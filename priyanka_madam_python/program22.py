'''printing the pattern 6
      A
      B C
      D E F
      G H I J    '''
n=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(n),end=" ")
        n=n+1
    print("")