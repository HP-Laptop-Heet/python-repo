t = int(input())
for i in range(0,t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    if(len(l)==2):
      a = l[-1]
      b = l[-2]
      ans = a*b + (a-b)
    else:
      l=set(l)
      l=list(l)
      a = l[-1]
      b = l[-2]
      ans = a*b + (a-b) 
    print(ans)