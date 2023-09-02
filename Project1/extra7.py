def count_substring(string, sub_string):
    fcnt = 0
    s = len(string)
    ss = len(sub_string)
    st = list(string)
    su = list(sub_string)
    for i in range(0, s - ss):
        cnt = 0
        for j in range(0, ss):
            if (st[i + j] == su[j]):
                cnt += 1
                if (cnt == ss):
                    fcnt += 1
                print(i+j,j)
    return fcnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)