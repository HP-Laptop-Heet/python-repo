# pascal triangle  in shorter way
n=7
for i in range(0,n):
    val=1
    for j in range(0,i+1):
        print(val,end=" ")
        val=val*(i-j)//(j+1)
    print("")