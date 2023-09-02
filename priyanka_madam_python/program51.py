# if we dont know that how many argument will be pass
def my_func(*kids):     # if we dont print * then it will show error
    for i in range(0,3):           # using for loop we are printing all the kids name
       print("the youngest child is "+ kids[i])

my_func("Emil","Tobias","Linus")