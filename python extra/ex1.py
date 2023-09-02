n=int(input())
l=list(map(int,input().split()))
ans = sum(l)/n
print("{0:.9f}".format(ans))