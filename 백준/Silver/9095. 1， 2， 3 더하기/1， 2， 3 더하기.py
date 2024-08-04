t = int(input())
for i in range(t):
    n = int(input())
    l = [0 for _ in range(12)]
    l[1] = 1
    l[2] = l[1] + 1
    l[3] = l[1] + l[2] + 1
    for j in range(4, n+1):
        l[j] = l[j-3] + l[j-2] + l[j-1]
    print(l[n])