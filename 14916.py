def change(n):
    dp = [0 for i in range(n+1)]
    dp[2], dp[5] = 1, 1

    for i in range(3, n+1):
        if dp[i-2] != 0 and dp[i-5] != 0:
            dp[i] = min(dp[i-2], dp[i-5]) + 1
        elif dp[i-2] != 0 or dp[i-5] != 0:
            dp[i] = max(dp[i-2], dp[i-5]) + 1

    return dp[n]


if __name__ == '__main__':
    n = int(input())
    print(change(n))