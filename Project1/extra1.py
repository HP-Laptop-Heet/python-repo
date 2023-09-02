n,q = [int(x) for x in input().split()]
lastAnswer = 0
s=[]
for i in range(0,n):
    s.append([])
for i in range(0,q):
       x1,y1,z1 =[int(x) for x in input().split()]
       if(x1==1):
           temp = (y1 ^ lastAnswer) % n
           s[temp].append(z1)
       if(x1==2):
           temp = (y1 ^ lastAnswer) % n
           y = z1 % len(s[temp])
           lastAnswer = s[temp][y]
           print(lastAnswer)