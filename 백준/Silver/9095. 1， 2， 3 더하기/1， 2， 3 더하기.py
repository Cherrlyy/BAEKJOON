t = int(input())
for i in range(t):
    n = int(input())
    l = [0 for _ in range(n+1)]
    l[1] = 1
    for j in range(2, n+1):
        if j == 2:
            l[2] = l[1] + 1
        elif j == 3:
            l[3] = l[1] + l[2] + 1
        else:
            l[j] = l[j-3] + l[j-2] + l[j-1]
    print(l[n])