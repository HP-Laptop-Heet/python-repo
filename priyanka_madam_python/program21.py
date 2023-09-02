'''printing the pattern 5
      *
      * *
      * * *
      * * * *    '''
print("Enter the number :")
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")