s = str(input())     # input string
n = int(input())     # total length of the string should be
sl = len(s)
cnt = 0
wcnt = 0
if(sl==1):
    if(s[0]=='a'):
        cnt=n
else:
 for i in range(0,n):
  for j in range(0,sl):
    wcnt+=1
    if(s[j]=='a'):
        cnt+=1
    if(wcnt==n):
      break
  if(wcnt==n):
     break

print(cnt)

