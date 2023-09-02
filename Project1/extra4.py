def decimalToBinary(n):
    return bin(n).replace("0b", "")


if __name__ == '__main__':
    t = int(input())
    n = list(decimalToBinary(t))
    print(n)
    z = []
    cnt = 0
    for i in range(len(n)):
        if (n[i] == '1'):
            cnt=cnt+1
            print(cnt)
        if (n[i] == '0'):
            z.append(cnt)
            cnt = 0
    if not z:
        z.append(cnt)
    print(max(z))