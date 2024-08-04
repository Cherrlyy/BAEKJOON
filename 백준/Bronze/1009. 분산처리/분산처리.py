t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    tmp = []
    for j in range(1, b+1):
        last = str(a**j)[-1]
        if last not in tmp:
            tmp.append(last)
        else:
            break
    ans = tmp[b%len(tmp)-1]
    print(ans if ans != "0" else 10)