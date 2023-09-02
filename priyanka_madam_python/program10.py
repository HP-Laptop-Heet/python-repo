# sum of the even number in 1 to 100
sum=0
for i in range(0,101,2):    # or use for i in range(1,101)
    sum=sum+i               #  if(i%2==0)  sum=sum+i
print(sum)