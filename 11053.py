def subsequence(n, l):
    dp = [0 for i in range(n)]
    dp[0] = 1

    for i in range(1, n):
        tmp = []
        for j in range(i-1, -1, -1):
            if l[i] > l[j]:
                tmp.append(dp[j]+1)
        if len(tmp) == 0:
            dp[i] = 1
        else:
            dp[i] = max(tmp)

    return max(dp)


if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    print(subsequence(n, l))
