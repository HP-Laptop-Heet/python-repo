# program to calculate sum of positive number till given number with function

def sum_num(num):
    f=1
    if(num==0):
        return f
    else:
        for i in range(1,num+1):
            f=f*i
        return f

n=int(input("Enter the number :"))
if (n>-1):
     print(sum_num(n))
else:
    print("Enter a non negative number")