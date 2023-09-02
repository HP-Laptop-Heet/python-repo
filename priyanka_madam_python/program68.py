#exception handling with else

try:
    print("Hello")
    print(a)                              # error will occur bcz a was not declare   and then make  print(a) as comment
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

    # "else will run when try will run without error" and also "else case will not run when except case runs"