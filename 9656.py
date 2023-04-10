def stone_game(n):
    dp = ['SK' for i in range(n+1)]
    dp[1:5] = ['CY', 'SK', 'SK', 'SK']
    for i in range(5, n+1):
        tmp = set([dp[i-1], dp[i-2], dp[i-3]])
        if 'CY' in tmp:
            dp[i] = 'SK'
        else:
            dp[i] = 'CY'
    return dp[n]

if __name__ == '__main__':
    n = int(input())
    print(stone_game(n))