def part_sequence():
    dp = l[:]
    for i in range(1, n):
        dp[i] = max(dp[i-1]+l[i], l[i])
    return max(dp)




if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    print(part_sequence())