
def num_case(n):
    tmp = n%15746
    dp = [0 for i in range(tmp+1)]
    dp[1], dp[2] = 1, 2
    for i in range(3, len(dp)):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[tmp]

if __name__ == "__main__":
    n = int(input())
    print(num_case(n))