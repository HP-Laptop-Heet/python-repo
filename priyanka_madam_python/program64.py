# function inside function

def fun():
    x=50
    def innerfun():
        print(x)
    innerfun()

fun()