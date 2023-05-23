def consult(n):
    dp = [[0 for i in range(n)] for j in range(n)]
    flag = l[0][1]
    dp[0][l[0][0]-1:] = [l[0][1]]*(n-l[0][0]+1)
    dp = [dp[0] for i in range(n)]
    for begin in range(1, n):
        # 종료일이 퇴사일 넘어가면
        stop = begin+l[begin][0]-1
        if stop > n-1:
            dp[begin] = dp[begin-1].copy()
        else:
            for k in range(stop, n):
                new = dp[begin-1][begin-1]+l[begin][1]
                if new > dp[begin][k]:
                    dp[begin][k] = new
            flag = max(flag, new)

        dp[begin:] = [dp[begin] for i in range(n-begin)]
    return dp[n-1][n-1]


if __name__ == "__main__":
    n = int(input())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))
    print(consult(n))