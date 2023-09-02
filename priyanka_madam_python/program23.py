'''printing the pattern 7
      A
      A B
      A B C
      A B C D    '''
n=65
for i in range(1,6):
    for j in range(n,n+i):
        print(chr(j),end=" ")

    print("")
