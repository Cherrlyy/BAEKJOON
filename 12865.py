def bag():
    dp = [0 for x in range(k+1)]
    dp[0] = 1


if __name__ == '__main__':
    n, k = map(int, input().split())
    c = []

    for _ in range(n):
        c.append(int(input()))
