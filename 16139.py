def isin_alpha(s, c, n, m):
    new = list(s[n:m+1])

    return new.count(c)

if __name__ == '__main__':
    s = input()
    n = int(input())

    for i in range(n):
        c, n, m = input().split()
        n, m = int(n), int(m)

        print((isin_alpha(s, c, n, m)))