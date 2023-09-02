# function that checks whether a passed string is palindrome or not
def palindrome_s(s):
    rs=""
    l=len(s)
    for i in range(0,l):
        rs=rs+s[-i-1]
    return rs

st=str(input("Enter the string : "))
rev = palindrome_s(st)
if (st==rev):
    print("Given string is palindrome")
else :
    print("String is not a palindrome")