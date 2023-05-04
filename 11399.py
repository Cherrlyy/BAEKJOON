def atm():
    p.sort()
    s = 0
    for i in range(n):
        s = s + p[i]*(n-i)

    return s

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))

    print(atm())