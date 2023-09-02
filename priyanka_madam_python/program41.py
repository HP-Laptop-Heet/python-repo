'''printing the pattern 23
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1                 '''

i=7
for n in range(0,i):
    for j in range(0,i+1):
        if (n + j == i):
          for r in range(0,n+1):
            f1, f2, f3 = 1, 1, 1           #Name : Heet kumar
            p=n                            #Reg. no.: 19BCE10301
            if(p==0):                      #Question no.: 8
                f1=1
            else:
                for x in range(p,0,-1):
                    f1=f1*x
            p=n-r
            if(p==0):
                f2=1
            else:
                for y in range(p,0,-1):
                    f2=f2*y
            p=r
            if (p==0):
                f3=1
            else:
                for z in range(p, 0, -1):
                    f3 = f3 * z
            p=f1//(f2*f3)
            print(p,end=" ")
        else:
            print(end=" ")
    print("\r")