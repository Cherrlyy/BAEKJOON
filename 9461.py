def pado_seq(n):
    dp = [0]*(n+1)
    dp[1:6] = [1, 1, 1, 2, 2]
    for i in range(6, n+1):
        dp[i] = dp[i-1] + dp[i-5]

    return dp[n]

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        print(pado_seq(int(input())))