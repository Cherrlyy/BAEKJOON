def change(n):
    if n < 5:
        dp = [-1 for i in range(6)]
    else:
        dp = [-1 for i in range(n+1)]

    dp[2], dp[5] = 1, 1

    for i in range(3, n+1):
        if dp[i-2] != -1 and dp[i-5] != -1:
            dp[i] = min(dp[i-2], dp[i-5]) + 1
        elif dp[i-2] != -1 or dp[i-5] != -1:
            dp[i] = max(dp[i-2], dp[i-5]) + 1
    return dp[n]


if __name__ == '__main__':
    n = int(input())
    print(change(n))