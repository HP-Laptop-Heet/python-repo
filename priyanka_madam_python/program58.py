# checking for number is a palindrome

num=int(input(" enter a number "))
t=num
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
if(rev==t):
    print(" number is palindrome")
else:
    print(" number is not palindrome")