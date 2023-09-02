# writing a program for fibonacci series using Recurssion function

def fibonacci(n1,n2,sum,n):
    if(n2<=n):
        n1=n2
        n2=sum
        sum=n1+n2
        print(sum)
        fibonacci(n1,n2,sum,n)
    else:
        return 1


n=int(input("Enter the number : "))
a=0
b=1
sum=0
print(a)
fibonacci(a,b,sum,n)