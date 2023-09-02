n = int(input())
dict = {}
for i in range(0,n):
    x,y = (str(a) for a in input().split())
    dict[x]=y

print(dict)

cnt = 0
while(cnt<1):
    #found = 1
    i = str(input())
    if i in dict:
        print(i+"="+dict[i])
        #found=0
    else:
        print("Not found")
    cnt=0