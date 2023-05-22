def tiling(n):
    dp = [0]*(n+3)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]%10007


if __name__ == "__main__":
    n = int(input())
    print(tiling(n))