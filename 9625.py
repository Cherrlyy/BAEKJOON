def BABBA(k):
    dp = [[0, 0] for i in range(k+1)]
    dp[0] = [1, 0]
    for i in range(1, k+1):
        a = dp[i-1][1]
        b = dp[i-1][0] + dp[i-1][1]
        dp[i] = [a, b]

    return dp[k]

if __name__ == '__main__':
    k = int(input())
    print(*BABBA(k))
