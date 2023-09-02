'''printing the pattern 9
      1 2 3 4
      1 2 3
      1 2
      1        '''
n=5
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(j,end=" ")
    print("")                  # or also you can use print("/r")

# after coming out of the i loop then we can use also print("/r")