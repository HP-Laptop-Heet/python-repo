#for loop with prime number between 1 to 100

for j in range(1,101):

    cnt=0
    for i in range(2,j):

        if (j%i==0):
          cnt=cnt+1

    if cnt==0 :
      print(j," is prime number")
