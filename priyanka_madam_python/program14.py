#for loop with prime number

n=int(input("Enter any numbr : "))
cnt=0
for i in range(2,n):
    if (n%i==0):
        cnt=cnt+1
if cnt==0 :
 print(n," is prime number")
else:
 print(n," is not a prime number")