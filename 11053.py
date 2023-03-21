def subsequence(n, a):
    dp = [1 for x in range(n)]
    print(dp)
    pre = a[0]
    for i in range(1, n):
        if a[i] > pre:
            dp[i] = dp[i-1] + 1
            pre = a[i]
        else:
            dp[i] = dp[i-1]
        print(dp[i])

    return dp[n-1]


if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    print(subsequence(n, l))
