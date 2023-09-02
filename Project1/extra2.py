if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    m = arr[-1]
    b = []
    for i in range(0, n):
        if(arr[i] < m):
          b.append(arr[i])
    x = b[-1]
    print(x)