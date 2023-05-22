def coin():
    dp = [0 for x in range(k+1)]
    dp[0] = 1

    for e in range(len(c)):
        for i in range(c[e], k+1):
            dp[i] = dp[i-c[e]] + dp[i]

    return dp[k]






if __name__ == '__main__':
    n, k = map(int, input().split())
    c = []
    for i in range(n):
        c.append(int(input()))
    print(coin())