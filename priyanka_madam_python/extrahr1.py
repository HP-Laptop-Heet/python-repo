t = int(input())
r = []
for i in range(0,t):
    rcnt = 0
    n = int(input())
    b = [int(b) for b in input().split(" ")]
    a = []
    for i in range(0,n):
        a.append(i+1)
    for i in range(0,n):
        if(a[i]!=b[i]):
            if(a[i]<b[i]):
                cnt = b[i]-a[i]
                if(cnt>=3):
                    r.append("Too chaotic")
                    break
                else:
                    rcnt+=cnt
            else:
                pass
        else:
            pass
    if(rcnt!=0):
      r.append(rcnt)

for i in r:
    print(i)
'''for i in range(0,t):
    print(r[i])'''